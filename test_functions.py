import os
from datetime import datetime
import sys
from time import sleep


from functions import sameline_print


def get_current_time():
    """Returns a dict with keys ['hour'] and ['minutes'] with int values"""
    current_time = datetime.now().strftime("%H-%M").split('-')

    return {
        'hour': int(current_time[0]),
        'minutes': int(current_time[1])
    }


def get_current_day():
    """
    Returns nonabbreviated lowercase current day. e.g. saturday | monday
    """
    current_day = datetime.now().strftime('%A').lower()
    return current_day


def banks_are_closed_day_test():
    return True


def increment_current_time(current_time):
    m_current_time = current_time.copy()

    m_current_time['minute'] = str(int(m_current_time['minute']) + 1)

    # If "01" was transformed into "2", transform it back to "02"
    if len(m_current_time['minute']) == 1:
        m_current_time['minute'] = f"0{m_current_time['minute']}"

    return m_current_time

def banks_are_closed_time_test():

    current_time = get_current_time()
    next_time = increment_current_time(current_time)

    conditions = [
        current_time['hour'] > next_time
    ]


def banks_are_closed():
    """This is a mock function with different conditions to make testing easier"""
    current_time = get_current_time()['hour']
    current_day = get_current_day()

    conditions = [
        current_day == 'saturday',
        current_day == 'sunday',
        current_time < 9,
        current_time > 18
    ]

    return any(conditions)


def banks_are_open():
    """This is a mock function with different conditions to make testing easier"""
    today = get_current_day()
    current_time = get_current_time()

    conditions = [
        today != 'saturday',
        today != 'sunday',
        current_time['hour'] < 18,
        current_time['hour'] >= 9
    ]

    return all(conditions)


def sleep_until_banks_open():
    today = get_current_day()
    current_time = get_current_time()

    while banks_are_closed():

        sameline_print('Waiting for banks to open..')
        sleep(1)

    return


def create_intervals(start_, finish_, wait_between):

    """
    Create intervals from start_ to finish_ with wait_between seconds between each interval

    :Parameters:

    :param start_ (str): string in the form "09:00" in 24hr format
    :param finish_ (str): string in the form "18:00" in 24hr format
    :param wait_between (int): amount to wait between intervals in Seconds

    :returns: (List) Intervals
    """

    # TODO: implement
    intervals = []

