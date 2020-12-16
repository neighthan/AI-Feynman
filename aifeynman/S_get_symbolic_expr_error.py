# Calculates the error of a given symbolic expression applied to a dataset. The input should be a string of the mathematical expression

import numpy as np
from sympy import N, lambdify
from sympy.parsing.sympy_parser import parse_expr


def get_symbolic_expr_error(data, expr):
    try:
        N_vars = len(data[0]) - 1
        possible_vars = ["x%s" % i for i in np.arange(0, 30, 1)]
        variables = []
        for i in range(N_vars):
            variables = variables + [possible_vars[i]]
        eq = parse_expr(expr)
        f = lambdify(variables, N(eq))
        real_variables = []

        for i in range(len(data[0]) - 1):
            check_var = "x" + str(i)
            if check_var in np.array(variables).astype("str"):
                real_variables = real_variables + [data[:, i]]

        # Remove accidental nan's
        good_idx = np.where(np.isnan(f(*real_variables)) == False)

        # use this to get rid of cases where the loss gets complex because of transformations of the output variable
        if isinstance(np.mean((f(*real_variables) - data[:, -1]) ** 2), complex):
            return 1000000
        else:
            try:
                return np.mean(
                    np.log2(
                        1
                        + abs(f(*real_variables)[good_idx] - data[good_idx][:, -1])
                        * 2 ** 30
                    )
                )
            except:
                return np.mean(
                    np.log2(1 + abs(f(*real_variables) - data[:, -1]) * 2 ** 30)
                )
    except:
        return 1000000
