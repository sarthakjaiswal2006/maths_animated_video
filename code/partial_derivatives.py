
from manim import *


class PartialDerivatives(ThreeDScene):

    def construct(self):

        # ==================================================
        # SECTION 1: INTRODUCTION (20 SECONDS)
        # ==================================================

        title = Text(
            "PARTIAL DERIVATIVES",
            font_size=48,
            color=BLUE,
            weight=BOLD
        )

        subtitle = Text(
            "A Visual Introduction to Multivariable Calculus",
            font_size=23
        ).next_to(title, DOWN, buff=0.4)

        self.play(Write(title), run_time=3)
        self.play(FadeIn(subtitle), run_time=2)
        self.wait(10)
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            run_time=2
        )
        self.wait(3)

        # ==================================================
        # SECTION 2: FUNCTIONS OF TWO VARIABLES (30 SEC)
        # ==================================================

        heading = Text(
            "Functions of Two Variables",
            font_size=34,
            color=BLUE
        ).to_edge(UP)

        explanation = Text(
            "A function can depend on two independent variables.",
            font_size=23
        )

        equation = MathTex(
            r"f(x,y)=x^2+2y^2",
            font_size=58,
            color=YELLOW
        )

        explanation.next_to(heading, DOWN, buff=0.7)
        equation.next_to(explanation, DOWN, buff=0.8)

        inputs = MathTex(
            r"x,\ y \longrightarrow f(x,y)",
            font_size=38
        ).next_to(equation, DOWN, buff=0.7)

        self.play(Write(heading), run_time=2)
        self.play(FadeIn(explanation), run_time=3)
        self.play(Write(equation), run_time=3)
        self.play(FadeIn(inputs), run_time=2)
        self.wait(17)
        self.play(
            FadeOut(heading),
            FadeOut(explanation),
            FadeOut(equation),
            FadeOut(inputs),
            run_time=3
        )

        # ==================================================
        # SECTION 3: 3D SURFACE (40 SECONDS)
        # ==================================================

        heading = Text(
            "Visualizing the Function in 3D",
            font_size=32,
            color=BLUE
        ).to_edge(UP)

        self.add_fixed_in_frame_mobjects(heading)
        self.play(Write(heading), run_time=2)

        axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[0, 12, 2],
            x_length=6,
            y_length=6,
            z_length=4
        )

        surface = Surface(
            lambda u, v: axes.c2p(
                u,
                v,
                u**2 + 2*v**2
            ),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(24, 24)
        )

        surface.set_fill(BLUE, opacity=0.8)
        surface.set_stroke(WHITE, opacity=0.25)

        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        z_label = axes.get_z_axis_label("f(x,y)")

        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.8
        )

        self.play(Create(axes), run_time=4)
        self.play(FadeIn(surface), run_time=5)

        self.play(
            FadeIn(x_label),
            FadeIn(y_label),
            FadeIn(z_label),
            run_time=2
        )

        formula = MathTex(
            r"z=x^2+2y^2",
            font_size=38,
            color=YELLOW
        ).to_corner(UL)

        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula), run_time=2)

        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(20)
        self.stop_ambient_camera_rotation()

        self.play(
            FadeOut(heading),
            FadeOut(formula),
            run_time=2
        )

        # ==================================================
        # SECTION 4: PARTIAL DERIVATIVE WITH RESPECT TO X
        # (50 SECONDS)
        # ==================================================

        heading_x = Text(
            "Partial Derivative with Respect to x",
            font_size=29,
            color=YELLOW
        ).to_edge(UP)

        description_x = Text(
            "Keep y constant. Observe the change along x.",
            font_size=21
        ).next_to(heading_x, DOWN, buff=0.25)

        self.add_fixed_in_frame_mobjects(
            heading_x,
            description_x
        )

        self.play(
            Write(heading_x),
            FadeIn(description_x),
            run_time=3
        )

        y_fixed = 1

        x_curve = ParametricFunction(
            lambda t: axes.c2p(
                t,
                y_fixed,
                t**2 + 2*y_fixed**2
            ),
            t_range=[-2, 2],
            color=YELLOW,
            stroke_width=7
        )

        self.play(Create(x_curve), run_time=5)

        fixed_y = MathTex(
            r"y=1",
            font_size=40,
            color=YELLOW
        ).to_corner(UL)

        self.add_fixed_in_frame_mobjects(fixed_y)
        self.play(Write(fixed_y), run_time=2)

        cross_section = MathTex(
            r"f(x,1)=x^2+2",
            font_size=42,
            color=YELLOW
        ).to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(cross_section)
        self.play(Write(cross_section), run_time=3)

        derivative_x = MathTex(
            r"\frac{\partial f}{\partial x}=2x",
            font_size=48,
            color=GREEN
        ).to_edge(DOWN)

        self.play(
            Transform(cross_section, derivative_x),
            run_time=3
        )

        self.wait(27)

        self.play(
            FadeOut(heading_x),
            FadeOut(description_x),
            FadeOut(fixed_y),
            FadeOut(cross_section),
            FadeOut(x_curve),
            run_time=3
        )

        # ==================================================
        # SECTION 5: PARTIAL DERIVATIVE WITH RESPECT TO Y
        # (50 SECONDS)
        # ==================================================

        heading_y = Text(
            "Partial Derivative with Respect to y",
            font_size=29,
            color=ORANGE
        ).to_edge(UP)

        description_y = Text(
            "Keep x constant. Observe the change along y.",
            font_size=21
        ).next_to(heading_y, DOWN, buff=0.25)

        self.add_fixed_in_frame_mobjects(
            heading_y,
            description_y
        )

        self.play(
            Write(heading_y),
            FadeIn(description_y),
            run_time=3
        )

        x_fixed = 1

        y_curve = ParametricFunction(
            lambda t: axes.c2p(
                x_fixed,
                t,
                x_fixed**2 + 2*t**2
            ),
            t_range=[-2, 2],
            color=ORANGE,
            stroke_width=7
        )

        self.play(Create(y_curve), run_time=5)

        fixed_x = MathTex(
            r"x=1",
            font_size=40,
            color=ORANGE
        ).to_corner(UL)

        self.add_fixed_in_frame_mobjects(fixed_x)
        self.play(Write(fixed_x), run_time=2)

        cross_section_y = MathTex(
            r"f(1,y)=1+2y^2",
            font_size=42,
            color=ORANGE
        ).to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(cross_section_y)
        self.play(Write(cross_section_y), run_time=3)

        derivative_y = MathTex(
            r"\frac{\partial f}{\partial y}=4y",
            font_size=48,
            color=GREEN
        ).to_edge(DOWN)

        self.play(
            Transform(cross_section_y, derivative_y),
            run_time=3
        )

        self.wait(27)

        self.play(
            FadeOut(heading_y),
            FadeOut(description_y),
            FadeOut(fixed_x),
            FadeOut(cross_section_y),
            FadeOut(y_curve),
            FadeOut(surface),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(z_label),
            run_time=4
        )

        # ==================================================
        # SECTION 6: MATHEMATICAL DERIVATION (35 SECONDS)
        # ==================================================

        self.set_camera_orientation(
            phi=0,
            theta=-90 * DEGREES,
            zoom=1
        )

        derivation_title = Text(
            "Mathematical Derivation",
            font_size=38,
            color=BLUE
        ).to_edge(UP)

        self.add_fixed_in_frame_mobjects(derivation_title)
        self.play(Write(derivation_title), run_time=2)

        original = MathTex(
            r"f(x,y)=x^2+2y^2",
            font_size=43
        ).shift(UP * 1.7)

        dx = MathTex(
            r"\frac{\partial f}{\partial x}=2x+0=2x",
            font_size=40,
            color=GREEN
        ).shift(UP * 0.3)

        dy = MathTex(
            r"\frac{\partial f}{\partial y}=0+4y=4y",
            font_size=40,
            color=ORANGE
        ).shift(DOWN * 1)

        self.add_fixed_in_frame_mobjects(
            original,
            dx,
            dy
        )

        self.play(Write(original), run_time=3)
        self.play(Write(dx), run_time=5)
        self.play(Write(dy), run_time=5)

        note = Text(
            "Differentiate one variable at a time.",
            font_size=25,
            color=YELLOW
        ).to_edge(DOWN)

        self.add_fixed_in_frame_mobjects(note)
        self.play(FadeIn(note), run_time=2)
        self.wait(12)

        self.play(
            FadeOut(derivation_title),
            FadeOut(original),
            FadeOut(dx),
            FadeOut(dy),
            FadeOut(note),
            run_time=3
        )

        # ==================================================
        # SECTION 7: WORKED EXAMPLE (30 SECONDS)
        # ==================================================

        example_title = Text(
            "Worked Example",
            font_size=40,
            color=BLUE
        ).to_edge(UP)

        self.add_fixed_in_frame_mobjects(example_title)
        self.play(Write(example_title), run_time=2)

        question = MathTex(
            r"\text{Evaluate at }(1,1)",
            font_size=36
        ).shift(UP * 1.2)

        function = MathTex(
            r"f(x,y)=x^2+2y^2",
            font_size=42,
            color=YELLOW
        )

        value = MathTex(
            r"f(1,1)=1^2+2(1)^2=3",
            font_size=38
        ).shift(DOWN * 0.8)

        result = MathTex(
            r"\frac{\partial f}{\partial x}(1,1)=2",
            r"\qquad",
            r"\frac{\partial f}{\partial y}(1,1)=4",
            font_size=32,
            color=GREEN
        ).shift(DOWN * 2)

        self.add_fixed_in_frame_mobjects(
            question,
            function,
            value,
            result
        )

        self.play(Write(question), run_time=2)
        self.play(Write(function), run_time=3)
        self.play(Write(value), run_time=4)
        self.play(Write(result), run_time=4)

        self.wait(11)

        self.play(
            FadeOut(example_title),
            FadeOut(question),
            FadeOut(function),
            FadeOut(value),
            FadeOut(result),
            run_time=2
        )

        # ==================================================
        # SECTION 8: CONCLUSION (15 SECONDS)
        # ==================================================

        conclusion = Text(
            "What Did We Learn?",
            font_size=40,
            color=BLUE
        ).to_edge(UP)

        point1 = Text(
            "Measure change in one variable at a time.",
            font_size=25
        )

        point2 = Text(
            "Keep the other variable constant.",
            font_size=25
        )

        final_formula = MathTex(
            r"\frac{\partial f}{\partial x}=2x",
            r"\qquad",
            r"\frac{\partial f}{\partial y}=4y",
            font_size=38,
            color=GREEN
        )

        points = VGroup(
            point1,
            point2,
            final_formula
        ).arrange(DOWN, buff=0.8)

        self.add_fixed_in_frame_mobjects(
            conclusion,
            points
        )

        self.play(Write(conclusion), run_time=2)
        self.play(FadeIn(point1), run_time=2)
        self.play(FadeIn(point2), run_time=2)
        self.play(Write(final_formula), run_time=3)

        self.wait(4)
