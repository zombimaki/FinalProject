import os
import glob
import pandas as pd

os.chdir("yearly_incident_data/pre_2018")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

incidents_comb = pd.concat([pd.read_csv(f) for f in all_filenames ])

incidents_comb.to_csv("incidents_2010_2018June.csv", index=False, encoding='utf-8-sig')

# Run with the above first, then comment out what's above, uncomment below and run again:
# os.chdir("yearly_incident_data/since_2018")

# extension = 'csv'
# all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# incidents_comb2 = pd.concat([pd.read_csv(f) for f in all_filenames ])

# incidents_comb2.to_csv("incidents_2018June_2020.csv", index=False, encoding='utf-8-sig')