pd.Timedelta(np.timedelta64(1, "ms"))
df['fin_time']= pd.to_datetime(df['fin_time'], format='%H:%M:%S.%f')
dfnew = df.loc[df['horse_name'] == "A Country Girl"].filter(['fin_time', 'fin_time_mic', 'horse_name'], axis=1)

#df['mean_tmp']=df.groupby('horse_name')['fin_time_mic'].transform(lambda x: x.ewm(alpha=0.30).mean())
#df['std_tmp']=df.groupby('horse_name')['fin_time_mic'].transform(lambda x: x.ewm(alpha=0.30).std())

