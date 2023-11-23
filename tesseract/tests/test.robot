*** Settings ***
Resource    ../resources/http_resource.robot

*** Test Cases ***
GetTodo
    ${response}=    Get Todo    1
    Log    ${response.json()}
    Should Be Equal As Numbers    ${response.status_code}    200
    Should Be Equal As Numbers    ${response.json()['userId']}    1
    Should Be Equal As Numbers    ${response.json()['id']}    1
    Should Be Equal As Strings    ${response.json()['title']}    delectus aut autem
    Should Not Be True    ${response.json()['completed']}
