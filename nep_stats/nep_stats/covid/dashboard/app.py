import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from nep_stats.config import engine
from nep_stats.utils import GeoJson
from nep_stats.covid.dashboard.figs import nepal_map

mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"
px.set_mapbox_access_token(mapbox_access_token)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


def df_to_data_table(df, id=None):
    return dash_table.DataTable(id=id,
                                columns=[{'name': i, 'id': i}
                                         for i in df.columns],
                                data=df.to_dict('records'))


# covid cases over time
sql = """
select
	cc.created_on::date "Date",
	count(*) "Count"
from
	covid_cases cc
group by
	cc.created_on::date
order by cc.created_on::date desc ;
"""
daily_cases_count_df = pd.read_sql(sql, engine)
cases_over_time_fig = px.line(
    daily_cases_count_df, x='Date', y='Count', title='Cases over time')
cases_over_time_fig.update_layout(margin={"r": 0, "t": 30, "l": 0, "b": 0})

# count of current covid cases
sql = """
select
	cc.current_state "Current State",
	count(*) "Count"
from
	covid_cases cc
group by
	cc.current_state ;
"""
cases_state_df = pd.read_sql(sql, engine)
sql = '''
with latest_dates as (
select
	qi.province_id ,
	qi.district_id ,
	max(qi.created_on) as created_on
from
	quarantine_info qi
group by
	qi.province_id ,
	qi.district_id )
select
	p.title_en as province,
	sum(qi.quarantined_count) quarantine,
	cast (sum(qi.quarantined_count)/max(p.population) *100 as DECIMAL(5,2))as quarantine_percentage 
from
	latest_dates ld
join quarantine_info qi on
	ld.province_id = qi.province_id
	and ld.district_id = qi.district_id
	and ld.created_on = qi.created_on
join provinces p on
	qi.province_id = p.id
group by
	p.title_en ;

'''
cases_per_district_qurantine_df = pd.read_sql(sql, engine)
sql = '''
with cases_per_province_per_day as ( with dates as (
select
	date_trunc('day', dd)::date as date
from
	generate_series ( '2020-04-01'::timestamp ,
	'2020-06-01'::timestamp ,
	'1 day'::interval) dd )
select
	p.id,
	p.title_en province,
	c.date,
	coalesce(a.count, 0) count
from
	dates as c
cross join (
	select
		distinct cc.province_id
	from
		covid_cases cc) as i
left outer join (
	select
		province_id,
		created_on::date,
		count(*)
	from
		covid_cases
	group by
		province_id,
		created_on::date) as a on
	c.date = a.created_on
	and a.province_id = i.province_id
join provinces p on
	p.id = i.province_id)
select
	id,
	province,
	date,
	count,
	sum(count) over (partition by province
order by
	date asc rows between unbounded preceding and current row) as cum_sum
from
	cases_per_province_per_day
order by
	province,
	date;

 ;'''
cases_per_province_df = pd.read_sql(sql, engine)
cases_per_province_df['date_str'] = cases_per_province_df['date'].astype('str')
cases_per_state_fig = px.pie(cases_state_df,
                             names='Current State', color='Current State', values='Count', title="Number of cases per status",
                             color_discrete_map={'active': 'cyan',
                                                 'recovered':'green',
                                                 'death':'red'
                                                 })
cases_per_state_fig.update_layout(margin={"r": 0, "t": 30, "l": 0, "b": 0})
cases_per_province_fig = px.bar(cases_per_province_df,
                                x="province", y="cum_sum", color="province",
                                animation_frame="date_str", range_y=(0, 700))

main_container = dbc.Container([
    dbc.Row(html.H1("Covid19 Stats")),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=cases_over_time_fig, responsive=True),
            dcc.Graph(figure=cases_per_state_fig)
        ], width=4),

        # dbc.Col(dcc.Graph(figure=nepal_map.get_map()), width=8),
        dbc.Col([
            df_to_data_table(df=cases_per_district_qurantine_df, id='quarantinetable'),
            dcc.Graph(figure=cases_per_province_fig)
        ]),
    ])
], fluid=True)

app.layout = main_container

if __name__ == "__main__":
    app.run_server(debug=True)
