# **About the Bank Spyders project**

## I created this as a basis for creating a more specialized **_sub-spyder_** for projects-to-come

## Each of these projects aim to do the following

- to **_scrape_** the daily exchange rates of a certain bank and save the results (to a database to-be defined in the future)
- to **_graph_** the scraping results in an informative way towards the [end-goal](https://addendgoalheaderhere) of the project.
- to **_email_** results that satisfy a certain criteria, defined by the [end-goal](https://addendgoalheaderhere) of the project.

## The End-goal(s) of all of these projects

- To find a connection between the results and current real-world events.

  - current real-world events is an ambiguous definition that needs to be better explained later, once enough data has been collected.

- To find a connection / link between the banks.

  - this can be found be overlaying the graphs of multiple banks over eachother, for example.

- To find a way to predict the fall or rise of prices given certain data (e.g Stock prices of some company, Tension between two major powers, etc..)
  - Using my currently non-existent machine-learning / deep-learning skills, I will attempt to predict prices according to the criteria of the previous two conditions.

---

## **Details about each file:**

- ### **_[BankSpyder.py](https://github.com/aziznal/bank_spyders/blob/master/BankSpyder.py)_**

  Main Class that subspyders will inherit from. has all the basic bellsand whistles to make programming a subspyder more straight-forward

  - **_load_settings(file_path)_**

    Loads the **_spyder_settings.json_** file by default. If otherwise given a filepath, it loads that instead.

  - **_save_settings()_**

    Saves any edits in **_spyder_settings.json_**. Or, if a different file was used, it saves there instead.

    Note: ResultGrapher will need results formatted in the pre-defined structure found [here](https://add_result_example.json_here).

- ### **_[ResultGrapher.py](<[https://](https://github.com/aziznal/bank_spyders/blob/master/ResultGrapher.py)>)_**

  Graphs the results collected by the subspyder

  - **_constructor( results_folder_path, time_interval, selected_currency )_**

    - **_results_folder_path_**: default is '**_results/_** '
    - **_time_interval_**: 'today' | 'more_options_in_the_future'
    - **_selected_currency_**: default is **_'USD'_**. can be any code from the results.

    - **_\_\_set_axes( )_**

    Loads data from results and assigns it to each axis in the grapher object.

  - **_\_\_compare_filenames( file1, file2 )_**

    Helper method for **_\_\_sort_files( \_list )_**

  - **_\_\_sort_files( \_list )_**

    This method organizes a given list of files numerically, using bubblesort.

  - **_\_\_check_axes( )_**
    Tests that all axes have the same length. otherwise raises **_AssertionError_**

  - **_\_\_format_timestamps( )_**

    formats the timestamps loaded from the result files in way that's suitable to show on the graph axes. returns __*day*__ and **_starting_date_** which are used in the graph **_title_**

  - **_\_\_format_x_ticks( plot )_**

    Changes the way the x-axis labels look. see method docs for more.

    - **_plot_**: current active plot.

  - **_\_\_annotate_plot( plot, current_index, y, x, color, bottom_offset)_**

    Draws each point's value on top of the point.

    - **_All parameters are self-explanatory or can be found in method docs_**

  - **_\_\_format_rates_plot( plot )_**

    Manages the Look and Format of the rates plot

  - **_\_\_format_ratios_plot( plot )_**

    Manages the Look and Format of the rates plot

  - **_create_graph( show, save )_**

    Method that creates the graph(s).

  - **_show & save:_** booleans that decide whether a graph is shown at the end of this method, or whether the graph is saved as a .png at the end of the method, respectively.

- ### **_[functions.py](https://github.com/aziznal/bank_spyders/blob/master/functions.py)_**

  Includes general helper functions for spyders.

  - **_get_current_time():_**

    Returns a dict object with keys 'hour' and 'minutes'

  - **_set_new_interval_( starting_hour, ending_hour, required_frequency ):**

    returns the proper interval to wait between each iteration of data collecting such that the
    required frequency of data points will be reached.

  - **_save_scraped_data( spyder, results ):_**

    Saves results to a file named by the spyder according to the current session's date.

    This function creates the destination folder if it does not exist.

  - **_numth(number):_**

    Takes in 'n', returns 'n _th_'

    e.g:

        1  -> "1st"
        2  -> "2nd"
        45 -> "45th"

- ### **_[init_script.py](https://github.com/aziznal/bank_spyders/blob/master/init_script.py)_**

  Creates project settings, exec.bat, and makes sure all the essential directories are present.

  Run this script to initialize project_settings.json, and create the exec.bat file to assign to an automatic process later.

  This script is made to be customized for every different spyder as needed.
