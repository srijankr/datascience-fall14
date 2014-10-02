from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import pandas as pd

reader = DataFileReader(open("countries.avro", "r"), DatumReader())

df = pd.DataFrame(columns=('name', 'country_id', 'area_sqkm', 'population'))

for country in reader:
    df = df.append(country, ignore_index=True)
reader.close()

print 'Number of countries with population over 10000000 = ', df[df['population'] > 10000000].groupby('country_id').size().sum()
