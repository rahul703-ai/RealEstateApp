import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='plotting Demo')

st.title('Analytics')

new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))

# Geo_map
st.header("sector, Price/sqft  GeoMap")
group_df = new_df.groupby('sector').mean(pd.to_numeric)[
    ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']]
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                        mapbox_style="open-street-map", width=1200, height=700,
                        hover_name=group_df.index)

st.plotly_chart(fig, use_container_width=True)

# st.dataframe(group_df)

# wordcloud
st.header("Amenities WordCloud")
plt.rcParams["font.family"] = "Arial"

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size=10).generate(feature_text)

fig = plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig)

# scatter plot area vs price
st.header("Area vs price")
property_type = st.selectbox('Select property type', ['flat', 'house'])
if property_type == "house":
    fig1 = px.scatter(new_df[new_df['property_type'] == "flat"], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == "house"], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")
    st.plotly_chart(fig1, use_container_width=True)

# BHk pie chart
st.header('BHK Pie Chart')

selected_options = new_df['sector'].unique().tolist()
selected_options.insert(0, 'overall')

selected_sector = st.selectbox("Select sector", selected_options)

if selected_sector == 'overall':
    fig3 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig3, use_container_width=True)
else:
    fig3 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')
    st.plotly_chart(fig3, use_container_width=True)

# BHK price comparison using boxplot
st.header('Side by Side Bhk price comparison')

fig4 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig4, use_container_width=True)

# distplot of price of flat and houses

st.header('Distplot For property Type')

fig3=plt.figure(figsize=(10,4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'], label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)







