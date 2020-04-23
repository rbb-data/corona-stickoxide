import json
import pandas as pd

def read_nox(path):
    '''
    Reads NOx JSON data that we saved from our endpoint and returns a pandas DataFrame
    '''
    with open(path, 'r') as f:
        response = json.load(f)
    df = pd.DataFrame([(d['id'], d['name'], d['federalstate'], v['t'], v['y']) for d in response['data'] for v in d['values']], columns=['id', 'name', 'federal_state', 'datetime', 'val'])
    df['datetime'] = pd.to_datetime(df['datetime'], utc=True)
    return df