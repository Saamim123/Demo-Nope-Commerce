import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture

def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(r'C:\Users\saamim.hasmi\Desktop\Python_test_files\Drivers\chromedriver.exe')
        print('Launching chrome.....')
        serv_obj=Service(r'C:\Users\saamim.hasmi\Desktop\Python_test_files\Drivers\chromedriver.exe')
        driver=webdriver.Chrome(service=serv_obj)
    elif browser=='firefox':
        driver=webdriver.Firefox(r'C:\Users\saamim.hasmi\Desktop\Python_test_files\Drivers\geckodriver.exe')
        serv_obj = Service(r'C:\Users\saamim.hasmi\Desktop\Python_test_files\Drivers\geckodriver.exe')
        driver = webdriver.Firefox(service=serv_obj)
        print('Launching edge.....')
    else:
        driver=driver=webdriver.Chrome(r'C:\Users\saamim.hasmi\Desktop\Python_test_files\Drivers\chromedriver.exe')
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## Pytest HTML Report #######

# Hook for adding environtment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module Name']='Customer'
    config._metadata['Tester']='Saamim'

#Hook for delete /Modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)