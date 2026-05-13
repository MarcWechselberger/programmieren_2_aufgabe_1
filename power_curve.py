import numpy as np
from sort import bubble_sort
import matplotlib.pyplot as plt
from load_data import load_data

if __name__ == "__main__":
    data = load_data('activity.csv')
    power_W = data['PowerOriginal']
    print(power_W)
    sorted_power_W = bubble_sort(power_W)
    print(sorted_power_W[::-1])

#X-Achse von 1
    time_array = np.arange(0, 1804, 1)

#einfacher Plot mit matplotlib
    plt.plot(time_array, sorted_power_W[::-1])
    #plt.axis((0, 6, 0, 20))
    plt.xlabel('Zeit in Sekunden')
    plt.ylabel('Leistung in Watt')
    
    plt.savefig('figures/NewFigure.png', dpi=200)