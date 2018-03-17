import numpy as np

def J(X, y, theta):
    """
    Cost function
    """
    m = X.shape[0]
    return np.sum((X.dot(theta.T) - y) ** 2) / (2*m)


# Pop, Lucro
f = open('datasets/foodtruck.txt')
lines = f.readlines()
alpha = 0.01

dataset = list(map(lambda x: x.split(','), lines))

X = np.array([float(d[0]) for d in dataset]).reshape(-1, 1)
y = np.array([float(d[1]) for d in dataset]).reshape(-1, 1)

X = np.insert(X, 0, 1, axis=1)

theta = np.array([[0.2, 0.2]])

assert X.shape == (97, 2)
assert y.shape == (97, 1)
assert theta.shape == (1, 2)

for i in range(1000):
    error = X.dot(theta.T) - y
    dvt = error.T.dot(X) / (X.shape[0])
    theta = theta - alpha * dvt

    print("{it}: {cost}".format(it=i, cost=J(X, y, theta)))


print(theta)
