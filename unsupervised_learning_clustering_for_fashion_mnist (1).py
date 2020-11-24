# -*- coding: utf-8 -*-
"""Unsupervised learning -Clustering for Fashion-MNIST

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cdfu56A7ze5n3v5mvs-dneJaZT4jtGmo

#EDA
"""

# Commented out IPython magic to ensure Python compatibility.
#Import libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
import sklearn
from sklearn.cluster import AgglomerativeClustering, DBSCAN, KMeans
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml
from sklearn.manifold import TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import umap
import plotly.io as plt_io
import plotly.graph_objects as go

import warnings
warnings.filterwarnings("ignore")
# %matplotlib inline

#load dataset
mnist = fetch_openml('Fashion-MNIST', version=1, cache=True)

np.random.seed(1000)
# Select 20000 images randomly
indices = np.random.choice(70000,20000)
X = mnist.data[indices] / 255.0
y = mnist.target[indices]

print(X.shape, y.shape)

#checking y
set(y)

# Standarizing the features
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# Data frame to store features and predicted cluster memberships.
ypred = pd.DataFrame()

# We just want the first two principal components
pca = PCA(n_components=2)

# We get the components by 
# calling fit_transform method with our data
X_pca = pca.fit_transform(X_std)

"""#Clustering

##KMeans
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# #Apply KMean with the evaluation based on Silhouette Score
# sil_k = np.arange(10,dtype="double")
# for k in np.arange(10):
#   km = KMeans(n_clusters=k+2)
#   km.fit(X_pca)
#   sil_k[k] = metrics.silhouette_score(X_pca,km.labels_,metric='euclidean')
#    
# print(sil_k)
# 
# plt.title("KMeans Silhouette")
# plt.xlabel("Number of Cluster")
# plt.plot(np.arange(2,12,1),sil_k)

"""> The highest Silhouette Score for KMeans clustering is 0.4562 with number of cluster is 4

##Hierarchical clustering
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# #Apply hierarchical clustering with the evaluation based on Silhouette Score
# sil_agg = np.arange(10,dtype="double")
# for k in np.arange(10):
#   agg = AgglomerativeClustering(linkage='complete', 
#                                     affinity='cosine',
#                                     n_clusters=k+2)
#   agg.fit(X_pca)
#   sil_agg[k] = metrics.silhouette_score(X_pca,agg.labels_,metric='euclidean')
#   
# print(sil_agg)
# 
# plt.title("Hierrachy Silhouette")
# plt.xlabel("Number of Cluster")
# plt.plot(np.arange(2,12,1),sil_agg)

"""> The highest Silhouette Score for Hierarchical clustering is 0.397 with number of cluster is 3"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# plt.figure(figsize=(20,10))
# dendrogram(linkage(X_pca, method='complete'))
# plt.show()

"""## Gaussian mixture models clustering"""

# Defining the agglomerative clustering
gmm_cluster = GaussianMixture(n_components=10, random_state=1996, covariance_type="full")

# Fit model
clusters = gmm_cluster.fit_predict(X_pca)

print("Silhouette score with covariance_type=full: {}".format(
    metrics.silhouette_score(X_pca, clusters, metric='euclidean')))
print("------------------------------------------------------")

# Defining the agglomerative clustering
gmm_cluster = GaussianMixture(n_components=10, random_state=1996, covariance_type="tied")

# Fit model
clusters = gmm_cluster.fit_predict(X_pca)

print("Silhouette score with covariance_type=tied: {}".format(
    metrics.silhouette_score(X_pca, clusters, metric='euclidean')))
print("------------------------------------------------------")

# Defining the agglomerative clustering
gmm_cluster = GaussianMixture(n_components=10, random_state=1996, covariance_type="diag")

# Fit model
clusters = gmm_cluster.fit_predict(X_pca)

print("Silhouette score with covariance_type=diag: {}".format(
    metrics.silhouette_score(X_pca, clusters, metric='euclidean')))
print("------------------------------------------------------")


# Defining the agglomerative clustering
gmm_cluster = GaussianMixture(n_components=10, random_state=1996, covariance_type="spherical")

# Fit model
clusters = gmm_cluster.fit_predict(X_pca)

print("Silhouette score with covariance_type=spherical: {}".format(
    metrics.silhouette_score(X_pca, clusters, metric='euclidean')))
print("------------------------------------------------------")

"""> The highest Silhouette Score for Gaussian mixture models clustering is 0.3867 with number of cluster is 3 and civariance type is 'full'

## DBSCAN
"""

# Commented out IPython magic to ensure Python compatibility.
# #Apply dbscan clustering with the evaluation based on Silhouette Score
# %%time
# start   = 0.01
# stop    = 1.5
# step    = 0.01
# my_list = np.arange(start, stop+step, step)
# 
# startb   = 1
# stopb    = 10
# stepb    = .2 # To scale proportionately with epsilon increments
# my_listb = np.arange(startb, stopb+stepb, stepb)
# 
# my_range = range(10)
# 
# sil_dbscan = []
# 
# for i in my_range:
#    dbscan = DBSCAN(eps = 0 + my_list[i] , min_samples = 0 + my_listb[i],metric='euclidean')
#    cluster = dbscan.fit_predict(X_pca)
#    sil_dbscan.append(metrics.silhouette_score(X_pca, cluster))

# Commented out IPython magic to ensure Python compatibility.
# %%time
# print(sil_dbscan)
# plt.title("DBSCAN Silhouette")
# plt.ylabel("Silhouette Score")
# plt.xlabel("Number of Eps")
# plt.plot(np.arange(0,10,1),sil_dbscan)

"""> The highest Silhouette Score for DBSCAN models clustering is 0.253 with number of eps = 0.01

## Clustering Evaluation
Overral, the best clustering algorithms is K mean with number of cluster is 4
> let's visuallize the dataset

#Using dimensionality reduction to visualize the dataset

## PCA dimensionally
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# plt.figure(figsize=(10,5))
# colours = ["r","b","g","c","m","y","k","r","burlywood","chartreuse"]
# for i in range(X_pca.shape[0]):
#     plt.text(X_pca[i, 0], X_pca[i, 1], str(y[i]),
#              color=colours[int(y[i])],
#              fontdict={'weight': 'bold', 'size': 50}
#         )
# 
# plt.xticks([])
# plt.yticks([])
# plt.axis('off')

"""Unfortunately the graph above doesn't enable us to infer the classes through visualization. As can be seen in the colored and labeled graph, PCA can gather together the observations of the same classes to some degree. However, observations from all of the classes intertwined each other and can't be distinguished without coloring or labeling. In this respect, PCA solution is not satisfactory.

## t-SNE dimensionally
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
# tsne_results = tsne.fit_transform(X_std)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# plt.figure(figsize=(10,5))
# colours = ["r","b","g","c","m","y","k","r","burlywood","chartreuse"]
# for i in range(tsne_results.shape[0]):
#     plt.text(tsne_results[i, 0], tsne_results[i, 1], str(y[i]),
#              color=colours[int(y[i])],
#              fontdict={'weight': 'bold', 'size': 50}
#         )
# 
# plt.xticks([])
# plt.yticks([])
# plt.axis('off')

"""By using t-SNE, we can distinguish some classes clearly and in this respect t-SNE solution is better than that of PCA's. However, observations from all of the classes intertwined each other and can't be distinguished without coloring or labeling. Let's test with LDA to see whether we have a better visuallization or not

## LDA dimentionally
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# lda = LDA(n_components=2)
# lda_result = lda.fit_transform(X_std,y)

# Commented out IPython magic to ensure Python compatibility.
# %%time 
# plt.figure(figsize=(10,5))
# colours = ["r","b","g","c","m","y","k","r","burlywood","chartreuse"]
# for i in range(lda_result.shape[0]):
#     plt.text(lda_result[i, 0], lda_result[i, 1], y[i],
#              color=colours[int(y[i])],
#              fontdict={'weight': 'bold', 'size': 50}
#         )
# 
# plt.xticks([])
# plt.yticks([])
# plt.axis('off')

"""Unfortunately the graph above doesn't enable us to infer the classes through visualization. As can be seen in the colored and labeled graph, LDA can gather together the observations of the same classes to some degree. We can see clearly it is not as good as t-SNE. However, observations from all of the classes intertwined each other and can't be distinguished without coloring or labeling. Only a few classes are seperated which means those have a large number. Let's test with UMAP to have a better visulization.

## UMAP dimensionally
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# umap_results = umap.UMAP(n_neighbors=5,
#                       min_dist=0.3,
#                       metric='correlation').fit_transform(X_std)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# plt.figure(figsize=(10,5))
# colours = ["r","b","g","c","m","y","k","r","burlywood","chartreuse"]
# for i in range(umap_results.shape[0]):
#     plt.text(umap_results[i, 0], umap_results[i, 1], y[i],
#              color=colours[int(y[i])],
#              fontdict={'weight': 'bold', 'size': 50}
#         )
# 
# plt.xticks([])
# plt.yticks([])
# plt.axis('off')

"""UMAP's solution is better than those of PCA's, t-SNE's, and LDA's because the different classes are separated more clearly. Let's do different parameters to find the best one for visualize

## Tunning parameters for UMAP
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# umap_results = umap.UMAP(n_neighbors=5,
#                       min_dist=1,
#                       metric='correlation').fit_transform(X_std)
# plt.figure(figsize=(10,5))
# colours = ["r","b","g","c","m","y","k","r","burlywood","chartreuse"]
# for i in range(umap_results.shape[0]):
#     plt.text(umap_results[i, 0], umap_results[i, 1], y[i],
#              color=colours[int(y[i])],
#              fontdict={'weight': 'bold', 'size': 50}
#         )
# plt.title("Umap with n_neighbors=5 and min_dist=1")
# plt.xticks([])
# plt.yticks([])
# plt.axis('off')

# Commented out IPython magic to ensure Python compatibility.
# %%time
# umap_results = umap.UMAP(n_neighbors=5,
#                       min_dist=0.3,
#                       metric='correlation').fit_transform(X_std)
# plt.figure(figsize=(10,5))
# colours = ["r","b","g","c","m","y","k","r","burlywood","chartreuse"]
# for i in range(umap_results.shape[0]):
#     plt.text(umap_results[i, 0], umap_results[i, 1], y[i],
#              color=colours[int(y[i])],
#              fontdict={'weight': 'bold', 'size': 50}
#         )
# plt.title("Umap with n_neighbors=7 and min_dist=0.3")
# plt.xticks([])
# plt.yticks([])
# plt.axis('off')

# Commented out IPython magic to ensure Python compatibility.
# %%time
# umap_results = umap.UMAP(n_neighbors=7,
#                       min_dist=1,
#                       metric='correlation').fit_transform(X_std)
# plt.figure(figsize=(10,5))
# colours = ["r","b","g","c","m","y","k","r","burlywood","chartreuse"]
# for i in range(umap_results.shape[0]):
#     plt.text(umap_results[i, 0], umap_results[i, 1], y[i],
#              color=colours[int(y[i])],
#              fontdict={'weight': 'bold', 'size': 50}
#         )
# plt.title("Umap with n_neighbors=7 and min_dist=1")
# plt.xticks([])
# plt.yticks([])
# plt.axis('off')

"""##Dimensionality reduction evaluation

Overal, the best dimentionality reduction is UMAP with n_neighbors = 5 and min_dist = 0.3 or n_neighbors = 7 and min_dist = 1
> Since UMAP is the best visuallization, Let's do something for fun. Create a 3D plot with plotly
"""

# Commented out IPython magic to ensure Python compatibility.
# %%time
# reducer = umap.UMAP(n_neighbors=5,
#                     n_components=3,
#                     min_dist=0.3,
#                     metric='correlation')
# embedding = reducer.fit_transform(X_std)
#

# set color to an array/list of desired values 
y_c = mnist.target[indices]
#marker_color should be a list of numbers, not strings
marker_color= np.array(y_c).astype(int) #

#3d plot function
def plot_3d(component1,component2,component3):
  colours = ["r","b","g","c","m","y","k","r","burlywood","chartreuse"]
  fig = go.Figure(data=[go.Scatter3d(
        x=component1,
        y=component2,
        z=component3,
        mode='markers',
        marker=dict(
            size=10,
            color=marker_color,                
            colorscale='Rainbow',   # choose a colorscale
            opacity=1,
            line_width=1))])
  
# tight layout
  fig.update_layout(margin=dict(l=50,r=50,b=50,t=50),width=1800,height=1000)
  fig.layout.template = 'plotly_dark'
  
  fig.show()

# Commented out IPython magic to ensure Python compatibility.
# %%time 
# plot_3d(reducer.embedding_[:, 0],reducer.embedding_[:, 1],reducer.embedding_[:, 2])