from time import sleep
import json
import traceback

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from functions import *
from custom_functions import *
from CustomExceptions import *


def run_script(spyder):

    interval = 3   # This will gather ~1000 rows of data in 9hrs
    current_loop = 0

    make_ascii_spyder()

    print(f"New data will be collected every {interval} seconds")
    print(f"Around {(9 * 60 * 60)//30} data points will be gathered")

    while banks_are_open():
        
        sameline_print(f"@datapoint {current_loop + 1}")
        current_loop += 1

        try:
            scrape(spyder, interval)

        except WebDriverException as e:
            print(f"\nEncountered Exception during Data Getting Stage: {e}")
            raise StalledSpyderException()


crash_limit = 2
load_project_settings()

while crash_limit > 0:
    
    try:

        
        if banks_are_closed():
            sleep_until_banks_open()

        spyder = make_spyder()
        run_script(spyder)

    # REFACTOR
    except Exception as e:
        print(f"\nEncountered exception while running script: {e}")
        traceback.print_exc()

        crash_limit -= 1

        print("*" * 50)
        print(f"\n\nScript has {crash_limit} more lives")
        print("*" * 50)

    # REFACTOR
    except KeyboardInterrupt as e:
        print(f"\nEncountered exception while running script: {e}")
        traceback.print_exc()

        crash_limit -= 1

        print("\n\n" + "*" * 50)
        print(f"Script has {crash_limit} more lives")
        print("*" * 50)
        print("\n\n")

    finally:

        try:
            spyder.die()

        except Exception as e:
            print("Ran into exception while destroying spyder.\nSpyder probably wasn't created yet")

        print("\n\nScript seems to have crashed")
        print("Attempting to start again..\n\n")

    continue


print("\nScript ran out of lives\n")

input("\n\nProgram execution has finished. Press Enter to exit")