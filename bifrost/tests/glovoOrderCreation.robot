*** Settings ***
Library     customLibrary.py
Library     RequestsLibrary

*** Variables ***
${base_url}     https://channels.xandar.instaleap.io
${job_id}       db195424-9088-4fd4-a9ba-1a4fc1053dcd

*** Test Cases ***
Get_av2
    [Setup] Create slots    fleet_id    resource_id
    create session  myssion  ${base_url}
    ${response}  GET On Session  myssion  /
    Should Be Equal As Strings  Tesseract  ${response.json()}[module]
    ${job_info}  get job info  ${job_id}
    Should Be Equal As Strings  34358622  ${job_info.json()}[job_number]
