from intel_engine.url_extractor import chromedriver_location
from intel_engine.url_extractor import chrome_options
from intel_engine.url_extractor import webdriver
from contextlib import contextmanager

@contextmanager
def hideUnhideCursor():
    """Hide and unhide the cursor."""
    print('\033[? 25l', end='') #hide cursor
    try:
        yield None
    finally:
        print('\033[? 25h', end='') #unhide cursor

@contextmanager
def seleniumCxtmanager():
    """Setup and Teardown ops on selenium driver."""
    driver = webdriver.Chrome(executable_path=chromedriver_location, options=chrome_options)
    try:
        yield driver
    finally:
        driver.close()
        driver.quit()

@contextmanager
def printNewLineAfter():
    """Print a new line after something."""
    try:
        yield None
    finally:
        print()
