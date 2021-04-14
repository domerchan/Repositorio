# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 01:32:31 2021

@author: domer
"""
import matplotlib.pyplot as plt
import numpy as np
import random


m = [10, 100, 1000, 10000, 100000, 1000000]

for n in m:
    list = [random.randint(1,6) + random.randint(1,6) for i in range(n)]
    fig, axs = plt.subplots()
    axs.grid(True)
    axs.set_xticks(range(2,13))
    axs.set_title("Histograma con " + str(n) + " lanzamientos")
    axs.set_xlabel("Sumatoria")
    axs.set_ylabel("Número de ocurrencias")
    axs.hist(list, bins=np.arange(2,14)-0.5, rwidth=0.9, facecolor='tan')
    fig.savefig(str(n) + '-lanzamientos.png')
    
