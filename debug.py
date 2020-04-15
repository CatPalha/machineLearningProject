import pandas as pd

df = pd.read_csv('train.csv')

df['Age'] = 2020 - df['Birthday_year']

df['Infected_per_Family'] = df['Parents or siblings infected'] + df['Wife/Husband or children infected']

df['Maritial_Status'] = 0

df['Gender'] = 0

df['Title'] = 0


for i in range(0, df.shape[0]):
    
    if df.Name[i].startswith('Miss'):
        df['Maritial_Status'] = 0
        df['Gender'] = 1
        df['Title'] = 'Miss'
        
    elif df.Name[i].startswith('Ms.'):
        df['Maritial_Status'] = 'unknown'
        df['Gender'] = 1
        df['Title'] = 'Ms.'
    
    elif df.Name[i].startswith('Mrs.'):
        df['Maritial_Status'] = 1
        df['Gender'] = 1
        df['Title'] = 'Mrs.'
        
    elif df.Name[i].startswith('Mr.'):
        df['Maritial_Status'] = 1
        df['Gender'] = 0
        df['Title'] = 'Mr.'
        
    elif df.Name[i].startswith('Master'):
        df['Maritial_Status'] = 0
        df['Gender'] = 0
        df['Title'] = 'Master'