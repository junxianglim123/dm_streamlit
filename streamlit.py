
import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')

# Create a title and a subtitle
st.title("Streamlit App")
st.subheader("Find the best location for your next store")
# Create a text input for the user
n_clusters = st.number_input("Enter a number:", value=5, min_value=0)

# Perform K-Means clustering with 5 clusters
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(df[['longitude', 'latitude']])


df['cluster'] = kmeans.labels_

cluster_centers = kmeans.cluster_centers_

plt.scatter(df['longitude'], df['latitude'], c=df['cluster'], cmap='rainbow')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', color='black')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('K-Means Clustering of Laundry Shop Customers')

st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)
