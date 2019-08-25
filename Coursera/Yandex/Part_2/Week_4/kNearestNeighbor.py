import numpy as np
from scipy.stats import mode
class kNearestNeighbor:
    def __init__(self, X_train, y_train,k=2):
        self.x_ = X_train
        self.y_ = y_train
        self.k_ = k

    def prediction(self, X_test):
        cl_list = list()
        for idx, x in enumerate(X_test):
            dist_min = np.linalg.norm(x - self.x_[0])
            cl = self.y_[0]
            dist = 0
            dist_arr = list()
            for i,x_ in enumerate(self.x_):
                dist = np.linalg.norm(x - x_)
                dist_arr.append(dist)
            min_ids = np.argpartition(np.array(dist_arr), self.k_)[:self.k_]
            # a = self.y_[min_ids]
            # b = np.bincount(self.y_[min_ids]).argmax()
            cl_list.append(np.bincount(self.y_[min_ids]).argmax())

        return cl_list