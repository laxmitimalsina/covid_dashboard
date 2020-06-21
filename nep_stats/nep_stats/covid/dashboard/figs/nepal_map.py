import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from nep_stats.config import engine
from nep_stats.utils import GeoJson

mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"
px.set_mapbox_access_token(mapbox_access_token)


def get_map():
    sql = """
with cases_per_province_per_day as ( with dates as (
select
	date_trunc('day', dd)::date as date
from
	generate_series ( '2020-04-01'::timestamp , '2020-06-01'::timestamp , '1 day'::interval) dd )
select
	p.id, p.title_en province, p.centroid->'coordinates'->0 long, p.centroid->'coordinates'->1 lat, c.date, coalesce(a.count, 0) count
from
	dates as c
cross join (
	select
		distinct cc.province_id
	from
		covid_cases cc) as i
left outer join (
	select
		province_id, created_on::date, count(*)
	from
		covid_cases
	group by
		province_id, created_on::date) as a on
	c.date = a.created_on
	and a.province_id = i.province_id
join provinces p on
	p.id = i.province_id)
select
	id,
	province,
	long,
	lat,
	to_char(date, 'MMDD') date,
	count,
	sum(count) over (partition by province
order by
	date asc rows between unbounded preceding and current row) as cum_sum
from
	cases_per_province_per_day
order by
	province,
	date;
"""
    per_province_count_df = pd.read_sql(sql, engine)
    per_province_count_map = px.scatter_mapbox(per_province_count_df, lat='lat', lon='long',
                                               mapbox_style='carto-positron',
                                               color='cum_sum', size='cum_sum',
                                               center={'lat': 28.3949,
                                                       'lon': 84.1240},
                                               range_color=(
                                                   0, per_province_count_df['cum_sum'].max()),
                                               zoom=5.4, height=700, animation_frame='date')

    per_province_count_map = px.choropleth_mapbox(per_province_count_df, geojson=GeoJson.get_provinces_geojson(),
                                                  locations='id',
                                                  featureidkey='properties.ADM1_EN',
                                                  color='cum_sum', hover_name='province',
                                                  color_continuous_scale="Viridis",
                                                  range_color=(
                                                      0, per_province_count_df['cum_sum'].max()),
                                                  mapbox_style="carto-positron",
                                                  zoom=6.2, center={'lon': 84.1240, 'lat': 28.3949},
                                                  opacity=0.5, height=700, animation_frame='date',
                                                  )
    # per_province_count_map.update_geos(fitbounds="locations", visible=False)
    # counts = per_province_count_df['count']
    # per_province_count_map.add_trace(go.Scattermapbox(lat=per_province_count_df['lat'], lon=per_province_count_df['long'], mode='markers', marker={
    #     'sizemode': 'area', 'sizemin': 8, 'size': counts, 'sizeref': 2.*max(counts)/(60.**2)}))
    per_province_count_map.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return per_province_count_map
