# **About the Bank Spyders project**

This repo is a template for creating more specialized spiders

---

## Target

Each of these projects aim to do the following

- to **_scrape_** the daily exchange rates of a certain bank and save the results (to a database to-be defined in the future)

---

## The End-goal

To find a connection (using some form of statistical analysis) between any of the banks

---

## **Details about each file:**

- ### **_[BankSpider.py](https://github.com/aziznal/bank_spyders/blob/master/BankSpider.py)_**

  Superclass for CustomSpider

- ### **_CustomSpider_**

  Write custom code for each domain you need to scrape. The get_single_reading method should return data as a tuple
  since everything is saved in a .csv

  Writing code in this file should be all you need to do for each project

- ### **_[functions.py](https://github.com/aziznal/bank_spyders/blob/master/functions.py)_**

  Includes general helper functions for spyders. Most have self-explanatory names

- ### **_[init_script.py](https://github.com/aziznal/bank_spyders/blob/master/init_script.py)_**

  Creates project settings, exec.bat, and makes sure some essential directories are present

  Run this script to initialize project_settings.json, and create the exec.bat file to assign to an automatic process later.

  Script is ready to use right out of the box. just use ' `python init_script` '

  It's also compatible with both Linux and Windows
