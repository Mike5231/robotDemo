*** Settings ***
Library     ../libraries/customLibrary.py

*** Variables ***
${base_url}     https://channels.xandar.instaleap.io
${job_id}       db195424-9088-4fd4-a9ba-1a4fc1053dcd

*** Test Cases ***
Get_health
    ${job_info}  get job info  ${job_id}
    Should Be Equal As Strings  3435862  ${job_info.json()}[job_number]

Get_health_2
    ${job_info}  get job info  ${job_id}
    Should Be Equal As Strings  34358621  ${job_info.json()}[job_number]
