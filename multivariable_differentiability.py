import streamlit as st
import numpy as np
import plotly.graph_objects as go

# =========================================================
# DIFFERENTIABILITY IN SEVERAL VARIABLES
# Based on Folland, Advanced Calculus, 2nd ed., Section 2.2
# =========================================================

st.title("Differentiability in Several Variables")

st.markdown(r"""
In one variable, we learned that differentiability is equivalent
to the existence of a sufficiently accurate local affine approximation.

We now extend this idea to functions of several variables.

The central question is: **what should a local linear approximation
look like when the input is a vector?**
""")

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

st.divider()


# ==========================================
# 1. WHY PARTIAL DERIVATIVES ARE NOT ENOUGH
# ==========================================

st.header("1. From Partial Derivatives to Differentiability")

st.markdown(r"""
A partial derivative measures the variation of a function along
**one coordinate direction**, while the other coordinates are fixed.

In the previous chapter, we saw that all partial derivatives can exist
at a point even when the function is not continuous there. Thus,
partial derivatives alone do not describe the function's full local behavior.

We need a notion that accounts for **all sufficiently small vector
increments**, not just increments parallel to the coordinate axes.

Our starting point will be the local linear approximation developed
in single-variable calculus.
""")

st.divider()


# ==========================================
# 2. LOCAL LINEAR APPROXIMATION
# ==========================================

st.header("2. Local Linear Approximation in $\\mathbb{R}^n$")

st.markdown(r"""
Let $U\subseteq\mathbb{R}^n$ be open, let $a\in U$, and consider
$f:U\to\mathbb{R}$.

In one variable, our approximating line had the form
$l(x_0+h)=f(x_0)+mh$.

The term $mh$ is linear in the increment $h$.

For several variables, the increment is a vector
$h=(h_1,\ldots,h_n)$.

We therefore look for an **affine function**
whose increment is given by a linear map
$L:\mathbb{R}^n\to\mathbb{R}$.

Why can every such linear map be written as a dot product?

Since $h=h_1e_1+\cdots+h_ne_n$, linearity gives
""")

st.latex(r"""
\begin{aligned}
L(h)
&=h_1L(e_1)+\cdots+h_nL(e_n)\\
&=c_1h_1+\cdots+c_nh_n\\
&=c\cdot h,
\end{aligned}
""")

st.markdown(r"""
where $c=(c_1,\ldots,c_n)$ and $c_j=L(e_j)$.

Thus, the dot product is **not an arbitrary choice**:
it represents every linear map from $\mathbb{R}^n$
to $\mathbb{R}$.

Consider an affine approximating function
""")

st.latex(r"l(x)=b+c\cdot x.")

st.markdown(r"""
**First condition.**

As in one variable, the approximating function
must pass through the point $(a,f(a))$:
""")

st.latex(r"l(a)=f(a).")

st.markdown(r"""
This forces
""")

st.latex(r"b=f(a)-c\cdot a,")

st.markdown(r"""
so that
""")

st.latex(r"""
\begin{aligned}
l(x)
&=b+c\cdot x\\
&=f(a)-c\cdot a+c\cdot x.
\end{aligned}
""")

st.markdown(r"""
Substituting
""")

st.latex(r"x=a+h,")

st.markdown(r"""
we obtain
""")

st.latex(r"""
\begin{aligned}
l(a+h)
&=f(a)-c\cdot a+c\cdot(a+h)\\
&=f(a)+c\cdot h.
\end{aligned}
""")

st.markdown(r"""
Therefore,
""")

st.latex(r"""
\boxed{
l(a+h)=f(a)+c\cdot h.
}
""")

st.markdown(r"""
**Second condition.**

The approximation error must become negligible
compared with the **size of the input increment**.

Define
""")

st.latex(r"""
E(h)=f(a+h)-f(a)-c\cdot h.
""")

st.markdown(r"""
Because $h$ is now a vector, we measure its size
using the Euclidean norm
""")

st.latex(r"""
\|h\|=\sqrt{h_1^2+\cdots+h_n^2}.
""")

st.markdown(r"""
We require the error to vanish faster than $\|h\|$:
""")

st.latex(r"""
\boxed{
\lim_{h\to0}\frac{E(h)}{\|h\|}=0.
}
""")

st.markdown(r"""
Here $h\to0$ means that the **entire vector**
approaches the zero vector, without restricting
its direction.

This is what makes the condition stronger than
merely knowing the partial derivatives.
""")

st.divider()


# ==========================================
# 3. FORMAL DEFINITION AND TANGENT PLANE
# ==========================================

st.header("3. Definition of Differentiability")

st.markdown("### Definition")

st.markdown(r"""
Let $f:U\to\mathbb{R}$, where
$U\subseteq\mathbb{R}^n$ is open,
and let $a\in U$.

We say that $f$ is **differentiable at $a$**
if there exists a vector $c\in\mathbb{R}^n$
such that
""")

st.latex(r"""
\boxed{
\lim_{h\to0}
\frac{f(a+h)-f(a)-c\cdot h}{\|h\|}=0.
}
""")

st.markdown(r"""
Equivalently, there exists a remainder function
$E$ for which
""")

st.latex(r"""
\boxed{
\begin{gathered}
f(a+h)=f(a)+c\cdot h+E(h),\\[5pt]
\displaystyle\lim_{h\to0}
\frac{E(h)}{\|h\|}=0.
\end{gathered}
}
""")

st.markdown(r"""
We will prove below that $c$ is uniquely determined
and equals the gradient $\nabla f(a)$.

When $n=2$, the approximating affine function
describes a **tangent plane** to the surface
$z=f(x,y)$.
""")


# ==========================================
# INTERACTIVE TANGENT PLANE
# ==========================================

st.markdown("### Interactive Visualization — The Tangent Plane")

st.markdown(r"""
Consider the function
""")

st.latex(r"f(x,y)=x^2+y^2.")

st.markdown(r"""
Choose a point and change the size of the
displayed neighborhood to compare the surface
with its tangent plane.
""")

left, right = st.columns([0.85, 1.3], gap="large")

with left:

    x0 = st.slider(
        "Choose x₀",
        min_value=-1.5,
        max_value=1.5,
        value=1.0,
        step=0.1,
        key="mv_diff_x0"
    )

    y0 = st.slider(
        "Choose y₀",
        min_value=-1.5,
        max_value=1.5,
        value=0.5,
        step=0.1,
        key="mv_diff_y0"
    )

    radius = st.slider(
        "Neighborhood radius",
        min_value=0.2,
        max_value=1.5,
        value=1.1,
        step=0.1,
        key="mv_diff_radius"
    )

    z0 = x0**2 + y0**2

    cx = 2*x0
    cy = 2*y0

    st.markdown("**Current approximation**")

    st.latex(
        rf"\nabla f({x0:.1f},{y0:.1f})"
        rf"=({cx:.1f},{cy:.1f})"
    )

    st.latex(rf"f(a)={z0:.2f}")

    st.markdown(r"""
The blue surface and orange plane agree at
the selected point.

As the neighborhood shrinks, their difference
becomes small relative to the horizontal displacement.
""")


with right:

    # Surface grid around the selected point

    grid = np.linspace(-radius, radius, 65)

    H1, H2 = np.meshgrid(grid, grid)

    X = x0 + H1
    Y = y0 + H2

    # Original surface

    Z = X**2 + Y**2

    # Tangent plane

    P = z0 + cx*H1 + cy*H2

    fig = go.Figure()

    # Original surface

    fig.add_trace(
        go.Surface(
            x=X,
            y=Y,
            z=Z,
            colorscale=[
                [0, "#153E68"],
                [0.5, "#247FAA"],
                [1, "#69D1EE"]
            ],
            opacity=0.86,
            showscale=False,
            name="Surface",
            showlegend=False
        )
    )

    # Tangent plane

    fig.add_trace(
        go.Surface(
            x=X,
            y=Y,
            z=P,
            colorscale=[
                [0, "#FFB347"],
                [1, "#FFB347"]
            ],
            opacity=0.56,
            showscale=False,
            name="Tangent plane",
            showlegend=False
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
                size=6,
                color="#FF5C7A"
            ),
            name="Selected point"
        )
    )

    # Dark theme

    axes = dict(
        backgroundcolor="#0E1117",
        gridcolor="#353A43",
        zerolinecolor="#6E7380",
        showbackground=True
    )

    fig.update_layout(
        paper_bgcolor="#0E1117",
        font=dict(color="white"),
        height=445,
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
        scene=dict(
            xaxis=dict(title="x", **axes),
            yaxis=dict(title="y", **axes),
            zaxis=dict(title="z", **axes),
            aspectmode="manual",
            aspectratio=dict(
                x=1,
                y=1,
                z=0.75
            ),
            camera=dict(
                eye=dict(
                    x=1.6,
                    y=1.5,
                    z=1.0
                )
            )
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displaylogo": False}
    )

    st.caption(
        "Blue: surface  |  "
        "Orange: tangent plane  |  "
        "Pink: selected point"
    )


# ==========================================
# EXAMPLE — REMAINDER CONDITION
# ==========================================

st.markdown(r"""
For this example, let $a=(x_0,y_0)$ and $h=(u,v)$.

Expanding the function at $a+h$ yields
""")

st.latex(r"""
\begin{aligned}
f(a+h)
&=(x_0+u)^2+(y_0+v)^2\\
&=f(a)+2x_0u+2y_0v+u^2+v^2.
\end{aligned}
""")

st.markdown(r"""
Thus $c=(2x_0,2y_0)$ and
$E(h)=u^2+v^2=\|h\|^2$.

Consequently,
""")

st.latex(r"""
\frac{E(h)}{\|h\|}
=
\|h\|
\longrightarrow0.
""")

st.markdown(r"""
Therefore, this function is differentiable
at every point.

The approximation is exact up to an error
of second order in the increment.
""")

st.divider()


# ==========================================
# 4. THE GRADIENT AND UNIQUENESS
# FOLLAND 2.17
# ==========================================

st.header("4. The Gradient and Uniqueness")

st.markdown("### Theorem — Folland 2.17")

st.markdown(r"""
If $f:U\to\mathbb{R}$ is differentiable
at $a\in U$, then all partial derivatives
$\partial_j f(a)$ exist.

Moreover, the vector $c$ in the local
linear approximation is uniquely determined
and satisfies
""")

st.latex(r"""
\boxed{
c=\nabla f(a)
=
\bigl(
\partial_1f(a),\ldots,\partial_nf(a)
\bigr).
}
""")


with st.expander(
    "Proof — The Gradient and Uniqueness",
    expanded=False
):

    st.markdown(r"""
**Proof.**

By differentiability, there exist
$c\in\mathbb{R}^n$ and $E$ such that
""")

    st.latex(r"""
f(a+h)=f(a)+c\cdot h+E(h),
""")

    st.markdown(r"""
where
""")

    st.latex(r"""
\lim_{h\to0}
\frac{E(h)}{\|h\|}=0.
""")

    st.markdown(r"""
Fix $j\in\{1,\ldots,n\}$, and let $e_j$
denote the $j$-th standard basis vector
of $\mathbb{R}^n$.

Choose the increment $h=te_j$, where
$t\in\mathbb{R}$ and $t\neq0$.

Since $c\cdot(te_j)=c_jt$, substituting
into the remainder representation gives
""")

    st.latex(r"""
f(a+te_j)=f(a)+c_jt+E(te_j).
""")

    st.markdown(r"""
Subtracting $f(a)$ and dividing by $t$,
we obtain
""")

    st.latex(r"""
\frac{f(a+te_j)-f(a)}{t}
=
c_j+\frac{E(te_j)}{t}.
""")

    st.markdown(r"""
Now we examine the remainder term.

Since $\|e_j\|=1$, we have
$\|te_j\|=|t|$, and therefore
$te_j\to0$ as $t\to0$.

By the remainder condition,
""")

    st.latex(r"""
\lim_{t\to0}
\frac{E(te_j)}{\|te_j\|}=0.
""")

    st.markdown(r"""
Moreover, for $t\neq0$,
""")

    st.latex(r"""
\begin{aligned}
\left|\frac{E(te_j)}{t}\right|
&=\frac{|E(te_j)|}{|t|}\\[6pt]
&=\frac{|E(te_j)|}{\|te_j\|}\\[6pt]
&=\left|\frac{E(te_j)}{\|te_j\|}\right|\\[6pt]
&\longrightarrow0
\qquad(t\to0).
\end{aligned}
""")

    st.markdown(r"""
Consequently,
""")

    st.latex(r"""
\lim_{t\to0}\frac{E(te_j)}{t}=0.
""")

    st.markdown(r"""
Taking the limit in the difference quotient,
we conclude that
""")

    st.latex(r"""
\begin{aligned}
\partial_j f(a)
&=\lim_{t\to0}
\frac{f(a+te_j)-f(a)}{t}\\[6pt]
&=c_j.
\end{aligned}
""")

    st.markdown(r"""
Since this is true for every $j$, we have
$c=\nabla f(a)$.

The components of $c$ are uniquely determined
by the partial derivatives, so the vector $c$
is unique.

$\square$
""")

st.markdown(r"""
In particular, **differentiability implies
the existence of all partial derivatives**.

However, the converse is false, as we saw
in the previous chapter.
""")

st.divider()


# ==========================================
# 5. DIFFERENTIABILITY IMPLIES CONTINUITY
# FOLLAND 2.18
# ==========================================

st.header("5. Differentiability Implies Continuity")

st.markdown("### Theorem — Folland 2.18")

st.markdown(r"""
If $f:U\to\mathbb{R}$ is differentiable
at $a\in U$, then $f$ is continuous at $a$.
""")


with st.expander(
    "Proof — Differentiability Implies Continuity",
    expanded=False
):

    st.markdown(r"""
**Proof.**

Using the remainder representation, we have
""")

    st.latex(r"""
f(a+h)-f(a)
=
\nabla f(a)\cdot h+E(h).
""")

    st.markdown(r"""
The linear term tends to zero by the
Cauchy–Schwarz inequality:
""")

    st.latex(r"""
|\nabla f(a)\cdot h|
\leq
\|\nabla f(a)\|\,\|h\|
\longrightarrow0.
""")

    st.markdown(r"""
Also, for every sufficiently small
$h\neq0$,
""")

    st.latex(r"""
|E(h)|
=
\|h\|
\left|
\frac{E(h)}{\|h\|}
\right|
\longrightarrow0.
""")

    st.markdown(r"""
Therefore,
""")

    st.latex(r"""
f(a+h)-f(a)\longrightarrow0.
""")

    st.markdown(r"""
This means precisely that $f$ is
continuous at $a$.

$\square$
""")

st.divider()


# ==========================================
# 6. SUFFICIENT CONDITION
# FOLLAND 2.19
# ==========================================

st.header("6. A Sufficient Condition for Differentiability")

st.markdown(r"""
We know that the existence of partial derivatives
at a point is **necessary but not sufficient**
for differentiability.

A useful additional assumption gives
a sufficient condition.
""")

st.markdown("### Theorem — Folland 2.19")

st.markdown(r"""
Let $f:U\to\mathbb{R}$, with
$U\subseteq\mathbb{R}^n$ open, and let $a\in U$.

Suppose that all the partial derivatives
$\partial_jf$ exist in a neighborhood of $a$
and are continuous at $a$.

Then **$f$ is differentiable at $a$**.
""")


with st.expander(
    "Proof — Continuous Partial Derivatives",
    expanded=False
):

    st.markdown(r"""
**Proof.**

We first consider $n=2$, following Folland's
argument.

Write $a=(a_1,a_2)$ and $h=(h_1,h_2)$.

The key idea is to change the coordinates
**one at a time**:
""")

    st.latex(r"""
\begin{aligned}
f(a+h)-f(a)
&=f(a_1+h_1,a_2+h_2)\\
&\quad-f(a_1,a_2+h_2)\\
&\quad+f(a_1,a_2+h_2)\\
&\quad-f(a_1,a_2).
\end{aligned}
""")

    st.markdown(r"""
Apply the one-variable mean value theorem
to each difference, holding the other
coordinate fixed.

For suitable $\theta_1,\theta_2\in[0,1]$,
we obtain
""")

    st.latex(r"""
\begin{aligned}
f(a+h)-f(a)
&=\partial_1 f(
a_1+\theta_1h_1,a_2+h_2
)h_1\\
&\quad+\partial_2 f(
a_1,a_2+\theta_2h_2
)h_2.
\end{aligned}
""")

    
    st.markdown(r"""
Subtracting the candidate linear term
$\nabla f(a)\cdot h = \partial_1 f(a) h_1 + \partial_2 f(a) h_2$ from both sides, we obtain
""")

    st.latex(r"""
\begin{aligned}
&f(a+h)-f(a)-\nabla f(a)\cdot h
=
\partial_1 f(a_1+\theta_1h_1,a_2+h_2)h_1
+
\partial_2 f(a_1,a_2+\theta_2h_2)h_2
-
\partial_1 f(a)h_1
-
\partial_2 f(a)h_2.
\end{aligned}
""")

    st.markdown(r"""
Grouping the terms corresponding to each coordinate,
the remainder becomes
""")

    st.latex(r"""
\begin{aligned}
E(h)
={}&
\left[
\partial_1 f(a_1+\theta_1h_1,a_2+h_2)
-\partial_1 f(a)
\right]h_1\\[8pt]
&+
\left[
\partial_2 f(a_1,a_2+\theta_2h_2)
-\partial_2 f(a)
\right]h_2.
\end{aligned}
""")

    st.markdown(r"""
For convenience, denote the two bracketed expressions
by $A_1(h)$ and $A_2(h)$, respectively. Then
""")

    st.latex(r"""
E(h)=A_1(h)h_1+A_2(h)h_2.
""")


    st.markdown(r"""
As $h\to0$, both evaluation points
approach $a$.

Continuity of the partial derivatives
at $a$ therefore gives
""")

    st.latex(r"""
A_1(h)\to0,
\qquad
A_2(h)\to0.
""")

    st.markdown(r"""
Moreover, $|h_j|\leq\|h\|$.

Thus, for $h\neq0$,
""")

    st.latex(r"""
\begin{aligned}
\left|\frac{E(h)}{\|h\|}\right|
&=\frac{|A_1(h)h_1+A_2(h)h_2|}{\|h\|}\\[8pt]
&\leq
\frac{|A_1(h)|\,|h_1|+|A_2(h)|\,|h_2|}{\|h\|}\\[8pt]
&\leq
\frac{|A_1(h)|\,\|h\|+|A_2(h)|\,\|h\|}{\|h\|}\\[8pt]
&=|A_1(h)|+|A_2(h)|\\[8pt]
&\longrightarrow 0
\qquad (h\to0).
\end{aligned}
""")

    st.markdown(r"""
Hence $f$ is differentiable at $a$.

**Generalization to $\mathbb{R}^n$.**

For general $n$, we proceed similarly, applying the
one-variable mean value theorem successively
to each coordinate.

The remainder then takes the form
""")

    st.latex(r"""
E(h)=\sum_{j=1}^{n}A_j(h)h_j,
\qquad A_j(h)\longrightarrow0
\quad (h\to0).
""")

    st.markdown(r"""
Since $|h_j|\leq\|h\|$ for every $j$, we obtain
""")

    st.latex(r"""
\left|\frac{E(h)}{\|h\|}\right|
\leq\sum_{j=1}^{n}|A_j(h)|
\longrightarrow0.
""")

    st.markdown(r"""
Thus, the differentiability condition holds
in $\mathbb{R}^n$ as well.

$\square$
""")



# ==========================================
# CONCLUSION
# ==========================================

st.markdown(r"""
A function whose first-order partial derivatives
exist and are continuous throughout an open
set $U$ is called **continuously differentiable**,
or **of class $C^1(U)$**.

We have established the chain of implications
""")

st.latex(r"""
\boxed{
C^1
\ \Longrightarrow\
\text{differentiable}
\ \Longrightarrow\
\text{partial derivatives exist}.
}
""")

st.markdown(r"""
Neither implication is reversible in general.

The next chapter will explore what the gradient
tells us about changes in **arbitrary directions**.
""")

st.caption(
    "Reference: Gerald B. Folland, Advanced Calculus, "
    "2nd Edition, Section 2.2, pp. 55–58."
)
