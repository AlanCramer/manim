# python3 -m manim alanGraph.py Graphing -pl

from big_ol_pile_of_manim_imports import *
from math import sin, cos, pi


class Graphing(GraphScene):

    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": WHITE
    }

    def construct(self):
        # Make graph
        self.setup_axes(animate=False)

        funCt = 2;

        funcs = [self.make_func(i+1) for i in range(funCt)]

        func_graphs = [self.get_graph(func) for func in funcs]

        func_graph_sum = self.get_graph(self.make_sum(funcs), GREEN)

        # Display graph
        for func_graph in func_graphs:
            self.play(ShowCreation(func_graph, run_time=5/funCt))

        self.wait(1)

        transforms = [Transform(func_graph, func_graph_sum, run_time=2) for func_graph in func_graphs]

        self.play(*transforms)

        self.wait(2)

    # approximate saw tooth on -2 to 2:
    # 4/pi * sum (-1)^(n+1)/n * sin((pi/2)*n*x)

    @staticmethod
    def make_func(n):
        def nth_func(x):
            return -4 / (pi * n) * sin((pi / 2) * n * x)
        return nth_func

    @staticmethod
    def make_sum(funcList):
        def sum_func(x):
            ret = 0
            for f in funcList:
                ret = ret + f(x)
            return ret
        return sum_func


