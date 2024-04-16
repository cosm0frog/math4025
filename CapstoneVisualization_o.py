#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:37:31 2024

@author: brendandervan
Data Science time woo-hoo!

Alright, so this code will access the dataframes from Derek's code, and plot
those formant values.
"""

import matplotlib.pyplot as plt
import pandas as pd
import boston_formant


boston_data = boston_formant.make_data()

def graph_boston(data):
    
    sixties_f1 = []
    sixties_f2 = []
    seventies_f1 = []
    seventies_f2 = []
    eighties_f1 = []
    eighties_f2 = []
    nineties_f1 = []
    nineties_f2 = []
    
    for i in range(len(data.loc[:, 'year'])):
        
        if data.loc[i, 'year'] < 1970:
            
            sixties_f1.append(data.loc[i, 'F1'])
            sixties_f2.append(data.loc[i, 'F2'])
            
        elif data.loc[i, 'year'] < 1980:
            
            seventies_f1.append(data.loc[i, 'F1'])
            seventies_f2.append(data.loc[i, 'F2'])
            
        elif data.loc[i, 'year'] < 1990:
            
            eighties_f1.append(data.loc[i, 'F1'])
            eighties_f2.append(data.loc[i, 'F2'])
            
        else:
            nineties_f1.append(data.loc[i, 'F1'])
            nineties_f2.append(data.loc[i, 'F2'])
    
    
    fig, ax = plt.subplots()
    plt.title('Formants for "ɑ"')
    plt.xlabel('Formant 2')
    plt.ylabel('Formant 1')
    plt.xlim((900, 2200))
    plt.ylim((400, 1100))
    
    plt.scatter(sixties_f2, sixties_f1, marker='x', color='red', label='1960s')
    plt.scatter(seventies_f2, seventies_f1, marker='x', color='blue', label='1970s')
    plt.scatter(eighties_f2, eighties_f1, marker='x', color='fuchsia', label='1980s')
    plt.scatter(nineties_f2, nineties_f1, marker='x', color='green', label='1990s')
    ax.invert_xaxis()
    ax.invert_yaxis()
    
    plt.legend()
    plt.savefig('boston_formants.png')
    
    
    plt.show()
    
formant1 = list(boston_data.F1)   
    
    
    
def main():
    
    print('this is testing the main function')
    print(boston_data)
    
    graph_boston(boston_data)
    
    boston_years = list(boston_data.year)
    print(boston_years)
    


main()


