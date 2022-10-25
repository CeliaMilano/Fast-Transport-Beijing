# ***********************************************************************************
# ********************************* Reading of data *********************************
# ***********************************************************************************

older_path = '/Users/mateoraeth/Desktop/BIA2_camp/release/taxi_log_2008_by_id/'

#allow us to have a list of all files name
file_list = glob.glob(folder_path + "*.txt")

#creation of the first df
df = pd.read_csv(file_list[132],sep=",", header=None)

#for i in range(1,len(file_list)):

for i in range(0,50):
    #to have size of the file to know how we will deal with it
    filesize = os.path.getsize(file_list[i])
    #print(filesize)
    if filesize !=0:
        #creation of the df with the i file
        df2 = pd.read_csv(file_list[i],sep=",", header=None)
        #concatenation of the main df and the new df2
        df = pd.concat([df, df2], axis = 0, ignore_index=True)

df['date_time'] = pd.to_datetime(df['date_time'])

df["coordinates"] = df.apply(lambda row: (str(round(row.latitude, 3)),str(round(row.longitude, 3))),axis=1)

df_clean = df.drop_duplicates()

from functools import cache

@cache
def geolocate(coordinates):
    print('Call to geolocator with coordinates', coordinates)
    return geolocator.reverse(coordinates).raw["address"]

geolocator = Nominatim(user_agent="geoapiExercises")

df["road"] = df.apply(lambda row: geolocate(row['coordinates']),axis=1
df["road"] = df["road"].raw