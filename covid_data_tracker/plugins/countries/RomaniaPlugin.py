import requests
import tabula
from bs4 import BeautifulSoup
import pandas as pd
from googletrans import Translator

from covid_data_tracker.plugins.base import BasePlugin

class RomaniaPlugin(BasePlugin):

    COUNTRY = "Romania"
    BASE_SOURCE = "https://www.cnscbt.ro/index.php/analiza-cazuri-confirmate-covid19/1761-raport-saptamanal-episaptamana20/file"
    TYPE = "PDF"

    def fetch(self):
        df = tabula.read_pdf(BASE_SOURCE)

        print (df)

        # self.sex_table['absolute_cases']['total'] = 30
        # self.sex_table['absolute_cases']['male'] = 30
        # self.sex_table['absolute_cases']['female'] = 30
        #
        # self.sex_table['percent_cases']['female'] = .3
        #
        # self.sex_table['absolute_deaths']['total'] = 10
        # self.sex_table['absolute_deaths']['male'] = 3
        # self.sex_table['absolute_deaths']['female'] = 10
