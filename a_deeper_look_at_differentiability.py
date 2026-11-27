import streamlit as st

# ==========================================
# A DEEPER LOOK AT DIFFERENTIABILITY
# Based on Folland, Advanced Calculus, §2.1
# ==========================================

st.title("A Deeper Look at Differentiability")

st.markdown(r"""
So far, we have understood the derivative as the limit
of secant slopes.

However, there is another, deeper way to understand
differentiability.

**Instead of starting with the derivative, we ask:**

What does it mean for a function to be well approximated
by a straight line near a given point?
""")

st.divider()


# ==========================================
# 1. LOCAL LINEAR APPROXIMATION
# ==========================================

st.header("1. Differentiability as Local Linear Approximation")

st.markdown(r"""
Let $f:\mathbb{R}\to\mathbb{R}$ be a function,
and suppose we want to approximate it near a point $x_0$.

We seek a straight line that provides a good
approximation of $f$ near this point.

To do so, consider a function of the form
""")

st.latex(r"l(x)=mx+b.")

st.markdown(r"""
where $m$ is the slope and $b$ is the y-intercept.

Strictly speaking, this is an affine function,
although it is often called a linear function
in elementary calculus.

**Our goal is to determine whether there exists
a suitable value of $m$ for which this line
approximates $f$ sufficiently well near $x_0$.**

To make this precise, we impose two conditions.
""")


# ==========================================
# 2. FIRST CONDITION
# ==========================================

import numpy as np
import matplotlib.pyplot as plt

st.header("2. First Condition — Passing Through the Point")

left, right = st.columns([1.1, 1], gap="large")

with left:

    st.markdown(r"""
First, we require the approximating line to pass
through the point $(x_0,f(x_0))$.

In other words,
""")

    st.latex(r"\boxed{l(x_0)=f(x_0).}")

    st.markdown(r"""
Since $l(x)=mx+b$, we obtain
""")

    st.latex(r"mx_0+b=f(x_0).")

    st.markdown("Solving for $b$ gives")

    st.latex(r"b=f(x_0)-mx_0.")

    st.markdown(r"""
Substituting this into the equation of the line,
we obtain
""")

    st.latex(r"""
\boxed{l(x)=f(x_0)+m(x-x_0).}
""")

    st.markdown(r"""
It is convenient to introduce the increment
$h=x-x_0$, so that $x=x_0+h$.

The approximating line can then be written as
""")

    st.latex(r"""
\boxed{l(x_0+h)=f(x_0)+mh.}
""")


with right:

    st.markdown("**Interactive Visualization**")

    st.markdown(r"""
Consider the function $f(x)=x^2$.

Choose a point $x_0$ and change the slope $m$
of the approximating line.
""")

    x0 = st.slider(
        "Choose the point x₀",
        min_value=-1.5,
        max_value=1.5,
        value=1.0,
        step=0.1,
        key="linear_approx_x0"
    )

    m = st.slider(
        "Choose the slope m",
        min_value=-4.0,
        max_value=4.0,
        value=0.0,
        step=0.1,
        key="linear_approx_m"
    )

    # Function and approximating line

    x = np.linspace(-2, 2, 600)

    def f(x):
        return x**2

    y = f(x)
    y0 = f(x0)

    line = y0 + m * (x - x0)

    # Dark-themed matplotlib figure

    fig, ax = plt.subplots(figsize=(6, 4.4))

    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#0E1117")

    # Original function

    ax.plot(
        x, y,
        color="#36C5F0",
        linewidth=2.8,
        label=r"$f(x)=x^2$"
    )

    # Approximating line

    ax.plot(
        x, line,
        color="#FFB347",
        linewidth=2.5,
        label=r"$l(x)$"
    )

    # Selected point

    ax.scatter(
        [x0], [y0],
        color="#FF5C7A",
        s=85,
        zorder=5
    )

    ax.annotate(
        rf"$({x0:.1f},\,{y0:.2f})$",
        xy=(x0, y0),
        xytext=(8, 12),
        textcoords="offset points",
        color="white",
        fontsize=10
    )

    # Guide line marking x0

    ax.plot(
        [x0, x0],
        [0, y0],
        linestyle=":",
        color="#AAAAAA",
        alpha=0.6
    )

    # Coordinate axes

    ax.axhline(
        0,
        color="white",
        linewidth=0.8,
        alpha=0.45
    )

    ax.axvline(
        0,
        color="white",
        linewidth=0.8,
        alpha=0.45
    )

    # Styling

    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 5)

    ax.set_xlabel("x", color="white")
    ax.set_ylabel("y", color="white")

    ax.tick_params(colors="white")

    for spine in ax.spines.values():
        spine.set_color("#555555")

    ax.grid(
        True,
        alpha=0.12,
        color="white"
    )

    ax.legend(
        facecolor="#0E1117",
        edgecolor="#444444",
        labelcolor="white",
        loc="upper center",
        fontsize=10
    )

    fig.tight_layout()

    st.pyplot(fig, use_container_width=True)

    plt.close(fig)

    st.latex(r"""
l(x)=f(x_0)+m(x-x_0)
""")

    st.caption(
        f"x₀ = {x0:.2f}  |  "
        f"f(x₀) = {y0:.2f}  |  "
        f"m = {m:.2f}"
    )


# ==========================================
# CONCLUSION OF THE FIRST CONDITION
# ==========================================

st.markdown(r"""
**Notice that this condition does not determine $m$.**

Every choice of $m$ produces a different line passing
through the point $(x_0,f(x_0))$.

Therefore, passing through the point is not sufficient
to identify the correct local approximation.

We need a second condition.
""")


# ==========================================
# 3. SECOND CONDITION
# ==========================================

st.header("3. Second Condition — The Approximation Error")

st.markdown(r"""
Passing through the point $(x_0,f(x_0))$ is not enough
to determine a suitable approximating line. We also
need to specify how accurately the line should
approximate the function near $x_0$.

To measure the accuracy of the approximation,
we consider the difference between the function
and the approximating line:
""")

st.latex(r"f(x)-l(x).")

st.markdown(r"""
This difference is called the **approximation error**.

Since $l(x_0)=f(x_0)$, the error is zero at $x_0$.
Moreover, if $f$ is continuous at $x_0$, the error
approaches zero as $x\to x_0$, regardless of the
chosen slope $m$.

Therefore, requiring the error merely to approach
zero is not sufficient to identify the desired line.

**We impose a stronger condition:** the approximation
error must become negligible compared with the
displacement $x-x_0$ as $x$ approaches $x_0$.

Mathematically, we require
""")

st.latex(r"""
\boxed{
\lim_{x\to x_0}
\frac{f(x)-l(x)}{x-x_0}=0.
}
""")


st.markdown(r"""
Using the increment $h=x-x_0$, this becomes
""")

st.latex(r"""
\boxed{
\lim_{h\to0}
\frac{f(x_0+h)-l(x_0+h)}{h}=0.
}
""")

st.markdown(r"""
Recall that our approximating line is given by
$l(x_0+h)=f(x_0)+mh$.

We can therefore write the following exact identity:
""")

st.latex(r"""
\begin{aligned}
f(x_0+h)
&=f(x_0)+mh\\
&\quad+\bigl(f(x_0+h)-f(x_0)-mh\bigr).
\end{aligned}
""")

st.markdown(r"""
The expression in parentheses is precisely
the approximation error. Let us denote it by $E(h)$:
""")

st.latex(r"""
E(h)=f(x_0+h)-f(x_0)-mh.
""")

st.markdown(r"""
Thus, we obtain
""")

st.latex(r"""
\boxed{
f(x_0+h)=f(x_0)+mh+E(h).
}
""")

st.markdown(r"""
By our **second condition**, the approximation error
must approach zero faster than the increment $h$.

In other words,
""")

st.latex(r"""
\boxed{
\lim_{h\to0}\frac{E(h)}{h}=0.
}
""")

# ==========================================
# 4. EQUIVALENT CHARACTERIZATIONS
# ==========================================

st.divider()

st.header("4. Equivalent Characterizations of Differentiability")


st.markdown("### Theorem")

st.markdown(r"""
Let $f$ be a real-valued function defined
on an open interval containing $x_0$.

The following statements are equivalent:

**(i)** The limit
""")

st.latex(r"""
\lim_{h\to0}
\frac{f(x_0+h)-f(x_0)}{h}
""")

st.markdown(r"""
exists and is finite.

**(ii)** There exist a real number $m$ and a remainder
function $E$ such that, for all sufficiently small $h$,
""")

st.latex(r"""
f(x_0+h)=f(x_0)+mh+E(h)
""")

st.markdown(r"""
and
""")

st.latex(r"""
\lim_{h\to0}\frac{E(h)}{h}=0.
""")

st.markdown(r"""
Moreover, whenever these conditions hold,
the coefficient $m$ is uniquely determined and
""")

st.latex(r"""
\boxed{m=f'(x_0).}
""")


# ==========================================
# PURPLE EXPANDER STYLING
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
# PROOF
# ==========================================

with st.expander("Proof — Equivalence of the Two Definitions",
                 expanded=False):

    st.markdown(r"""
### Proof

We prove both implications.

**(i) $\Rightarrow$ (ii)**

Assume that $f$ is differentiable at $x_0$
in the usual sense. Then
""")

    st.latex(r"""
\lim_{h\to0}
\frac{f(x_0+h)-f(x_0)}{h}
=f'(x_0).
""")

    st.markdown(r"""
Choose
""")

    st.latex(r"m=f'(x_0)")

    st.markdown(r"""
and define the remainder function by
""")

    st.latex(r"""
E(h)=f(x_0+h)-f(x_0)-f'(x_0)h.
""")

    st.markdown(r"""
By construction,
""")

    st.latex(r"""
f(x_0+h)=f(x_0)+mh+E(h).
""")

    st.markdown(r"""
It remains to verify that $E(h)/h\to0$.
For $h\neq0$,
""")

    st.latex(r"""
\frac{E(h)}{h}
=
\frac{f(x_0+h)-f(x_0)}{h}
-f'(x_0).
""")

    st.markdown(r"""
Taking the limit as $h\to0$, we obtain
""")

    st.latex(r"""
\begin{aligned}
\lim_{h\to0}\frac{E(h)}{h}
&=
\lim_{h\to0}
\frac{f(x_0+h)-f(x_0)}{h}
-f'(x_0)\\[6pt]
&=f'(x_0)-f'(x_0)\\
&=0.
\end{aligned}
""")

    st.markdown(r"""
Therefore, condition (ii) holds.
""")

    st.divider()

    st.markdown(r"""
**(ii) $\Rightarrow$ (i)**

Conversely, suppose that there exist
$m\in\mathbb{R}$ and a function $E$ such that
""")

    st.latex(r"""
f(x_0+h)=f(x_0)+mh+E(h)
""")

    st.markdown(r"""
and
""")

    st.latex(r"""
\lim_{h\to0}\frac{E(h)}{h}=0.
""")

    st.markdown(r"""
Subtracting $f(x_0)$ from both sides
and dividing by $h\neq0$ gives
""")

    st.latex(r"""
\frac{f(x_0+h)-f(x_0)}{h}
=
m+\frac{E(h)}{h}.
""")

    st.markdown(r"""
Taking the limit as $h\to0$, we obtain
""")

    st.latex(r"""
\begin{aligned}
\lim_{h\to0}
\frac{f(x_0+h)-f(x_0)}{h}
&=
m+\lim_{h\to0}\frac{E(h)}{h}\\[6pt]
&=m.
\end{aligned}
""")

    st.markdown(r"""
Thus, the derivative exists and
""")

    st.latex(r"""
\boxed{f'(x_0)=m.}
""")

    st.markdown(r"""
Since the derivative is uniquely determined,
the coefficient $m$ must also be unique.

This completes the proof of the equivalence.
$\square$
""")


# ==========================================
# CONCLUSION
# ==========================================

st.markdown(r"""
The theorem shows that **differentiability can be
understood in two equivalent ways**:

- As the existence of a finite limit of difference quotients.
- As the existence of a local affine approximation whose
  error is negligible compared with the increment.

These two perspectives describe exactly the same
mathematical property.
""")


# ==========================================
# 5. THE CHAIN RULE
# ==========================================

st.divider()

st.header("5. The Chain Rule")

st.markdown(r"""
Having established the equivalence between the classical
definition of differentiability and its characterization
through local linear approximation, we can now use
this alternative perspective to prove the **Chain Rule**.

The key idea is to compose the linear approximations
of two differentiable functions and show that the
resulting remainder still satisfies the required condition.
""")


st.markdown("### Theorem")

st.markdown(r"""
Let $g$ be differentiable at $x_0$, and let $f$ be
differentiable at $g(x_0)$.

Then the composition $f\circ g$ is differentiable
at $x_0$, and
""")

st.latex(r"""
\boxed{
(f\circ g)'(x_0)
=
f'(g(x_0))g'(x_0).
}
""")


# ==========================================
# PROOF — CHAIN RULE
# ==========================================

with st.expander("Proof — The Chain Rule", expanded=False):

    st.markdown(r"""
### Proof

We use the characterization of differentiability
in terms of local linear approximation and
remainder terms.

**Step 1 — Express both functions using remainder terms.**

Since $g$ is differentiable at $x_0$, we can write
""")

    st.latex(r"""
g(x_0+h)
=
g(x_0)+g'(x_0)h+E_g(h),
""")

    st.markdown(r"""
where
""")

    st.latex(r"""
\lim_{h\to0}\frac{E_g(h)}{h}=0.
""")

    st.markdown(r"""
Similarly, since $f$ is differentiable at
$b=g(x_0)$, we have
""")

    st.latex(r"""
f(b+k)
=
f(b)+f'(b)k+E_f(k),
""")

    st.markdown(r"""
where
""")

    st.latex(r"""
\lim_{k\to0}\frac{E_f(k)}{k}=0.
""")

    st.markdown(r"""
These are precisely the remainder-term
representations established in the previous section.
""")

    st.divider()

    st.markdown(r"""
**Step 2 — Substitute one approximation into the other.**

Our goal is to study the composition
$f(g(x_0+h))$.

To obtain this expression, set
""")

    st.latex(r"""
k=k(h)=g(x_0+h)-g(x_0).
""")

    st.markdown(r"""
Since $b=g(x_0)$, we have
$b+k=g(x_0+h)$.

Substituting into the representation of $f$ gives
""")

    st.latex(r"""
\begin{aligned}
f(g(x_0+h))
&=f(g(x_0))\\
&\quad+f'(g(x_0))k+E_f(k).
\end{aligned}
""")

    st.markdown(r"""
Now, from the representation of $g$,
""")

    st.latex(r"""
k=g'(x_0)h+E_g(h).
""")

    st.markdown(r"""
Substituting this expression for $k$, we obtain
""")

    st.latex(r"""
\begin{aligned}
f(g(x_0+h))
&=f(g(x_0))\\
&\quad+f'(g(x_0))g'(x_0)h\\
&\quad+f'(g(x_0))E_g(h)\\
&\quad+E_f(k(h)).
\end{aligned}
""")

    st.markdown(r"""
Notice that this expression already resembles
the remainder-term characterization of
differentiability:
""")

    st.latex(r"""
F(x_0+h)=F(x_0)+mh+E(h).
""")

    st.markdown(r"""
Indeed, for $F=f\circ g$, the coefficient
of the linear term is
""")

    st.latex(r"""
m=f'(g(x_0))g'(x_0).
""")

    st.markdown(r"""
This is exactly the expression appearing
in the chain rule.

**However, we must still verify that the new
remainder term satisfies the required condition.**
""")

    st.divider()

    st.markdown(r"""
**Step 3 — Verify the remainder condition.**

Define the new remainder function by
""")

    st.latex(r"""
\boxed{
E(h)=f'(g(x_0))E_g(h)+E_f(k(h)).
}
""")

    st.markdown(r"""
To establish differentiability, we need to prove
""")

    st.latex(r"""
\lim_{h\to0}\frac{E(h)}{h}=0.
""")

    st.markdown(r"""
Dividing the expression for $E(h)$ by $h\neq0$,
we obtain
""")

    st.latex(r"""
\begin{aligned}
\frac{E(h)}{h}
&=f'(g(x_0))\frac{E_g(h)}{h}\\
&\quad+\frac{E_f(k(h))}{h}.
\end{aligned}
""")

    st.markdown(r"""
The first term tends to zero immediately, since
""")

    st.latex(r"""
\frac{E_g(h)}{h}\longrightarrow0.
""")

    st.markdown(r"""
It remains to examine the second term.

Recall that
""")

    st.latex(r"""
k(h)=g(x_0+h)-g(x_0).
""")

    st.markdown(r"""
Since differentiability implies continuity,
""")

    st.latex(r"""
k(h)\longrightarrow0
\qquad (h\to0).
""")

    st.markdown(r"""
Moreover, by the definition of the derivative,
""")

    st.latex(r"""
\frac{k(h)}{h}
\longrightarrow g'(x_0).
""")

    st.markdown(r"""
In particular, $k(h)/h$ is bounded for
sufficiently small nonzero $h$.

If $k(h)\neq0$, we can factor the second term:
""")

    st.latex(r"""
\frac{E_f(k(h))}{h}
=
\frac{E_f(k(h))}{k(h)}
\cdot\frac{k(h)}{h}.
""")

    st.markdown(r"""
The first factor tends to zero by the
remainder condition for $f$, while the
second factor tends to $g'(x_0)$.

Therefore, their product tends to zero.

There is one technical detail: it is possible
that $k(h)=0$ for some nonzero values of $h$.

In that case, the remainder representation of
$f$ gives $E_f(0)=0$, so
""")

    st.latex(r"""
\frac{E_f(k(h))}{h}=0.
""")

    st.markdown(r"""
To handle both cases rigorously, define
""")

    st.latex(r"""
r(k)=
\begin{cases}
\displaystyle\frac{E_f(k)}{k},
& k\neq0,\\[8pt]
0,&k=0.
\end{cases}
""")

    st.markdown(r"""
By the remainder condition, $r(k)\to0$
as $k\to0$.

Consequently, for every sufficiently small
nonzero $h$,
""")

    st.latex(r"""
\frac{E_f(k(h))}{h}
=
r(k(h))\frac{k(h)}{h}
\longrightarrow0.
""")

    st.markdown(r"""
Thus, both terms in $E(h)/h$ tend to zero,
and we conclude that
""")

    st.latex(r"""
\boxed{
\lim_{h\to0}\frac{E(h)}{h}=0.
}
""")

    st.divider()

    st.markdown(r"""
**Step 4 — Apply the equivalence theorem.**

We have shown that the composition satisfies
""")

    st.latex(r"""
\begin{aligned}
(f\circ g)(x_0+h)
&=(f\circ g)(x_0)\\
&\quad+f'(g(x_0))g'(x_0)h\\
&\quad+E(h),
\end{aligned}
""")

    st.markdown(r"""
with
""")

    st.latex(r"""
\lim_{h\to0}\frac{E(h)}{h}=0.
""")

    st.markdown(r"""
By the equivalence theorem established earlier,
$f\circ g$ is differentiable at $x_0$, and its
derivative is the coefficient of the linear term.

Therefore,
""")

    st.latex(r"""
\boxed{
(f\circ g)'(x_0)
=
f'(g(x_0))g'(x_0).
}
""")

    st.markdown(r"""
This completes the proof. $\square$
""")

st.caption(
    "Reference: Gerald B. Folland, Advanced Calculus, "
    "2nd Edition, Section 2.1, pp. 43–44."
)
