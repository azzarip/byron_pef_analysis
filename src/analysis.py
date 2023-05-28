import pandas as pd

def extractTimes(filename):
    distance = 4.68/2
    data = pd.read_csv(f'data/{filename}.txt', header=None).drop(columns=[0]).T
    times=data.iloc[::2,0]
    positions = data.iloc[1::2].set_index(times)
    low = abs(positions+distance).idxmin()
    high = abs(positions-distance).idxmin()
    time = high-low
    return time

def getAverage(pre):
    import pandas as pd
    import os
    df = pd.DataFrame()

    for file in os.listdir("data"):
        if file.startswith(pre):
            print(file)
            flow = file.replace(pre,'').replace('.txt','').lstrip('_')            
            times = extractTimes(f'{pre}_{flow}')
            mean = times.mean()
            std = times.std()
            df = pd.concat([df, pd.DataFrame([[flow, mean]])])
                
    df = df.rename(columns={0:'flow', 1:f'{pre}'}).set_index('flow')
    df.index = pd.to_numeric(df.index, errors='coerce')
    return df.sort_index()