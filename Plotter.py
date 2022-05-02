import sympy as sym
import numpy as np
import matplotlib.pyplot as plt


def f(value, function):
    x = sym.symbols('x')
    # function = sym.sympify(function)
    return function.evalf(subs={x: value})


def plot(equation, x_min, x_max, step):
    function = sym.sympify(equation, convert_xor=True)
    X = np.arange(x_min, x_max, step)
    Y = np.array([f(x, function) for x in X])
    plt.grid()
    plt.plot(X, Y)
    plt.show()


if __name__ == '__main__':
    # Input
    function = input('Enter function: ')
    x_min = float(input('Enter x_min: '))
    x_max = float(input('Enter x_max: '))
    x_step = float(input('Enter x_step: '))

    # Plotting
    plot(function, x_min, x_max, x_step)
    plt.show()
