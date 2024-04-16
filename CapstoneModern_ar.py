#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:08:20 2024

@author: brendandervan
Data Science time woo-hoo!
"""

import matplotlib.pyplot as plt
import pandas as pd
import modern_ar_frame

park_data = modern_ar_frame.get_data()

def graph_park(data):
    
    modern_f1f2diff = []
    modern_f3diff = []
    modern_years = []
    
    
    for i in range(len(data.loc[:, 'year'])):
    
        modern_f1f2diff.append(data.loc[i, 'F1/F2 dif'])
        modern_f3diff.append(data.loc[i, 'F3 dif'])
        modern_years.append(data.loc[i, 'year'])
            
            
    fig, ax = plt.subplots()
    plt.title('Difference in F3 Over Time for "ɐɹ"')
    plt.xlabel('Year')
    plt.ylabel('Formant 3 Difference')
    plt.xticks([2021, 2022, 2023, 2024])
    plt.ylim((-50, 1000))
    
    plt.scatter(modern_years, modern_f3diff, marker='x', color='blue', label='2020s')
    # ax.invert_xaxis()
    # ax.invert_yaxis()
    
    plt.legend()
    plt.savefig('modern_park_formants.png')
    
    
    plt.show()
    
    plt.title('Difference in F3 and Difference Between F1 and F2 for "ɐɹ"')
    plt.xlabel('Difference in Formant 3')
    plt.ylabel('Difference Between Formant 1 and Formant 2')
    plt.xlim((-50, 1000))
    plt.ylim((200, 1300))
    
    plt.scatter(modern_f3diff, modern_f1f2diff, marker='x', color='blue', label='2020s')
    ax.invert_xaxis()
    ax.invert_yaxis()
    
    plt.legend()
    plt.savefig('modern_park_formants_comparison.png')
    
    
    plt.show()
    
    
def main():
    
    print('Testing my ɐɹ visualization code')
    
    print(park_data)
    
    graph_park(park_data)
    
    park_years = list(park_data.year)
    print(park_years)
    
main()