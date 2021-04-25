# HackMed 21 Helper Function File
# creation date: 24.04.2021 | author: Camillo Moschner (cm967)

import numpy as np
import pandas as pd
from pprint import pprint
import re
import numpy as np

import requests
from bs4 import BeautifulSoup
from pandas.io.html import read_html

# --------------------------------------------------------------------------

def find_name(s):
    pattern = "Link to (.*?) detail"
    substring_name = re.search(pattern, s).group(1)
    return substring_name

def find_status(s):
    pattern = "ng>\r\n    \r\n    \t(.*?) \t\r\n\t\r\n    </str"
    substring_name = re.search(pattern, s).group(1)
    return substring_name

def find_datalink(s):
    pattern = "ng>\r\n    \r\n    \t(.*?) \t\r\n\t\r\n    </str"
    substring_name = re.search(pattern, s).group(1)
    base_link = "https://www.accessdata.fda.gov/scripts/drugshortages/"
    return base_link+substring_name

def find_CAS_number_and_ChEBI(drug_name_wanted):
    wikipedia_link = "https://en.wikipedia.org/wiki/"
    drug_name = drug_name_wanted
    try:
        drug_name= drug_name.replace(" ", "_")
    except TypeError:
        print('wwwww')
    drug_wikipedia_link = wikipedia_link+drug_name
    print(drug_wikipedia_link)

    try:
        infoboxes = read_html(drug_wikipedia_link, index_col=0, attrs={"class":"infobox"})
        return infoboxes[0].xs(u'CAS Number').values[0], infoboxes[0].xs(u'ChEBI').values[0].split(':')[1]
    except (ValueError,KeyError):
        return 'N/A', 'N/A'


