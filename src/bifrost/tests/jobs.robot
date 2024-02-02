*** Settings ***
Library     ../libraries/jobs.py    WITH NAME    Jobs
Library     ../data/jobsMock.py
Resource     ../useCases/jobs.resource

*** Variables ***
${job_id}   cf22f7e0-c14f-4bd1-a5f4-6ef67c36ea4c
${job_id2}   db195424-9088-4fd4-a9ba-1a4fc1053dc4
${picker_resource}  Create Dictionary   db195424-9088-4fd4-a9ba-1a4fc1053dcd    db195424-9088-4fd4-a9ba-1a4fc1053dcd
${delivery_resource}    Create Dictionary   db195424-9088-4fd4-a9ba-1a4fc1053dcd    db195424-9088-4fd4-a9ba-1a4fc1053dcd

*** Test Cases ***
Get_job
    [Setup]    Set Job ID    ${job_id}
    ${response}     Jobs.Get Job    ${job_id}
    $payload= Dict job_id
    $response= POST /JOBS $payload
    Log        ${job_info}
    Log        ${response}
    ${status_code}  Set Variable  ${response.status_code}
    ${data}  Set Variable  ${response.text}
    ${job_number}  Set Variable  ${data["job_number"]}
    Log    ${status_code}
    Log    ${data}
    Should Be Equal As Numbers  200  ${status_code}
    Should Be Equal As Strings  856XMLSQL  ${job_number}

Get_job_2
    ${response}     Jobs.Get Job    ${job_id}
    ${status_code}  Set Variable  ${response.status_code}
    ${job_number}  Set Variable  ${response.data['job_number']}
    Should Be Equal As Numbers  200  ${status_code}
    Should Be Equal As Strings  856XMLSQL  ${job_number}

Get_availability
    ${availability}    create availability payload    currency_code=EUR
    Log    ${availability}
    ${response}    Get Availability    ${availability}
    ${status_code}  Set Variable  ${response.status_code}
    Should Be Equal As Numbers  200  ${status_code}
    
Test_setup
    [Setup]    Set Job Id    ${job_id}
    Log    ${job_info.status_code}
    Log    ${job_info.data}

Test_setup_2
    [Setup]    Set Job Id    ${job_id}
    Log    ${job_info}

Test_setup_3
    [Setup]    Set Job Id   ${job_id2}
    Log    ${job_info}
