import environment
import random

def element_wise_multiplication(A, B):
    res = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            res[i][j] = A[i]*B[j]
    return res

def matrix_multiplication(A, B):
    res = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            res[i][j] = 0
            for k in range(len(A[0])):
                res[i][j] += A[i][k] * B[k][j]
    return  res

def column_sum(A):
    res = [[0] for i in len(A)]
    for i in range(len(A)):
        res[i][0] = sum(A[i])
    return res

def matrix_sum(A, B):
    # If you want the sum to be broadcasted in case B is just one column in size, use it as second argument
    res = [[0 for i in range(len(A[0]))] for j in range(len(B))]
    for i in range(len(B)):
        for j in range(len(A[0])):
            try:
                res[i][j] = A[i][j] + B[i][j]
            except:
                res[i][j] = A[i][j] + B[i][0]
    return res

def relu(A):
    res = [[0 for i in range(len(A[0]))] for j in range(len(A))] 
    for i in range(len(A)):
        for j in range(len(A[0])):
            res[i][j] = A[i][j]*(A[i][j]>0)
    return res

'''
Now we move forward to declare our deep learning agent:

The agent uses two neural networks to store value function approximations corresponding to each of the two possible actions: moveLeft and moveRight
Each of these neural networks thus takes state features as input and computes the value function for given state (and action according to which of the two nets is used)
To construct the feature vector we use: x-coordinate of ball, y-coordinate of ball, x-coordinate of slider, velocity of ball in x direction and velocity of ball in y direction.

Each of these two neural networks consists of 2 hidden layers, the input layer consists of 5 nodes, first hidden layer consists of 5 nodes, 2nd hidden layer consists of 3 nodes and the output layer consists of a single neuron that outputs the estimated action-value funciton.

All layers except the last one use ReLu activation function but the last layer uses linear activation function.
We use mean squared error as our loss function.
'''
                
class agent:
    def __init__(self):
        self.last_state = -1
        self.addMode = -1
        
        self.lw1 = [[random.random() for i in range(5)] for j in range(5)]
        self.lb1 = [[random.random() for i in range(1)] for j in range(5)]
        self.lw2 = [[random.random() for i in range(5)] for j in range(3)]
        self.lb2 = [[random.random() for i in range(1)] for j in range(3)]
        self.lw3 = [[random.random() for i in range(3)] for j in range(1)]
        self.lb3 = [[random.random() for i in range(1)] for j in range(1)]
        self.ltrain_data = []
        self.lestimates = []
        
        self.rw1 = [[random.random() for i in range(5)] for j in range(5)]
        self.rb1 = [[random.random() for i in range(1)] for j in range(5)]
        self.rw2 = [[random.random() for i in range(5)] for j in range(3)]
        self.rb2 = [[random.random() for i in range(1)] for j in range(3)]
        self.rw3 = [[random.random() for i in range(3)] for j in range(1)]
        self.rb3 = [[random.random() for i in range(1)] for j in range(1)]
        
        self.rtrain_data = []
        self.restimates = []
        
    def levaluate(self, state):
        state_ = [[i] for i in state]
        a1 = relu(matrix_sum(matrix_multiplication(self.lw1, state_), self.lb1))
        a2 = relu(matrix_sum(matrix_multiplication(self.lw2, a1), self.lb2))
        a3 = matrix_sum(matrix_multiplication(self.lw3, a2), self.lb3)
        return [a1, a2, a3]
    
    def revaluate(self, state):
        state_ = [[i] for i in state]
        a1 = relu(matrix_sum(matrix_multiplication(self.rw1, state_), self.rb1))
        a2 = relu(matrix_sum(matrix_multiplication(self.rw2, a1), self.rb2))
        a3 = matrix_sum(matrix_multiplication(self.rw3, a2), self.rb3)
        return [a1, a2, a3]
        
    def get_action(self, ball, slider):
        
        state = [ball.xPos, ball.yPos, slider.xPos, ball.xSpeed, ball.ySpeed]
        self.last_state = state
        if self.revaluate(state)[2][0][0] > self.levaluate(state)[2][0][0]:
            #self.rtrain_data.append(state)
            self.addMode = 0
            return 1
        else:
            #self.ltrain_data.append(state)
            self.addMode = 1
            return 0
        
    def get_reward(self, ball, slider):
        state = [ball.xPos, ball.yPos, slider.xPos, ball.xSpeed, ball.ySpeed]
        reward = environment.reward(ball, slider)
        if self.addMode and self.addMode!=-1:
            self.ltrain_data.append(self.last_state)
            self.lestimates.append(reward+self.levaluate(state)[2][0][0])
        else:
            self.rtrain_data.append(self.last_state)
            self.restimates.append(reward+self.revaluate(state)[2][0][0])
