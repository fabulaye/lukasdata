import numpy as np


class perceptron():
    def __init__(self,X,y):
        self.X=X
        self.y=y
    def fit(self,learning_rate=0.1,weights=None,threshold=0.5,max_epoch=30):
        if weights==None:
                weights=np.zeros(self.X.shape[1])
        self.bias=0
        for epoch in range(max_epoch):
            e_list=[]
            y_hat_list=[]
            for index,row in enumerate(self.X):
                linear_output=row@weights+self.bias
                y_hat=self.step_function(linear_output,threshold=threshold)
                e=self.y[index]-y_hat
                
                weights=weights+learning_rate*e
                e_list.append(e[0])
                y_hat_list.append(y_hat[0])
            e=np.array(e_list)
            if e.sum()==0:
                    break
        self.weights=weights
        self.y_hat=y_hat_list
        self.e=e
        return self
    def step_function(self,probabilities,threshold):
         return apply_threshold(probabilities,threshold)


def apply_threshold(probabilities, threshold=0.5):
    return np.where(probabilities >= threshold, 1, 0)



X=np.array([[0,0],
 [1,0],
 [0,1],
 [1,1]])

y=np.array([[0],[0],[0],[1]])

percep=perceptron(X,y)
percep.fit()
print(percep.y_hat)
print(percep.e)



     