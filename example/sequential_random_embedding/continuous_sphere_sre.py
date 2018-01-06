"""
This module contains an example of optimizing high-dimensional sphere function with sequential random embedding.

Author:
    Yu-Ren Liu
"""

from fx import sphere_sre
from zoopt import Dimension, Objective, Parameter, ExpOpt


def sphere_continuous_sre():
    """
    Example of minimizing high-dimensional sphere function with sequential random embedding.

    :return: unused return
    """

    dim_size = 10000  # dimensions
    dim_regs = [[-1, 1]] * dim_size  # dimension range
    dim_tys = [True] * dim_size  # dimension type : real
    dim = Dimension(dim_size, dim_regs, dim_tys)  # form up the dimension object
    objective = Objective(sphere_sre, dim)  # form up the objective function

    # setup algorithm parameters
    budget = 2000  # number of calls to the objective function
    parameter = Parameter(budget=budget, high_dim_handling=True, sre=True, num_sre=5, low_dimension=Dimension(10, [[-1, 1]] * 10, [True] * 10),
                          withdraw_alpha=Dimension(1, [[-1, 1]], [True]), intermediate_result=False,
                          intermediate_freq=100)
    solution_list = ExpOpt.min(objective, parameter, repeat=1, plot=True, plot_file="img/sphere_continuous_sre.png")

if __name__ == "__main__":
    sphere_continuous_sre()