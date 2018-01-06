
"""
The class ParetoOptimization is a wrapper of Pareto optimization methods, even though currently there is only the canonical Pareto optimization method

Author:
    Yu-Ren Liu

"""

from zoopt.opt_algorithms.paretoopt.paretoopt import ParetoOpt


class ParetoOptimization:

    def __init__(self):
        self.__best_solution = None
        self.__algorithm = None

    def clear(self):
        self.__best_solution = None
        self.__algorithm = None

    def opt(self, objective, parameter):
        """
        Optimization function for pareto optimization.

        :param objective: Objective object
        :param parameter: Parameter object
        :return: best solution
        """
        self.clear()
        self.__algorithm = ParetoOpt()
        self.__best_solution = self.__algorithm.opt(objective, parameter)
        return self.__best_solution

    def get_best_sol(self):
        return self.__best_solution