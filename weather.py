#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:23:48 2022

@author: camilasury
"""

#### Import package
from wwo_hist import retrieve_hist_data


#### Set working directory to store output csv file(s)

import os
os.chdir("/Users/camilasury/Desktop/Herramientas computacionales/Python Scrappinng /Output/weather")


#### Example code
frequency=24
start_date = '01-JAN-2015'
end_date = '31-DEC-2015'
api_key = 'f3bbf164c66342a492b125413221107'
location_list = ["20637","20653","20688","20724","20742","20871","21040","21043","21158","21220","21240","21502","21550","21601","21638","21639","21643","21651","21701","21742","21804","21811","21853","21902"]
# En stata faltaba Garret county, lo rellenamos con el zipcode de Oakland, la cede del condado: 21550. 
hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)
