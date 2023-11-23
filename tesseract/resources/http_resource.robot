*** Settings ***
Library     ../libraries/http_libraries.py

*** Variables ***
${base_url}    https://jsonplaceholder.typicode.com

*** Keywords ***
Get Todo
    [Arguments]    ${todo_id}
    ${url}=    Set Variable    ${base_url}/todos/${todo_id}
    ${response}=    http_libraries.Get Request    ${url}
    [Return]    ${response}
