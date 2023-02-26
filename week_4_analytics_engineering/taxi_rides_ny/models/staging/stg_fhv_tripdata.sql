{{ config(materialized='view') }}

with tripdata as 
(
  select *
    --row_number() over(partition by dispatching_base_num, pickup_datetime) as rn
  from {{ source('staging','fhv_tripdata') }}
  where dispatching_base_num is not null 
)
select
    -- identifiers
    {{ dbt_utils.surrogate_key(['dispatching_base_num', 'pickup_datetime']) }} as tripid,
    cast(dispatching_base_num as string) as dispatching_base_num,
    cast(PUlocationID as integer) as  pickup_locationid,
    cast(DOlocationID as integer) as dropoff_locationid,
    cast(SR_Flag as string) as SR_Flag,
    cast(Affiliated_base_number as string) as Affiliated_base_number,

    -- timestamps
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropOff_datetime as timestamp) as dropoff_datetime

from tripdata
--where rn = 1


-- dbt build --m <model.sql> --var 'is_test_run: false'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}
