from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
import selenium
from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

__version__ = '1.0'

class DebuggingLibrary:

    """ Library for remote chrome browser
     """
    
    def __init__(self, *args, **kwargs):
        pass
    
    @property
    def selenium(self):
        return BuiltIn().get_library_instance('SeleniumLibrary')

    @keyword(name='Debug::Execute On Opened Browser')
    def execute_on_opened_browser(self, port='9014'):
        """
        usage:
        chrome.exe --remote-debugging-port=9014 --user-data-dir="C:\testChrome"
        
        - set chrome location as environment variable.
        - 9014 is port, you can change any port you want.
        - C:\\testChrome location can change to any folder you want to set chrome data. 

        """
        options = webdriver.ChromeOptions()
        address = "127.0.0.1:" + str(port)
        options.add_experimental_option("debuggerAddress", address)
        self.selenium.create_webdriver('Chrome', desired_capabilities=options.to_capabilities())
        