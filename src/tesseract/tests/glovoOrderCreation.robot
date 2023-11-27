*** Settings ***
Library     ../../bifrost/libraries/jobs.py

*** Variables ***
${job_id}       db195424-9088-4fd4-a9ba-1a4fc1053dcd
${job_requests}    JobRequests

*** Test Cases ***
Get_health
    ${job_info}     ${job_requests}.get_job    ${job_id}
    Log     ${job_info.data}
    ${job_number}  Set Variable  ${job_info.data['job_number']}
    Should Be Equal As Strings  3435862  ${job_number}

Get_health_2
    ${job_info}  ${job_requests}.get_job  ${job_id}
    ${job_number}  Set Variable  ${job_info.data['job_number']}
    Should Be Equal As Strings  3435862  ${job_number}
