import datetime as DT
today = DT.date.today()
week_ago = today - DT.timedelta(days=7)
print(week_ago)

#
# today = DT.date.today()
# week_ago = today - DT.timedelta(days=7)
# print(today,week_ago)
#
# filtersf = df[(df['date'] >= str(week_ago)) & (df['date'] <= str(today))]
# filtersf.groupby(by=filtersf['date'].dt.date).count()
#
# with st.container():
# asd = st.selectbox("filter", filtersf["district"].unique())
# wwe = filtersf[filtersf["district"] == asd]
# fig =px.bar(wwe,x = "date",y = "count")
# fig.update_layout(width=900, height=400)
# st.plotly_chart(fig)
#
# fgh = pd.DataFrame(filtersf.groupby(['district']).size().reset_index(name='counts'))
# filtersf.groupby(['count'])['district'].sum()
# df2 = filtersf.groupby(['district'])['count'].sum().reset_index()

df['u'] = pd.to_datetime(df['u']).dt.date
df['u'] = pd.to_datetime(df['u']).dt.normalize()
filtersf = df[(df['u'] >= '2022-07-01') & (df['u'] <= '2022-07-04')]
print(len(filtersf))