from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import requests

user_agent=''

def get_chrome_user_agent() -> str:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # headless
    driver = webdriver.Chrome(options=options)
    
    user_agent = driver.execute_script("return navigator.userAgent;")  # run JavaScript code
    driver.quit()
    return user_agent

def get_edge_user_agent() -> str:
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")  # headless
    driver = webdriver.Edge(options=options)
    
    user_agent = driver.execute_script("return navigator.userAgent;")  # run JavaScript code
    driver.quit()
    return user_agent

def get_safari_user_agent() -> str:
    options = webdriver.SafariOptions()
    options.add_argument("--headless")  # headless
    driver = webdriver.Safari(options=options)
    
    user_agent = driver.execute_script("return navigator.userAgent;")  # run JavaScript code
    driver.quit()
    return user_agent

def get_auto_user_agent() -> str:
    global user_agent

    if not user_agent:
        for fn in [get_chrome_user_agent, get_edge_user_agent, get_safari_user_agent]:
            try:
                user_agent = fn()
                break
            except WebDriverException:
                continue
        if not user_agent:
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/134.0.0.0 Safari/537.36'

    return user_agent

def get(url: str, referer='', content_type='', user_agent_input='') -> requests.models.Response:
    global user_agent
    
    if not user_agent:
        if not user_agent_input:
            user_agent = get_auto_user_agent()
        else:
            user_agent = user_agent_input
    
    header = {'User-Agent': user_agent}
    
    if referer:
        header.update({'Referer': referer})
    if content_type:
        header.update({'Content-Type': content_type})
        
    response = requests.get(url, headers=header)
    return response