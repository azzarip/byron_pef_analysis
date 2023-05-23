import pandas as pd

def getTimes(filename):
    distance = 4.68/2
    data = pd.read_csv(f'data/{filename}.txt', header=None).drop(columns=[0]).T
    times=data.iloc[::2,0]
    positions = data.iloc[1::2].set_index(times)
    low = abs(positions+distance).idxmin()
    high = abs(positions-distance).idxmin()
    time = high-low
    return time
