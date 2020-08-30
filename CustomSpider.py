from BankSpider import BankSpider
from CustomExceptions import *


class CustomSpider(BankSpider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_rates_list(self):
        pass

    def _extract_values(self, rates_list):
        pass

    def _get_usd_value(self, values):
        pass

    def get_single_reading(self):
        
        rates_list = self._get_rates_list()

        extracted_values = self._extract_values(rates_list)

        usd_value = self._get_usd_value(extracted_values)

        return usd_value
