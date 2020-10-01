import numpy as np
import math
import random
from collections import Counter
import torch

###########################################
# Code
###########################################


def load_yacht_dataset():
    data = np.loadtxt('yacht_hydrodynamics.csv', delimiter=",")
    train_end = math.floor(data.shape[0]*.8)
    train_data = data[:train_end]
    test_data = data[train_end:]

    train_inputs = torch.from_numpy(train_data[:, :-1]).float()
    train_outputs = torch.from_numpy(train_data[:, -1].reshape((-1, 1))).float()
    test_inputs = torch.from_numpy(test_data[:, :-1]).float()
    test_outputs = torch.from_numpy(test_data[:, -1].reshape((-1, 1))).float()

    return train_inputs, train_outputs, test_inputs, test_outputs


def set_random_seeds():
    seed = 12
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)  # if you are using multi-GPU.
    np.random.seed(seed)  # Numpy module.
    random.seed(seed)  # Python random module.
    torch.manual_seed(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True


class Question2:
    def __init__(self):
        self.train_inputs, self.train_outputs, self.test_inputs, self.test_outputs = load_yacht_dataset()

        self.train_set_size = self.train_inputs.shape[0]
        self.test_set_size = self.test_inputs.shape[0]

        self.loss_fn = torch.nn.MSELoss()

    def train_model(self, model):
        learning_rate = 1e-3
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

        for epoch in range(10000):
            optimizer.zero_grad()
            y_pred = model.forward(self.train_inputs)

            loss = self.loss_fn(y_pred, self.train_outputs)
            if epoch % 1000 == 0:
                print("Epoch %d, MSE on epoch is: %0.4f" % (epoch, loss))
            loss.backward()
            optimizer.step()
        return model

    def train_and_evaluate_model_q2_a(self):
        set_random_seeds()

        # D_in is input dimension;
        # H is hidden dimension; D_out is output dimension.
        D_in, H, D_out = 6, 100, 1

        model = torch.nn.Sequential(
            torch.nn.Linear(D_in, H),
            torch.nn.ReLU(),
            torch.nn.Linear(H, D_out),
        )
        model = self.train_model(model)
        return self.evaluate_model(model)

    def train_and_evaluate_model_q2_b(self):
        set_random_seeds()

        #model = None ## TODO: For question 2b, create a better model!
        D_in, H, D_out = 6, 200, 1

        model = torch.nn.Sequential(
            torch.nn.Linear(D_in, H),
            torch.nn.Tanh(),
            torch.nn.Linear(H, D_out),
        )

        model = self.train_model(model)
        return self.evaluate_model(model)

    def evaluate_model(self, model):
        """ Takes as input a trained model.

        Use model.forward() and self.loss_fn() to evaluate the model on the test set.
        You should return the MSE on the test set"""

        ## TODO: Implement this function for question 2a
        ## The autograder will give you a grade based on whether or not the return value from
        ## train_and_evaluate_model_q2_a is correct.
        y_pred_test = model.forward(self.test_inputs)
        return self.loss_fn(y_pred_test, self.test_outputs)



if __name__ == "__main__":
    q = Question2()
    print(q.train_and_evaluate_model_q2_a())
    print(q.train_and_evaluate_model_q2_b())

