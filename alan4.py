
# tutorial https://github.com/malhotra5/Manim-Tutorial#Running-Manim-Projects

# python3 -m manim alan2.py Shapes -pl

from big_ol_pile_of_manim_imports import *

class Ball(Scene):
    def construct(self):
        ball = Circle(
            stroke_width=1,
            stroke_color=BLACK,
            fill_color=GREEN_E,
            fill_opacity=1,
            # sheen_factor=1,
            # sheen_direction=UL,
            radius=1.5,
        )
        square = Square(
            fill_color=RED
        )
        cube = Cube(
            fill_color=RED
        )

        # self.play(ShowCreation(ball))
        self.play(ShowCreation(square))
        # self.play(ShowCreation(cube))
