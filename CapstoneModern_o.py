#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:36:03 2024

@author: brendandervan
Data Science time woo-hoo!
"""

import matplotlib.pyplot as plt
import pandas as pd
import modern_o_frame


boston_data = modern_o_frame.get_data()

def graph_boston(data):
    
    modern_f1 = []
    modern_f2 = []
    
    for i in range(len(data.loc[:, 'year'])):
        
        modern_f1.append(data.loc[i, 'F1'])
        modern_f2.append(data.loc[i, 'F2'])
    
    
    fig, ax = plt.subplots()
    plt.title('Formants for "ɑ"')
    plt.xlabel('Formant 2')
    plt.ylabel('Formant 1')
    plt.xlim((900, 2200))
    plt.ylim((400, 1100))
    
    plt.scatter(modern_f2, modern_f1, marker='x', color='blue', label='2020s')
    ax.invert_xaxis()
    ax.invert_yaxis()
    
    plt.legend()
    plt.savefig('modern_boston_formants.png')
    
    
    plt.show()
    
formant1 = list(boston_data.F1)   
    
    
    
def main():
    
    print('this is testing the main function')
    print(boston_data)
    
    graph_boston(boston_data)
    
    boston_years = list(boston_data.year)
    print(boston_years)


main()