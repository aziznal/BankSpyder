# **About the Bank Spyders project**

## I created this as a basis for creating a more specialized ***sub-spyder*** for projects-to-come.

## Each of these projects have the following aim:
* ### to ***scrape*** the daily exchange rates of a certain bank and save the results (to a database to-be defined in the future)
* ### to ***graph*** the scraping results in an informative way towards the [end-goal](https://addendgoalheaderhere) of the project.
* ### to ***email*** results that satisfy a certain criteria, defined by the [end-goal](https://addendgoalheaderhere) of the project.

## The End-goal(s) of all of these projects:

* ### To find a connection between the results and current real-world events.
  * #### current real-world events is an ambiguous definition that needs to be better explained later, once enough data has been collected.

* ### To find a connection / link between the banks.
  * #### this can be found be overlaying the graphs of multiple banks over eachother, for example.

* ### To find a way to predict the fall or rise of prices given certain data (e.g Stock prices of some company, Tension between two major powers, etc..)
  * #### Using my currently non-existent machine-learning / deep-learning skills, I will attempt to predict prices according to the criteria of the previous two conditions.

---

## **Details about each file**:

* ### ***[BankSpyder.py](https://github.com/aziznal/bank_spyders/blob/master/BankSpyder.py)***
    #### Main Class that subspyders will inherit from. has all the basic bells and whistles to make programming a subspyder more straight-forward.

    * ***load_settings(file_path)***
        
        Loads the ***spyder_settings.json*** file by default. If otherwise given a filepath, it loads that instead.

    * ***save_settings()***

        Saves any edits in ***spyder_settings.json***. Or, if a different file was used, it saves there instead.

    #### Note: ResultGrapher will need results formatted in the pre-defined structure found [here](https://add_result_example.json_here).

* ### ***[ResultGrapher.py]([https://](https://github.com/aziznal/bank_spyders/blob/master/ResultGrapher.py))***
    #### Graphs the results collected by the subspyder.

    * ***constructor( results_folder_path, time_interval, selected_currency )***
      * ***results_folder_path***: default is ' ***results/*** '
      * ***time_interval***: 'today' | 'more_options_in_the_future'
      * ***selected_currency***: default is ***'USD'***. can be any code from the results.

    * ***__set_axes( )***

        Loads data from results and assigns it to each axis in the grapher object.

    * ***__compare_filenames( file1, file2 )***

        Helper method for ***__sort_files( _list )***
    
    * ***__sort_files( _list )***

        This method organizes a given list of files numerically, using bubblesort.

    * ***__check_axes( )***
      Tests that all axes have the same length. otherwise raises ***AssertionError***

    * ***__format_timestamps( )***

        formats the timestamps loaded from the result files in way that's suitable to show on the graph axes. returns ***day*** and ***starting_date*** which are used in the graph ***title***

    * ***__format_x_ticks( plot )***

        Changes the way the x-axis labels look. see method docs for more.

      * ***plot***: current active plot.

    * ***__annotate_plot( plot, current_index, y, x, color, bottom_offset)***
        
        Draws each point's value on top of the point.
        * ***All parameters are self-explanatory or can be found in method docs***
    
    * ***__format_rates_plot( plot )***

        Manages the Look and Format of the rates plot

    * ***__format_ratios_plot( plot )***

        Manages the Look and Format of the rates plot

    * ***create_graph( show, save )***

        Method that creates the graph(s).
    
      * ***show & save:*** booleans that decide whether a graph is shown at the end of this method, or whether the graph is saved as a .png at the end of the method, respectively.
    