# Fashion_MNIST

## 1. Understand the dataset

`Fashion-MNIST` is a dataset of [Zalando](https://jobs.zalando.com/tech/)'s article images—consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes. We intend `Fashion-MNIST` to serve as a direct **drop-in replacement** for the original [MNIST dataset](http://yann.lecun.com/exdb/mnist/) for benchmarking machine learning algorithms. It shares the same image size and structure of training and testing splits.
![fashion-mnist-sprite](https://user-images.githubusercontent.com/63126292/99628952-cba4ba80-29fc-11eb-9df9-003808365855.png)

## 2. What I do in this projects
### a. Finding  the best Unsupervised Learning Algorithm by evaluating the best Silhouette score

* Applied KMeans clustering, Hierarchical clustering, and Gaussian mixture models clustering
* Utilized Silhouette coefficient to determine which one is the best model

### b. Visualizing the dataset
* Applied demensionally reduction with PCA, t-SNE, and UMAP
* Evaluated based on visuall plots

## 3. Results.
* The best Clustering Model is KMeans with the number of cluster is 4

![download (2)](https://user-images.githubusercontent.com/63126292/99629616-e9265400-29fd-11eb-9780-ed496f9c6402.png)

* The best dimensional reduction to visualize is UMAP with n_neighbors = 5 and min_dist = 0.3 or n_neighbors = 7 and min_dist = 1

***UMAP dimensionaly with n_neighbors = 5 and min_dist = 0.3***
![download (1)](https://user-images.githubusercontent.com/63126292/99630113-e841f200-29fe-11eb-9e90-34e7ed46c324.png)

***UMAP dimensionaly with n_neighbors = 7 and min_dist = 1***
![download](https://user-images.githubusercontent.com/63126292/99630030-c0528e80-29fe-11eb-9704-9fe6658cccd0.png)

## 4. Link to my work
Due to the large file, I can't upload my work on GitHub. However, I attach my work through google colab
https://colab.research.google.com/drive/14Vgmx5nvFua145AoIZeMjsgBwcznoHqp?usp=sharing
