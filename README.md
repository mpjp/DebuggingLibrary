# DebuggingLibrary
Library for remote chrome browser

Introduction
------------
This keyword library is based on [Robot Framework](https://robotframework.org/). In my experience in developing automation test cases, every time we want to check the specific action, we may run the whole test script but it also wastes a lot of time.

So this library provides a keyword `Debug::Execute On Opened Browser` that can run the test scripts on the same browser.

Installation
----------
* Using pip
  
      pip install mpjp-debuggingLibrary
* Open remote chrome browser
  * Setting the location of chrome browser as environmental variables
  * Create an empty folder at **C:\testChrome**
  * Input the command below
   
        chrome.exe --remote-debugging-port=9014 --user-data-dir="C:\testChrome"
    > **9014** is port, you can change any port you want.
        - **C:\\testChrome** location can change to any folder you want to set chrome data. 
    
    The clean chrome browser should be opened.

Usage
-----
Todo