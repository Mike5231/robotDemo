*** Settings ***
Library     ../libraries/jobs.py

*** Variables ***
${job_id}       db195424-9088-4fd4-a9ba-1a4fc1053dcd

*** Test Cases ***
Get_job
    ${response}     get job    ${job_id}
    Log     ${response.data}
    Log     ${response.status_code}
    ${status_code}  Set Variable  ${response.status_code}
    ${job_number}  Set Variable  ${response.data['job_number']}
    Should Be Equal As Numbers  200  ${status_code}
    Should Be Equal As Strings  3435862  ${job_number}

Get_job_2
    ${response}     get job    ${job_id}
    ${status_code}  Set Variable  ${response.status_code}
    ${job_number}  Set Variable  ${response.data['job_number']}
    Should Be Equal As Numbers  200  ${status_code}
    Should Be Equal As Strings  3435862  ${job_number}
