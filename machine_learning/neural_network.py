import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)  # Derivative of the sigmoid function

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)  # Derivative of ReLU


class my_neural_network():
    def __init__(self,X,y,layer_sizes) -> None:
        self.X=X
        self.y=y
        self.layer_sizes=layer_sizes
    def init_parameters(self,):
        parameters={}
        for i in range(1, len(self.layer_sizes)):
            parameters[f"W{i}"]=np.random.randn(self.layer_sizes[l-1], layer_sizes[l]) * 0.01
            parameters[f"b{i}"] = np.zeros((1, self.layer_sizes[l]))
        return parameters
    def forward_propagation(self):
        cache={"A0":self.X}
        A=self.X
        for layer in range(1,len(self.layer_sizes)):
            Z = np.dot(A, self.parameters[f"W{layer}"]) + self.parameters[f"b{layer}"]
            A=relu(Z)
            cache[f"Z{layer}"] = Z
            cache[f"A{layer}"] = A
        #output layer
        Z = np.dot(A, self.parameters[f"W{len(self.layer_sizes)}"]) + self.parameters[f"b{len(self.layer_sizes)}"]
        A = sigmoid(Z)
        cache[f"Z{len(self.layer_sizes)}"] = Z
        cache[f"A{len(self.layer_sizes)}"] = A
        self.A=A
        self.cache=cache
        return self
    def compute_loss(self):
        return np.sum(np.sqrt(self.y-self.A))
    def backpropagation(self):
        gradients={}
        m=self.y.shape[0]
        L=len(self.layer_sizes)
        # SSE loss derivative with respect to Z
        dZ = (self.cache[f"A{L}"] - self.y) * self.cache[f"A{L}"] * (1 - self.cache[f"A{L}"]) / m
        gradients[f"dW{L}"] = np.dot(self.cache[f"A{L-1}"].T, dZ) / m
        gradients[f"db{L}"] = np.sum(dZ, axis=0, keepdims=True) / m
        for l in reversed(range(1, L)):
            dA = np.dot(dZ, self.parameters[f"W{l+1}"].T)
            dZ = dA * relu_derivative(self.cache[f"Z{l}"])
            gradients[f"dW{l}"] = np.dot(self.cache[f"A{l-1}"].T, dZ) / m
            gradients[f"db{l}"] = np.sum(dZ, axis=0, keepdims=True) / m
        self.gradients=gradients
        return self
    def update_parameters(self):
        L=len(self.layer_sizes)
        for l in range(1, L + 1):
            self.parameters[f"W{l}"] -= self.learning_rate * self.gradients[f"dW{l}"]
            self.parameters[f"b{l}"] -= self.learning_rate * self.gradients[f"db{l}"]
        return self
    def fit(self,max_epoch=100):
        for epoch in range(max_epoch):
            self.init_parameters()
            self.forward_propagation()
            self.backpropagation()
            self.update_parameters()
        return self