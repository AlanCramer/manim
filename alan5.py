
from big_ol_pile_of_manim_imports import *

class Grid(Scene):
    def construct(self):
        grid = NumberPlane()
        # grid_title = TextMobject("This is a grid")
        # grid_title.scale(1.5)
        # grid_title.move_to(transform_title)

        # self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            # FadeOut(title),
            # FadeInFromDown(grid_title),
            # ShowCreation(grid, run_time=3, lag_ratio=0.1),
            ShowCreation(grid)
        )
        self.wait()

        # grid_transform_title = TextMobject(
        #     "That was a non-linear function \\\\"
        #     "applied to the grid"
        # )
        # grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(4*p[1]),
                np.sin(4*p[0]),
                0,
            ]),
            run_time=6,
        )
        self.wait()
