#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    country_name= ["United Kingdom","Finland", "USA", "Sweden", "Germany", "Russia"]
    independance= [np.nan, 1917, 1776, 1523, np.nan, 1992 ]
    president=[None, "Niinistö", "Trump",None, "Steinmeier", "Putin"]
    countys= pd.DataFrame({"Year of independence": independance, "President": president}, index= country_name)
    return countys 
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
