{{ config(materialized='view') }}

  select *
  from {{ source('staging','external_green_tripdata') }}
  where vendorid is not null 
  limit 1000


-- dbt build --m <model.sql> --var 'is_test_run: false'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}
