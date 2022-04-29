pd.Timedelta(np.timedelta64(1, "ms"))
df['fin_time']= pd.to_datetime(df['fin_time'], format='%H:%M:%S.%f')

