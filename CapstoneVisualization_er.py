#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:48:52 2024

@author: brendandervan
Data Science time woo-hoo!
"""

import matplotlib.pyplot as plt
import pandas as pd
import care_formants


care_data = care_formants.get_data()

def graph_care(data):
    
    sixties_f1f2diff = []
    sixties_f3diff = []
    sixties_years = []
    
    seventies_f1f2diff = []
    seventies_f3diff = []
    seventies_years = []
    
    eighties_f1f2diff = []
    eighties_f3diff = []
    eighties_years = []
    
    nineties_f1f2diff = []
    nineties_f3diff = []
    nineties_years = []
    
    
    for i in range(len(data.loc[:, 'year'])):
        
        if data.loc[i, 'year'] < 1970:
            
            sixties_f1f2diff.append(data.loc[i, 'F1/F2 dif'])
            sixties_f3diff.append(data.loc[i, 'F3 dif'])
            sixties_years.append(data.loc[i, 'year'])
            
        elif data.loc[i, 'year'] < 1980:
            seventies_f1f2diff.append(data.loc[i, 'F1/F2 dif'])
            seventies_f3diff.append(data.loc[i, 'F3 dif'])
            seventies_years.append(data.loc[i, 'year'])
            
        elif data.loc[i, 'year'] < 1990:
            eighties_f1f2diff.append(data.loc[i, 'F1/F2 dif'])
            eighties_f3diff.append(data.loc[i, 'F3 dif'])
            nineties_years.append(data.loc[i, 'year'])
            
        else:
            nineties_f1f2diff.append(data.loc[i, 'F1/F2 dif'])
            nineties_f3diff.append(data.loc[i, 'F3 dif'])
            nineties_years.append(data.loc[i, 'year'])
            
    fig, ax = plt.subplots()
    plt.title('Difference in F3 Over Time for "eɹ"')
    plt.xlabel('Year')
    plt.ylabel('Formant 3 Difference')
    plt.ylim((-50, 900))
    
    plt.scatter(sixties_years, sixties_f3diff, marker='x', color='red', label='1960s')
    plt.scatter(seventies_years, seventies_f3diff, marker='x', color='blue', label='1970s')
    plt.scatter(eighties_years, eighties_f3diff, marker='x', color='orange', label='1980s')
    plt.scatter(nineties_years, nineties_f3diff, marker='x', color='green', label='1990s')
    # ax.invert_xaxis()
    # ax.invert_yaxis()
    
    plt.legend()
    plt.savefig('care_formants.png')
    
    
    plt.show()
    
    plt.title('Difference in F3 and Difference Between F1 and F2 for "eɹ"')
    plt.xlabel('Difference in Formant 3')
    plt.ylabel('Difference Between Formant 1 and Formant 2')
    plt.xlim((-50, 900))
    plt.ylim((800, 1700))
    
    plt.scatter(sixties_f3diff, sixties_f1f2diff, marker='x', color='red', label='1960s')
    plt.scatter(seventies_f3diff, seventies_f1f2diff, marker='x', color='blue', label='1970s')
    plt.scatter(eighties_f3diff, eighties_f1f2diff, marker='x', color='orange', label='1980s')
    plt.scatter(nineties_f3diff, nineties_f1f2diff, marker='x', color='green', label='1990s')
    ax.invert_xaxis()
    ax.invert_yaxis()
    
    plt.legend()
    plt.savefig('care_formants_comparison.png')
    
    
    plt.show()
            
def main():
    
    print('Testing my eɹ visualization code')
    
    print(care_data)
    
    graph_care(care_data)
    
    care_years = list(care_data.year)
    print(care_years)
    
main()