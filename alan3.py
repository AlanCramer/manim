from big_ol_pile_of_manim_imports import *
#from math import cos, sin, pi
import math

# from https://github.com/malhotra5/Manim-Tutorial#Running-Manim-Projects

# python3 -m manim alan3.py Shapes -pl
# python3 -m manim alan3.py Equations -pl
# python3 -m manim alan3.py Graphing -pl

class Shapes(Scene):
    def construct(self):
        #######Code#######
        #Making Shapes
        circle = Circle(color=YELLOW)
        square = Square(color=DARK_BLUE)
        square.surround(circle)

        rectangle = Rectangle(height=2, width=3, color=RED)
        ring=Annulus(inner_radius=.2, outer_radius=1, color=BLUE)
        ring2 = Annulus(inner_radius=0.6, outer_radius=1, color=BLUE)
        ring3=Annulus(inner_radius=.2, outer_radius=1, color=BLUE)
        ellipse=Ellipse(width=5, height=3, color=DARK_BLUE)

        pointers = []
        for i in range(8):
            pointers.append(Line(ORIGIN, np.array([cos(pi/180*360/8*i),sin(pi/180*360/8*i), 0]),color=YELLOW))

        #Showing animation
        self.add(circle)
        self.play(FadeIn(square))
        self.play(Transform(square, rectangle))
        self.play(FadeOut(circle), FadeIn(ring))
        self.play(Transform(ring,ring2))
        self.play(Transform(ring2, ring))
        self.play(FadeOut(square), GrowFromCenter(ellipse), Transform(ring2, ring3))
        self.add(*pointers)
        self.wait(2)

class Equations(Scene):
    def construct(self):
        #Making equations
        first_eq = TextMobject("$$J(\\theta) = -\\frac{1}{m} [\\sum_{i=1}^{m} y^{(i)} \\log{h_{\\theta}(x^{(i)})} + (1-y^{(i)}) \\log{(1-h_{\\theta}(x^{(i)}))}] $$")
        second_eq = ["$J(\\theta_{0}, \\theta_{1})$", "=", "$\\frac{1}{2m}$", "$\\sum\\limits_{i=1}^m$", "(", "$h_{\\theta}(x^{(i)})$", "-", "$y^{(i)}$", "$)^2$"]

        second_mob = TextMobject(*second_eq)

        for i,item in enumerate(second_mob):
            if(i != 0):
                item.next_to(second_mob[i-1],RIGHT)

        eq2 = VGroup(*second_mob)

        des1 = TextMobject("With manim, you can write complex equations like this...")
        des2 = TextMobject("Or this...")
        des3 = TextMobject("And it looks nice!!")

        #Coloring equations
        second_mob.set_color_by_gradient("#33ccff","#ff00ff")

        #Positioning equations
        des1.shift(2*UP)
        des2.shift(2*UP)

        #Animating equations
        self.play(Write(des1))
        self.play(Write(first_eq))
        self.play(ReplacementTransform(des1, des2), Transform(first_eq, eq2))
        self.wait(1)

        for i, item in enumerate(eq2):
            if (i<2):
                eq2[i].set_color(color=PURPLE)
            else:
                eq2[i].set_color(color="#00FFFF")

        self.add(eq2)
        self.wait(1)
        self.play(FadeOutAndShiftDown(eq2), FadeOutAndShiftDown(first_eq), Transform(des2, des3))
        self.wait(2)

import math

class Graphing(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE
    }

    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        graph_lab = self.get_graph_label(func_graph, label = "x^{2}")

        func_graph_2=self.get_graph(self.func_to_graph_2,self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label = "x^{3}")

        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x,y, color=YELLOW)

        point = Dot(self.coords_to_point(1,self.func_to_graph(1)))

        #Display graph
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(horz_line))
        self.add(point)
        self.wait(1)
        self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2))
        self.wait(2)


    def func_to_graph(self, x):
        return (x**2)

    def func_to_graph_2(self, x):
        return (x-2) * (x-1) * (x+1)
