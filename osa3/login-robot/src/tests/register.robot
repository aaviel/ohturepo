*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallek  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  salasana123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  k4113  salasana123
    Output Should Contain  Username must have only letters

Register With Valid Username And Too Short Password
    Input Credentials  kallex  x2
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallex  abcdefgh
    Output Should Contain  Password must not contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
