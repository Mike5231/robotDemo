*** Settings ***s
Library     ./libraries/customLibrary.py

*** Keywords ***
Get job info-
    [Arguments]    ${job_id}
    ${job_info}=    Get Job Information    ${job_id}
    [Return]    ${job_info}
