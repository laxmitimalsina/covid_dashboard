# bipad_api
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import bipad_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import bipad_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import bipad_api
from bipad_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = bipad_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = bipad_api.ApiApi(bipad_api.ApiClient(configuration))
version = 'version_example' # str | 
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.api_agriculture_type_list(version, search=search, ordering=ordering, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_agriculture_type_list: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://bipad.gov.np*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiApi* | [**api_agriculture_type_list**](docs/ApiApi.md#api_agriculture_type_list) | **GET** /api/{version}/agriculture-type/ | 
*ApiApi* | [**api_agriculture_type_read**](docs/ApiApi.md#api_agriculture_type_read) | **GET** /api/{version}/agriculture-type/{id}/ | 
*ApiApi* | [**api_alert_list**](docs/ApiApi.md#api_alert_list) | **GET** /api/{version}/alert/ | 
*ApiApi* | [**api_alert_read**](docs/ApiApi.md#api_alert_read) | **GET** /api/{version}/alert/{id}/ | 
*ApiApi* | [**api_citizen_report_create**](docs/ApiApi.md#api_citizen_report_create) | **POST** /api/{version}/citizen-report/ | 
*ApiApi* | [**api_citizen_report_list**](docs/ApiApi.md#api_citizen_report_list) | **GET** /api/{version}/citizen-report/ | 
*ApiApi* | [**api_citizen_report_read**](docs/ApiApi.md#api_citizen_report_read) | **GET** /api/{version}/citizen-report/{id}/ | 
*ApiApi* | [**api_contact_training_list**](docs/ApiApi.md#api_contact_training_list) | **GET** /api/{version}/contact-training/ | 
*ApiApi* | [**api_contact_training_read**](docs/ApiApi.md#api_contact_training_read) | **GET** /api/{version}/contact-training/{id}/ | 
*ApiApi* | [**api_country_list**](docs/ApiApi.md#api_country_list) | **GET** /api/{version}/country/ | 
*ApiApi* | [**api_country_read**](docs/ApiApi.md#api_country_read) | **GET** /api/{version}/country/{id}/ | 
*ApiApi* | [**api_covid19_case_list**](docs/ApiApi.md#api_covid19_case_list) | **GET** /api/{version}/covid19-case/ | 
*ApiApi* | [**api_covid19_case_read**](docs/ApiApi.md#api_covid19_case_read) | **GET** /api/{version}/covid19-case/{id}/ | 
*ApiApi* | [**api_covid19_immigrant_country_list**](docs/ApiApi.md#api_covid19_immigrant_country_list) | **GET** /api/{version}/covid19-immigrant-country/ | 
*ApiApi* | [**api_covid19_immigrant_country_read**](docs/ApiApi.md#api_covid19_immigrant_country_read) | **GET** /api/{version}/covid19-immigrant-country/{id}/ | 
*ApiApi* | [**api_covid19_immigrant_create**](docs/ApiApi.md#api_covid19_immigrant_create) | **POST** /api/{version}/covid19-immigrant/ | 
*ApiApi* | [**api_covid19_immigrant_district_list**](docs/ApiApi.md#api_covid19_immigrant_district_list) | **GET** /api/{version}/covid19-immigrant-district/ | 
*ApiApi* | [**api_covid19_immigrant_district_read**](docs/ApiApi.md#api_covid19_immigrant_district_read) | **GET** /api/{version}/covid19-immigrant-district/{id}/ | 
*ApiApi* | [**api_covid19_immigrant_list**](docs/ApiApi.md#api_covid19_immigrant_list) | **GET** /api/{version}/covid19-immigrant/ | 
*ApiApi* | [**api_covid19_immigrant_read**](docs/ApiApi.md#api_covid19_immigrant_read) | **GET** /api/{version}/covid19-immigrant/{id}/ | 
*ApiApi* | [**api_covid19_nationalinfo_list**](docs/ApiApi.md#api_covid19_nationalinfo_list) | **GET** /api/{version}/covid19-nationalinfo/ | 
*ApiApi* | [**api_covid19_nationalinfo_read**](docs/ApiApi.md#api_covid19_nationalinfo_read) | **GET** /api/{version}/covid19-nationalinfo/{id}/ | 
*ApiApi* | [**api_covid19_quarantineinfo_create**](docs/ApiApi.md#api_covid19_quarantineinfo_create) | **POST** /api/{version}/covid19-quarantineinfo/ | 
*ApiApi* | [**api_covid19_quarantineinfo_delete**](docs/ApiApi.md#api_covid19_quarantineinfo_delete) | **DELETE** /api/{version}/covid19-quarantineinfo/{id}/ | 
*ApiApi* | [**api_covid19_quarantineinfo_list**](docs/ApiApi.md#api_covid19_quarantineinfo_list) | **GET** /api/{version}/covid19-quarantineinfo/ | 
*ApiApi* | [**api_covid19_quarantineinfo_partial_update**](docs/ApiApi.md#api_covid19_quarantineinfo_partial_update) | **PATCH** /api/{version}/covid19-quarantineinfo/{id}/ | 
*ApiApi* | [**api_covid19_quarantineinfo_read**](docs/ApiApi.md#api_covid19_quarantineinfo_read) | **GET** /api/{version}/covid19-quarantineinfo/{id}/ | 
*ApiApi* | [**api_covid19_quarantineinfo_update**](docs/ApiApi.md#api_covid19_quarantineinfo_update) | **PUT** /api/{version}/covid19-quarantineinfo/{id}/ | 
*ApiApi* | [**api_covid19_situationreport_list**](docs/ApiApi.md#api_covid19_situationreport_list) | **GET** /api/{version}/covid19-situationreport/ | 
*ApiApi* | [**api_covid19_travelhistory_list**](docs/ApiApi.md#api_covid19_travelhistory_list) | **GET** /api/{version}/covid19-travelhistory/ | 
*ApiApi* | [**api_covid19_travelhistory_read**](docs/ApiApi.md#api_covid19_travelhistory_read) | **GET** /api/{version}/covid19-travelhistory/{id}/ | 
*ApiApi* | [**api_covid19_verifiedimmigrant_list**](docs/ApiApi.md#api_covid19_verifiedimmigrant_list) | **GET** /api/{version}/covid19-verifiedimmigrant/ | 
*ApiApi* | [**api_covid19_verifiedimmigrant_read**](docs/ApiApi.md#api_covid19_verifiedimmigrant_read) | **GET** /api/{version}/covid19-verifiedimmigrant/{id}/ | 
*ApiApi* | [**api_demographic_list**](docs/ApiApi.md#api_demographic_list) | **GET** /api/{version}/demographic/ | 
*ApiApi* | [**api_demographic_read**](docs/ApiApi.md#api_demographic_read) | **GET** /api/{version}/demographic/{id}/ | 
*ApiApi* | [**api_disability_type_list**](docs/ApiApi.md#api_disability_type_list) | **GET** /api/{version}/disability-type/ | 
*ApiApi* | [**api_disability_type_read**](docs/ApiApi.md#api_disability_type_read) | **GET** /api/{version}/disability-type/{id}/ | 
*ApiApi* | [**api_district_list**](docs/ApiApi.md#api_district_list) | **GET** /api/{version}/district/ | 
*ApiApi* | [**api_district_read**](docs/ApiApi.md#api_district_read) | **GET** /api/{version}/district/{id}/ | 
*ApiApi* | [**api_document_category_list**](docs/ApiApi.md#api_document_category_list) | **GET** /api/{version}/document-category/ | 
*ApiApi* | [**api_document_category_read**](docs/ApiApi.md#api_document_category_read) | **GET** /api/{version}/document-category/{id}/ | 
*ApiApi* | [**api_document_list**](docs/ApiApi.md#api_document_list) | **GET** /api/{version}/document/ | 
*ApiApi* | [**api_document_read**](docs/ApiApi.md#api_document_read) | **GET** /api/{version}/document/{id}/ | 
*ApiApi* | [**api_earthquake_list**](docs/ApiApi.md#api_earthquake_list) | **GET** /api/{version}/earthquake/ | 
*ApiApi* | [**api_earthquake_read**](docs/ApiApi.md#api_earthquake_read) | **GET** /api/{version}/earthquake/{id}/ | 
*ApiApi* | [**api_earthquake_riskscore_list**](docs/ApiApi.md#api_earthquake_riskscore_list) | **GET** /api/{version}/earthquake-riskscore/ | 
*ApiApi* | [**api_earthquake_riskscore_read**](docs/ApiApi.md#api_earthquake_riskscore_read) | **GET** /api/{version}/earthquake-riskscore/{id}/ | 
*ApiApi* | [**api_enum_choice_list**](docs/ApiApi.md#api_enum_choice_list) | **GET** /api/{version}/enum-choice/ | 
*ApiApi* | [**api_event_list**](docs/ApiApi.md#api_event_list) | **GET** /api/{version}/event/ | 
*ApiApi* | [**api_event_read**](docs/ApiApi.md#api_event_read) | **GET** /api/{version}/event/{id}/ | 
*ApiApi* | [**api_fire_list**](docs/ApiApi.md#api_fire_list) | **GET** /api/{version}/fire/ | 
*ApiApi* | [**api_fire_read**](docs/ApiApi.md#api_fire_read) | **GET** /api/{version}/fire/{id}/ | 
*ApiApi* | [**api_fiscal_year_list**](docs/ApiApi.md#api_fiscal_year_list) | **GET** /api/{version}/fiscal-year/ | 
*ApiApi* | [**api_fiscal_year_read**](docs/ApiApi.md#api_fiscal_year_read) | **GET** /api/{version}/fiscal-year/{id}/ | 
*ApiApi* | [**api_hazard_list**](docs/ApiApi.md#api_hazard_list) | **GET** /api/{version}/hazard/ | 
*ApiApi* | [**api_hazard_read**](docs/ApiApi.md#api_hazard_read) | **GET** /api/{version}/hazard/{id}/ | 
*ApiApi* | [**api_incident_feedback_create**](docs/ApiApi.md#api_incident_feedback_create) | **POST** /api/{version}/incident-feedback/ | 
*ApiApi* | [**api_incident_feedback_list**](docs/ApiApi.md#api_incident_feedback_list) | **GET** /api/{version}/incident-feedback/ | 
*ApiApi* | [**api_incident_feedback_read**](docs/ApiApi.md#api_incident_feedback_read) | **GET** /api/{version}/incident-feedback/{id}/ | 
*ApiApi* | [**api_incident_list**](docs/ApiApi.md#api_incident_list) | **GET** /api/{version}/incident/ | 
*ApiApi* | [**api_incident_profile_list**](docs/ApiApi.md#api_incident_profile_list) | **GET** /api/{version}/incident-profile/ | 
*ApiApi* | [**api_incident_profile_read**](docs/ApiApi.md#api_incident_profile_read) | **GET** /api/{version}/incident-profile/{id}/ | 
*ApiApi* | [**api_incident_read**](docs/ApiApi.md#api_incident_read) | **GET** /api/{version}/incident/{id}/ | 
*ApiApi* | [**api_infrastructure_type_list**](docs/ApiApi.md#api_infrastructure_type_list) | **GET** /api/{version}/infrastructure-type/ | 
*ApiApi* | [**api_infrastructure_type_read**](docs/ApiApi.md#api_infrastructure_type_read) | **GET** /api/{version}/infrastructure-type/{id}/ | 
*ApiApi* | [**api_infrastructure_unit_list**](docs/ApiApi.md#api_infrastructure_unit_list) | **GET** /api/{version}/infrastructure-unit/ | 
*ApiApi* | [**api_infrastructure_unit_read**](docs/ApiApi.md#api_infrastructure_unit_read) | **GET** /api/{version}/infrastructure-unit/{id}/ | 
*ApiApi* | [**api_inventory_category_list**](docs/ApiApi.md#api_inventory_category_list) | **GET** /api/{version}/inventory-category/ | 
*ApiApi* | [**api_inventory_category_read**](docs/ApiApi.md#api_inventory_category_read) | **GET** /api/{version}/inventory-category/{id}/ | 
*ApiApi* | [**api_inventory_item_list**](docs/ApiApi.md#api_inventory_item_list) | **GET** /api/{version}/inventory-item/ | 
*ApiApi* | [**api_inventory_item_read**](docs/ApiApi.md#api_inventory_item_read) | **GET** /api/{version}/inventory-item/{id}/ | 
*ApiApi* | [**api_inventory_list**](docs/ApiApi.md#api_inventory_list) | **GET** /api/{version}/inventory/ | 
*ApiApi* | [**api_inventory_read**](docs/ApiApi.md#api_inventory_read) | **GET** /api/{version}/inventory/{id}/ | 
*ApiApi* | [**api_layer_group_list**](docs/ApiApi.md#api_layer_group_list) | **GET** /api/{version}/layer-group/ | 
*ApiApi* | [**api_layer_group_read**](docs/ApiApi.md#api_layer_group_read) | **GET** /api/{version}/layer-group/{id}/ | 
*ApiApi* | [**api_layer_list**](docs/ApiApi.md#api_layer_list) | **GET** /api/{version}/layer/ | 
*ApiApi* | [**api_layer_read**](docs/ApiApi.md#api_layer_read) | **GET** /api/{version}/layer/{id}/ | 
*ApiApi* | [**api_livestock_type_list**](docs/ApiApi.md#api_livestock_type_list) | **GET** /api/{version}/livestock-type/ | 
*ApiApi* | [**api_livestock_type_read**](docs/ApiApi.md#api_livestock_type_read) | **GET** /api/{version}/livestock-type/{id}/ | 
*ApiApi* | [**api_loss_agriculture_list**](docs/ApiApi.md#api_loss_agriculture_list) | **GET** /api/{version}/loss-agriculture/ | 
*ApiApi* | [**api_loss_agriculture_read**](docs/ApiApi.md#api_loss_agriculture_read) | **GET** /api/{version}/loss-agriculture/{id}/ | 
*ApiApi* | [**api_loss_family_list**](docs/ApiApi.md#api_loss_family_list) | **GET** /api/{version}/loss-family/ | 
*ApiApi* | [**api_loss_family_read**](docs/ApiApi.md#api_loss_family_read) | **GET** /api/{version}/loss-family/{id}/ | 
*ApiApi* | [**api_loss_infrastructure_list**](docs/ApiApi.md#api_loss_infrastructure_list) | **GET** /api/{version}/loss-infrastructure/ | 
*ApiApi* | [**api_loss_infrastructure_read**](docs/ApiApi.md#api_loss_infrastructure_read) | **GET** /api/{version}/loss-infrastructure/{id}/ | 
*ApiApi* | [**api_loss_list**](docs/ApiApi.md#api_loss_list) | **GET** /api/{version}/loss/ | 
*ApiApi* | [**api_loss_livestock_list**](docs/ApiApi.md#api_loss_livestock_list) | **GET** /api/{version}/loss-livestock/ | 
*ApiApi* | [**api_loss_livestock_read**](docs/ApiApi.md#api_loss_livestock_read) | **GET** /api/{version}/loss-livestock/{id}/ | 
*ApiApi* | [**api_loss_people_list**](docs/ApiApi.md#api_loss_people_list) | **GET** /api/{version}/loss-people/ | 
*ApiApi* | [**api_loss_people_read**](docs/ApiApi.md#api_loss_people_read) | **GET** /api/{version}/loss-people/{id}/ | 
*ApiApi* | [**api_loss_read**](docs/ApiApi.md#api_loss_read) | **GET** /api/{version}/loss/{id}/ | 
*ApiApi* | [**api_manual_list**](docs/ApiApi.md#api_manual_list) | **GET** /api/{version}/manual/ | 
*ApiApi* | [**api_manual_read**](docs/ApiApi.md#api_manual_read) | **GET** /api/{version}/manual/{id}/ | 
*ApiApi* | [**api_metadata_list**](docs/ApiApi.md#api_metadata_list) | **GET** /api/{version}/metadata/ | 
*ApiApi* | [**api_metadata_read**](docs/ApiApi.md#api_metadata_read) | **GET** /api/{version}/metadata/{id}/ | 
*ApiApi* | [**api_municipality_contact_list**](docs/ApiApi.md#api_municipality_contact_list) | **GET** /api/{version}/municipality-contact/ | 
*ApiApi* | [**api_municipality_contact_read**](docs/ApiApi.md#api_municipality_contact_read) | **GET** /api/{version}/municipality-contact/{id}/ | 
*ApiApi* | [**api_municipality_covid19_info_list**](docs/ApiApi.md#api_municipality_covid19_info_list) | **GET** /api/{version}/municipality-covid19-info/ | 
*ApiApi* | [**api_municipality_covid19_info_read**](docs/ApiApi.md#api_municipality_covid19_info_read) | **GET** /api/{version}/municipality-covid19-info/{id}/ | 
*ApiApi* | [**api_municipality_list**](docs/ApiApi.md#api_municipality_list) | **GET** /api/{version}/municipality/ | 
*ApiApi* | [**api_municipality_read**](docs/ApiApi.md#api_municipality_read) | **GET** /api/{version}/municipality/{id}/ | 
*ApiApi* | [**api_nap_precipitation_list**](docs/ApiApi.md#api_nap_precipitation_list) | **GET** /api/{version}/nap-precipitation/ | 
*ApiApi* | [**api_nap_precipitation_read**](docs/ApiApi.md#api_nap_precipitation_read) | **GET** /api/{version}/nap-precipitation/{id}/ | 
*ApiApi* | [**api_nap_temperature_list**](docs/ApiApi.md#api_nap_temperature_list) | **GET** /api/{version}/nap-temperature/ | 
*ApiApi* | [**api_nap_temperature_read**](docs/ApiApi.md#api_nap_temperature_read) | **GET** /api/{version}/nap-temperature/{id}/ | 
*ApiApi* | [**api_organization_list**](docs/ApiApi.md#api_organization_list) | **GET** /api/{version}/organization/ | 
*ApiApi* | [**api_organization_read**](docs/ApiApi.md#api_organization_read) | **GET** /api/{version}/organization/{id}/ | 
*ApiApi* | [**api_pollution_list**](docs/ApiApi.md#api_pollution_list) | **GET** /api/{version}/pollution/ | 
*ApiApi* | [**api_pollution_read**](docs/ApiApi.md#api_pollution_read) | **GET** /api/{version}/pollution/{id}/ | 
*ApiApi* | [**api_project_list**](docs/ApiApi.md#api_project_list) | **GET** /api/{version}/project/ | 
*ApiApi* | [**api_project_read**](docs/ApiApi.md#api_project_read) | **GET** /api/{version}/project/{id}/ | 
*ApiApi* | [**api_province_list**](docs/ApiApi.md#api_province_list) | **GET** /api/{version}/province/ | 
*ApiApi* | [**api_province_read**](docs/ApiApi.md#api_province_read) | **GET** /api/{version}/province/{id}/ | 
*ApiApi* | [**api_rain_list**](docs/ApiApi.md#api_rain_list) | **GET** /api/{version}/rain/ | 
*ApiApi* | [**api_rain_read**](docs/ApiApi.md#api_rain_read) | **GET** /api/{version}/rain/{id}/ | 
*ApiApi* | [**api_reconstruction_list**](docs/ApiApi.md#api_reconstruction_list) | **GET** /api/{version}/reconstruction/ | 
*ApiApi* | [**api_reconstruction_read**](docs/ApiApi.md#api_reconstruction_read) | **GET** /api/{version}/reconstruction/{id}/ | 
*ApiApi* | [**api_relief_release_status_list**](docs/ApiApi.md#api_relief_release_status_list) | **GET** /api/{version}/relief-release-status/ | 
*ApiApi* | [**api_relief_release_status_read**](docs/ApiApi.md#api_relief_release_status_read) | **GET** /api/{version}/relief-release-status/{id}/ | 
*ApiApi* | [**api_resource_list**](docs/ApiApi.md#api_resource_list) | **GET** /api/{version}/resource/ | 
*ApiApi* | [**api_resource_profile_list**](docs/ApiApi.md#api_resource_profile_list) | **GET** /api/{version}/resource-profile/ | 
*ApiApi* | [**api_resource_profile_read**](docs/ApiApi.md#api_resource_profile_read) | **GET** /api/{version}/resource-profile/{id}/ | 
*ApiApi* | [**api_resource_read**](docs/ApiApi.md#api_resource_read) | **GET** /api/{version}/resource/{id}/ | 
*ApiApi* | [**api_river_list**](docs/ApiApi.md#api_river_list) | **GET** /api/{version}/river/ | 
*ApiApi* | [**api_river_read**](docs/ApiApi.md#api_river_read) | **GET** /api/{version}/river/{id}/ | 
*ApiApi* | [**api_situation_report_list**](docs/ApiApi.md#api_situation_report_list) | **GET** /api/{version}/situation-report/ | 
*ApiApi* | [**api_situation_report_read**](docs/ApiApi.md#api_situation_report_read) | **GET** /api/{version}/situation-report/{id}/ | 
*ApiApi* | [**api_streamflow_list**](docs/ApiApi.md#api_streamflow_list) | **GET** /api/{version}/streamflow/ | 
*ApiApi* | [**api_streamflow_read**](docs/ApiApi.md#api_streamflow_read) | **GET** /api/{version}/streamflow/{id}/ | 
*ApiApi* | [**api_token_create**](docs/ApiApi.md#api_token_create) | **POST** /api/{version}/token/ | 
*ApiApi* | [**api_token_refresh_create**](docs/ApiApi.md#api_token_refresh_create) | **POST** /api/{version}/token/refresh/ | 
*ApiApi* | [**api_token_verify_create**](docs/ApiApi.md#api_token_verify_create) | **POST** /api/{version}/token/verify/ | 
*ApiApi* | [**api_v1_auth_login_create**](docs/ApiApi.md#api_v1_auth_login_create) | **POST** /api/v1/auth/login/ | 
*ApiApi* | [**api_v1_geolookup_list**](docs/ApiApi.md#api_v1_geolookup_list) | **GET** /api/v1/geolookup/ | 
*ApiApi* | [**api_vulnerability_list**](docs/ApiApi.md#api_vulnerability_list) | **GET** /api/{version}/vulnerability/ | 
*ApiApi* | [**api_vulnerability_read**](docs/ApiApi.md#api_vulnerability_read) | **GET** /api/{version}/vulnerability/{id}/ | 
*ApiApi* | [**api_ward_list**](docs/ApiApi.md#api_ward_list) | **GET** /api/{version}/ward/ | 
*ApiApi* | [**api_ward_read**](docs/ApiApi.md#api_ward_read) | **GET** /api/{version}/ward/{id}/ | 
*ApiApi* | [**api_weather_list**](docs/ApiApi.md#api_weather_list) | **GET** /api/{version}/weather/ | 
*ApiApi* | [**api_weather_read**](docs/ApiApi.md#api_weather_read) | **GET** /api/{version}/weather/{id}/ | 


## Documentation For Models

 - [Agriculture](docs/Agriculture.md)
 - [AgricultureType](docs/AgricultureType.md)
 - [Alert](docs/Alert.md)
 - [Case](docs/Case.md)
 - [Category](docs/Category.md)
 - [CitizenReport](docs/CitizenReport.md)
 - [Contact](docs/Contact.md)
 - [Country](docs/Country.md)
 - [Demographic](docs/Demographic.md)
 - [DetailResource](docs/DetailResource.md)
 - [DisabilityType](docs/DisabilityType.md)
 - [District](docs/District.md)
 - [Document](docs/Document.md)
 - [DocumentCategory](docs/DocumentCategory.md)
 - [Earthquake](docs/Earthquake.md)
 - [EarthquakeRiskScore](docs/EarthquakeRiskScore.md)
 - [Event](docs/Event.md)
 - [Family](docs/Family.md)
 - [Fire](docs/Fire.md)
 - [FiscalYear](docs/FiscalYear.md)
 - [Hazard](docs/Hazard.md)
 - [Immigrant](docs/Immigrant.md)
 - [ImmigrantByCountry](docs/ImmigrantByCountry.md)
 - [ImmigrantByDistrict](docs/ImmigrantByDistrict.md)
 - [ImmigrantVerified](docs/ImmigrantVerified.md)
 - [Incident](docs/Incident.md)
 - [IncidentFeedback](docs/IncidentFeedback.md)
 - [Infrastructure](docs/Infrastructure.md)
 - [InfrastructureType](docs/InfrastructureType.md)
 - [InfrastructureUnit](docs/InfrastructureUnit.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse20023](docs/InlineResponse20023.md)
 - [InlineResponse20024](docs/InlineResponse20024.md)
 - [InlineResponse20025](docs/InlineResponse20025.md)
 - [InlineResponse20026](docs/InlineResponse20026.md)
 - [InlineResponse20027](docs/InlineResponse20027.md)
 - [InlineResponse20028](docs/InlineResponse20028.md)
 - [InlineResponse20029](docs/InlineResponse20029.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse20030](docs/InlineResponse20030.md)
 - [InlineResponse20031](docs/InlineResponse20031.md)
 - [InlineResponse20032](docs/InlineResponse20032.md)
 - [InlineResponse20033](docs/InlineResponse20033.md)
 - [InlineResponse20034](docs/InlineResponse20034.md)
 - [InlineResponse20035](docs/InlineResponse20035.md)
 - [InlineResponse20036](docs/InlineResponse20036.md)
 - [InlineResponse20037](docs/InlineResponse20037.md)
 - [InlineResponse20038](docs/InlineResponse20038.md)
 - [InlineResponse20039](docs/InlineResponse20039.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse20040](docs/InlineResponse20040.md)
 - [InlineResponse20041](docs/InlineResponse20041.md)
 - [InlineResponse20042](docs/InlineResponse20042.md)
 - [InlineResponse20043](docs/InlineResponse20043.md)
 - [InlineResponse20044](docs/InlineResponse20044.md)
 - [InlineResponse20045](docs/InlineResponse20045.md)
 - [InlineResponse20046](docs/InlineResponse20046.md)
 - [InlineResponse20047](docs/InlineResponse20047.md)
 - [InlineResponse20048](docs/InlineResponse20048.md)
 - [InlineResponse20049](docs/InlineResponse20049.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse20050](docs/InlineResponse20050.md)
 - [InlineResponse20051](docs/InlineResponse20051.md)
 - [InlineResponse20052](docs/InlineResponse20052.md)
 - [InlineResponse20053](docs/InlineResponse20053.md)
 - [InlineResponse20054](docs/InlineResponse20054.md)
 - [InlineResponse20055](docs/InlineResponse20055.md)
 - [InlineResponse20056](docs/InlineResponse20056.md)
 - [InlineResponse20057](docs/InlineResponse20057.md)
 - [InlineResponse20058](docs/InlineResponse20058.md)
 - [InlineResponse20059](docs/InlineResponse20059.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse20060](docs/InlineResponse20060.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [Inventory](docs/Inventory.md)
 - [Item](docs/Item.md)
 - [Layer](docs/Layer.md)
 - [LayerGroup](docs/LayerGroup.md)
 - [Livestock](docs/Livestock.md)
 - [LivestockType](docs/LivestockType.md)
 - [Loss](docs/Loss.md)
 - [Manual](docs/Manual.md)
 - [Metadata](docs/Metadata.md)
 - [Municipality](docs/Municipality.md)
 - [MunicipalityCovid19Info](docs/MunicipalityCovid19Info.md)
 - [NationalInfo](docs/NationalInfo.md)
 - [Organization](docs/Organization.md)
 - [People](docs/People.md)
 - [Pollution](docs/Pollution.md)
 - [Precipitation](docs/Precipitation.md)
 - [Project](docs/Project.md)
 - [Province](docs/Province.md)
 - [QuarantineInfo](docs/QuarantineInfo.md)
 - [Rain](docs/Rain.md)
 - [Reconstruction](docs/Reconstruction.md)
 - [ReleaseStatus](docs/ReleaseStatus.md)
 - [Resource](docs/Resource.md)
 - [River](docs/River.md)
 - [SituationReport](docs/SituationReport.md)
 - [StreamFlow](docs/StreamFlow.md)
 - [Temperature](docs/Temperature.md)
 - [TokenObtainPair](docs/TokenObtainPair.md)
 - [TokenRefresh](docs/TokenRefresh.md)
 - [TokenVerify](docs/TokenVerify.md)
 - [Training](docs/Training.md)
 - [Transit](docs/Transit.md)
 - [TravelHistory](docs/TravelHistory.md)
 - [Vulnerability](docs/Vulnerability.md)
 - [Ward](docs/Ward.md)
 - [Weather](docs/Weather.md)


## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication


## Author


