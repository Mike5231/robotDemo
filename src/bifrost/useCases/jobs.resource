*** Settings ***
Library     ../libraries/jobs.py    WITH NAME    Jobs
Library     ../data/jobsMock.py

*** Keywords ***
Set Job Id
    [Arguments]    ${job_id}
    ${job_info}=    Jobs.Get Job    ${job_id}
    Should Be Equal As Numbers  200  ${job_info.status_code}
    Set Test Variable    ${job_info}

Set Availability Slot ID
    ${availability}=    Get Availability
    Should Be Equal As Numbers  200  ${availability.status_code}
    Set Test Variable    ${availability}
