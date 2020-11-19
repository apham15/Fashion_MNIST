# Fashion_MNIST

## 1. Understand the dataset

`Fashion-MNIST` is a dataset of [Zalando](https://jobs.zalando.com/tech/)'s article images—consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes. We intend `Fashion-MNIST` to serve as a direct **drop-in replacement** for the original [MNIST dataset](http://yann.lecun.com/exdb/mnist/) for benchmarking machine learning algorithms. It shares the same image size and structure of training and testing splits.
![fashion-mnist-sprite](https://user-images.githubusercontent.com/63126292/99628952-cba4ba80-29fc-11eb-9df9-003808365855.png)

## 2. What I do in this projects
### a. Finding  the best Unsupervised Learning Algorithm by evaluating the best Silhouette score
### b. Visualizing the dataset

## 3. Results.
### a. The best Clustering Model is KMeans with the number of cluster is 4
![download (2)](https://user-images.githubusercontent.com/63126292/99629616-e9265400-29fd-11eb-9780-ed496f9c6402.png)

### b. The best dimentionality reduction to visualize is UMAP with n_neighbors = 5 and min_dist = 0.3 or n_neighbors = 7 and min_dist = 1
