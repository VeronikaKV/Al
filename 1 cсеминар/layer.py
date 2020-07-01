import numpy as np


class layer:

    def __init__(self):
        pass

    def forward(self, input: np.ndarray): #input [N, D] N-зазмер бетча D- размер инпута,  входного вектора в этот уровень 
        #значеня с пред уровня, передаем 
        return input
#механизм обратного распространеия ошибки для каждого уровня
    def backward(self, input: np.ndarray, grad_output: np.ndarray): #grad output [N, Y] N-зазмер бетча Y- колво выходных связей 
        return np.array([[], []]) # количество строк и столбцов нашего двумерного массива клво сигналов в пред уровне