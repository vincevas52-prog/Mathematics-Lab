import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ==========================================
# PARTIAL DERIVATIVES
# Based on Folland, Advanced Calculus, §2.2
# ==========================================

st.title("Partial Derivatives")

st.markdown(r"""
In single-variable calculus, the derivative describes
how a function changes as its input varies.

For a function of several variables, however,
we can change one variable while keeping
the others fixed.

This leads to the notion of a **partial derivative**.
""")

st.divider()


# ==========================================
# PURPLE EXPANDER STYLE
# ==========================================

st.markdown("""
<style>
div[data-testid="stExpander"] > details > summary {
    background-color: #382A56;
    color: #FFFFFF;
    border-radius: 8px;
    padding: 12px 16px;
    transition: background-color 0.2s ease;
}

div[data-testid="stExpander"] > details > summary:hover {
    background-color: #4B396E;
}

div[data-testid="stExpander"] > details > summary * {
    color: #FFFFFF;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# 1. PARTIAL DERIVATIVES IN TWO VARIABLES
# ==========================================

st.header("1. Partial Derivatives in Two Variables")

st.markdown(r"""
Consider a function $f:\mathbb{R}^2\to\mathbb{R}$,
defined in a neighborhood of $(x_0,y_0)$.

To study how $f$ changes with respect to $x$,
we keep $y=y_0$ fixed and consider
the one-variable function
""")

st.latex(r"g(x)=f(x,y_0).")

st.markdown(r"""
We can now differentiate $g$ using
the usual definition of the derivative.

This gives the **partial derivative of $f$
with respect to $x$** at $(x_0,y_0)$:
""")

st.latex(r"""
\boxed{
\frac{\partial f}{\partial x}(x_0,y_0)
=
\lim_{h\to0}
\frac{f(x_0+h,y_0)-f(x_0,y_0)}{h}.
}
""")

st.markdown(r"""
Similarly, fixing $x=x_0$ and allowing
only $y$ to vary, we define
""")

st.latex(r"""
\boxed{
\frac{\partial f}{\partial y}(x_0,y_0)
=
\lim_{h\to0}
\frac{f(x_0,y_0+h)-f(x_0,y_0)}{h}.
}
""")

st.markdown(r"""
Both definitions require the corresponding
limits to exist and be finite.

**The essential idea is simple:** a partial derivative
is an ordinary derivative obtained by varying
only one coordinate.
""")


# ==========================================
# 2. INTERACTIVE VISUALIZATION
# ==========================================

st.divider()

st.header("2. Interactive Visualization")

st.markdown(r"""
Let us explore the function
""")

st.latex(r"f(x,y)=x^2+xy+2y^2.")

st.markdown(r"""
Its partial derivatives are
""")

st.latex(r"""
\frac{\partial f}{\partial x}=2x+y,
\qquad
\frac{\partial f}{\partial y}=x+4y.
""")

left, right = st.columns([0.85, 1.25], gap="large")

with left:

    st.markdown("**Choose a point and a direction**")

    x0 = st.slider(
        "Choose x₀",
        min_value=-1.5,
        max_value=1.5,
        value=1.0,
        step=0.1,
        key="partial_x0"
    )

    y0 = st.slider(
        "Choose y₀",
        min_value=-1.5,
        max_value=1.5,
        value=0.5,
        step=0.1,
        key="partial_y0"
    )

    direction = st.radio(
        "Differentiate with respect to",
        ["x", "y"],
        horizontal=True,
        key="partial_direction"
    )

    def f(x, y):
        return x**2 + x*y + 2*y**2

    z0 = f(x0, y0)

    if direction == "x":
        slope = 2*x0 + y0
        st.markdown(r"""
We keep $y=y_0$ fixed and vary $x$.

The highlighted curve is the intersection
of the surface with the plane $y=y_0$.
""")
    else:
        slope = x0 + 4*y0
        st.markdown(r"""
We keep $x=x_0$ fixed and vary $y$.

The highlighted curve is the intersection
of the surface with the plane $x=x_0$.
""")

    st.markdown("**Current partial derivative**")

    st.latex(
        rf"\frac{{\partial f}}{{\partial {direction}}}"
        rf"({x0:.1f},{y0:.1f})={slope:.2f}"
    )

    st.markdown(r"""
The partial derivative is the slope
of the tangent line to the selected
cross-sectional curve.
""")


with right:

    # Surface grid

    grid = np.linspace(-2, 2, 65)
    X, Y = np.meshgrid(grid, grid)
    Z = f(X, Y)

    # Cross-sectional curve

    t = np.linspace(-2, 2, 250)

    if direction == "x":
        xs = t
        ys = np.full_like(t, y0)
        center = x0
    else:
        xs = np.full_like(t, x0)
        ys = t
        center = y0

    zs = f(xs, ys)

    # Tangent line along the selected direction

    local_t = np.linspace(
        max(-2, center - 0.75),
        min(2, center + 0.75),
        80
    )

    if direction == "x":
        tangent_x = local_t
        tangent_y = np.full_like(local_t, y0)
    else:
        tangent_x = np.full_like(local_t, x0)
        tangent_y = local_t

    tangent_z = z0 + slope*(local_t - center)

    # 3D figure

    fig = go.Figure()

    fig.add_trace(
        go.Surface(
            x=X,
            y=Y,
            z=Z,
            colorscale=[
                [0.0, "#16354D"],
                [0.5, "#2379A3"],
                [1.0, "#67D5CF"]
            ],
            opacity=0.75,
            showscale=False,
            name="Surface"
        )
    )

    # Highlighted cross-section

    fig.add_trace(
        go.Scatter3d(
            x=xs,
            y=ys,
            z=zs,
            mode="lines",
            line=dict(
                color="#FFB347",
                width=8
            ),
            name="Cross-section"
        )
    )

    # Tangent line

    fig.add_trace(
        go.Scatter3d(
            x=tangent_x,
            y=tangent_y,
            z=tangent_z,
            mode="lines",
            line=dict(
                color="#FF5C7A",
                width=7
            ),
            name="Tangent line"
        )
    )

    # Selected point

    fig.add_trace(
        go.Scatter3d(
            x=[x0],
            y=[y0],
            z=[z0],
            mode="markers",
            marker=dict(
                size=7,
                color="#FFFFFF",
                line=dict(
                    color="#FF5C7A",
                    width=3
                )
            ),
            name="Selected point"
        )
    )

    axis_style = dict(
        backgroundcolor="#0E1117",
        gridcolor="#343A46",
        zerolinecolor="#666666",
        showbackground=True
    )

    fig.update_layout(
        paper_bgcolor="#0E1117",
        font=dict(color="#FFFFFF"),
        height=470,
        margin=dict(l=0, r=0, t=5, b=0),
        showlegend=True,
        legend=dict(
            x=0.01,
            y=0.99,
            bgcolor="rgba(14,17,23,0.6)"
        ),
        scene=dict(
            xaxis=dict(title="x", **axis_style),
            yaxis=dict(title="y", **axis_style),
            zaxis=dict(title="f(x,y)", **axis_style),
            aspectmode="cube",
            camera=dict(
                eye=dict(x=1.6, y=1.6, z=1.1)
            )
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displaylogo": False}
    )

    st.caption(
        "Blue: surface  |  Orange: cross-section  |  "
        "Pink: tangent line"
    )


st.markdown(r"""
Notice that each partial derivative only describes
the behavior of the function along a particular
coordinate direction.

It does not, by itself, describe how the function
changes when several coordinates vary simultaneously.
""")


# ==========================================
# 3. GENERAL DEFINITION IN R^n
# ==========================================

st.divider()

st.header("3. Partial Derivatives in Several Variables")

st.markdown(r"""
The same idea extends naturally to functions
of $n$ variables.

Let $f:U\to\mathbb{R}$, where $U$ is an open
subset of $\mathbb{R}^n$, and let $a\in U$.

We write
""")

st.latex(r"""
a=(a_1,\ldots,a_n).
""")

st.markdown(r"""
To differentiate with respect to the $j$-th
coordinate, we vary only $a_j$ and keep
all other coordinates fixed.

Let $e_j$ denote the $j$-th standard basis
vector of $\mathbb{R}^n$.

Then the **$j$-th partial derivative** is
defined by
""")

st.latex(r"""
\boxed{
\partial_j f(a)=
\lim_{h\to0}
\frac{f(a+he_j)-f(a)}{h},
}
""")

st.markdown(r"""
provided the limit exists and is finite.

Common notations include
""")

st.latex(r"""
\frac{\partial f}{\partial x_j},
\qquad
\partial_j f,
\qquad
f_{x_j}.
""")

st.markdown(r"""
Thus, partial differentiation in $\mathbb{R}^n$
reduces to ordinary differentiation along
a line parallel to one of the coordinate axes.
""")


# ==========================================
# 4. WORKED EXAMPLES
# ==========================================

st.divider()

st.header("4. Worked Examples")

with st.expander(
    "Example 1 — A Function of Two Variables",
    expanded=False
):

    st.markdown(r"""
Consider
""")

    st.latex(r"f(x,y)=x^2+xy+2y^2.")

    st.markdown(r"""
When differentiating with respect to $x$,
we treat $y$ as a constant:
""")

    st.latex(r"""
\boxed{
\frac{\partial f}{\partial x}(x,y)=2x+y.
}
""")

    st.markdown(r"""
Similarly, treating $x$ as a constant,
we obtain
""")

    st.latex(r"""
\boxed{
\frac{\partial f}{\partial y}(x,y)=x+4y.
}
""")


with st.expander(
    "Example 2 — Three Variables (Folland)",
    expanded=False
):

    st.markdown(r"""
Consider the function
""")

    st.latex(r"""
f(x,y,z)=
\frac{e^{3x}\sin(xy)}
{1+5y-7z},
""")

    st.markdown(r"""
defined wherever $1+5y-7z\neq0$.

Differentiating with respect to each variable,
while keeping the remaining variables fixed,
gives the following partial derivatives.
""")

    st.markdown("**With respect to $x$:**")

    st.latex(r"""
\frac{\partial f}{\partial x}
=
\frac{
e^{3x}\left(3\sin(xy)+y\cos(xy)\right)
}{
1+5y-7z
}.
""")

    st.markdown("**With respect to $y$:**")

    st.latex(r"""
\frac{\partial f}{\partial y}
=
\frac{
e^{3x}\left[
x(1+5y-7z)\cos(xy)-5\sin(xy)
\right]
}{
(1+5y-7z)^2
}.
""")

    st.markdown("**With respect to $z$:**")

    st.latex(r"""
\frac{\partial f}{\partial z}
=
\frac{
7e^{3x}\sin(xy)
}{
(1+5y-7z)^2
}.
""")

    st.markdown(r"""
This is Example 1 from Folland, Section 2.2.
""")


# ==========================================
# 5. ARE PARTIAL DERIVATIVES ENOUGH?
# ==========================================

st.divider()

st.header("5. Are Partial Derivatives Enough?")

st.markdown(r"""
Partial derivatives describe the variation
of a function along the coordinate directions.

But what happens when several variables
change simultaneously?

**Do the existence of all partial derivatives
at a point guarantee that the function
behaves continuously near that point?**

The answer is **no**.

Folland illustrates this with the following
counterexample.
""")

st.markdown("### Example — Partial Derivatives Without Continuity")

st.markdown(r"""
Consider the function
""")

st.latex(r"""
f(x,y)=
\begin{cases}
\displaystyle\frac{xy}{x^2+y^2},
& (x,y)\neq(0,0),\\[8pt]
0,&(x,y)=(0,0).
\end{cases}
""")

st.markdown(r"""
We will show that both partial derivatives
exist at the origin, even though $f$ is
not continuous there.
""")


with st.expander(
    "Proof — Partial Derivatives Without Continuity",
    expanded=False
):

    st.markdown(r"""
**Step 1 — Compute the partial derivatives at the origin.**

Along the $x$-axis, we have
""")

    st.latex(r"""
f(h,0)=0.
""")

    st.markdown(r"""
Therefore,
""")

    st.latex(r"""
\begin{aligned}
\frac{\partial f}{\partial x}(0,0)
&=
\lim_{h\to0}
\frac{f(h,0)-f(0,0)}{h}\\[6pt]
&=0.
\end{aligned}
""")

    st.markdown(r"""
Similarly, along the $y$-axis,
""")

    st.latex(r"""
f(0,h)=0,
""")

    st.markdown(r"""
and hence
""")

    st.latex(r"""
\boxed{
\frac{\partial f}{\partial y}(0,0)=0.
}
""")

    st.markdown(r"""
Thus, both partial derivatives exist
at $(0,0)$ and are equal to zero.
""")

    st.divider()

    st.markdown(r"""
**Step 2 — Examine continuity at the origin.**

Now approach the origin along the line $y=x$.

For $t\neq0$,
""")

    st.latex(r"""
\begin{aligned}
f(t,t)
&=\frac{t^2}{t^2+t^2}\\[6pt]
&=\frac12.
\end{aligned}
""")

    st.markdown(r"""
Therefore,
""")

    st.latex(r"""
\lim_{t\to0}f(t,t)=\frac12.
""")

    st.markdown(r"""
But $f(0,0)=0$, and along the $x$-axis,
$f(t,0)=0$.

Consequently, the values of $f$ approach
different limits along different paths.

Thus, $f$ is not continuous at the origin.
""")

    st.divider()

    st.markdown(r"""
**Conclusion**

We have constructed a function for which
""")

    st.latex(r"""
\boxed{
\frac{\partial f}{\partial x}(0,0)
=
\frac{\partial f}{\partial y}(0,0)
=0,
}
""")

    st.markdown(r"""
yet $f$ is not continuous at $(0,0)$.

This shows that the existence of partial
derivatives alone does not control the
behavior of a function in every direction.

$\square$
""")


# ==========================================
# FINAL OBSERVATION
# ==========================================

st.markdown(r"""
The example reveals a fundamental limitation
of partial differentiation.

Partial derivatives examine the function
along individual coordinate directions,
whereas the local behavior of a multivariable
function depends on how its variables
change together.

**We therefore need a stronger notion
of differentiability.**

In the next section, we will develop this
notion by extending the local linear
approximation approach from single-variable
calculus to functions on $\mathbb{R}^n$.
""")

st.caption(
    "Reference: Gerald B. Folland, Advanced Calculus, "
    "2nd Edition, Section 2.2, pp. 53–55."
)
