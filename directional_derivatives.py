import streamlit as st

# ==========================================
# GRADIENT & DIRECTIONAL DERIVATIVES
# Based on Folland, Advanced Calculus, §2.2
# ==========================================

st.title("Gradient & Directional Derivatives")

st.markdown(r"""
Partial derivatives describe how a function changes
along the coordinate directions.

We now extend this idea to arbitrary directions
and investigate the geometric meaning of the gradient.
""")

# ==========================================
# EXPANDER STYLE
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
# 1. DIRECTIONAL DERIVATIVES
# ==========================================

st.header("1. Directional Derivatives")

st.markdown(r"""
Let $U\subseteq\mathbb{R}^n$ be open, and let
$f:U\to\mathbb{R}$.

Given a point $a\in U$ and a unit vector
$u\in\mathbb{R}^n$, consider the line through
$a$ in the direction $u$:
""")

st.latex(r"""
g(t)=a+tu.
""")

st.markdown(r"""
The parameter $t\in\mathbb{R}$ describes
the displacement along this line.

We want to determine how rapidly $f$ changes
when moving away from $a$ in the direction $u$.
""")

st.subheader("Definition — Directional Derivative")

st.markdown(r"""
The **directional derivative** of $f$ at $a$
in the direction of the unit vector $u$ is defined by
""")

st.latex(r"""
\boxed{
D_uf(a)=
\lim_{t\to0}
\frac{f(a+tu)-f(a)}{t}
}
""")

st.markdown(r"""
provided that the limit exists.

It represents the instantaneous rate of change
of $f$ along the line through $a$ in the direction $u$.

Notice that the definition does **not** require
$f$ to be differentiable at $a$.
""")

st.subheader("Connection to Partial Derivatives")

st.markdown(r"""
Let $e_j$ denote the $j$-th standard basis vector
of $\mathbb{R}^n$.

Choosing $u=e_j$, only the $j$-th coordinate changes.
Therefore,
""")

st.latex(r"""
\begin{aligned}
D_{e_j}f(a)
&=
\lim_{t\to0}
\frac{f(a+te_j)-f(a)}{t}\\[6pt]
&=\partial_j f(a).
\end{aligned}
""")

st.markdown(r"""
Thus, partial derivatives are special cases
of directional derivatives.
""")


# ==========================================
# 2. THE GRADIENT FORMULA
# ==========================================

st.divider()

st.header("2. Directional Derivatives and the Gradient")

st.subheader("Theorem — Folland 2.23")

st.markdown(r"""
If $f$ is differentiable at $a$, then all
directional derivatives of $f$ at $a$ exist,
and for every unit vector $u$,
""")

st.latex(r"""
\boxed{D_uf(a)=\nabla f(a)\cdot u.}
""")

st.markdown(r"""
The theorem shows that, once differentiability
is known, every directional derivative can be
computed from the gradient.
""")

with st.expander(
    "Proof — Directional Derivative Formula",
    expanded=False
):

    st.markdown("**Proof.**")

    st.markdown(r"""
    Since $f$ is differentiable at $a$, we have
    the remainder representation
    """)

    st.latex(r"""
    f(a+h)=f(a)+\nabla f(a)\cdot h+E(h),
    """)

    st.markdown(r"""
    where $h\in\mathbb{R}^n$ and
    """)

    st.latex(r"""
    \lim_{h\to0}\frac{E(h)}{\|h\|}=0.
    """)

    st.markdown(r"""
    Let $u\in\mathbb{R}^n$ be an arbitrary
    unit vector, so that $\|u\|=1$.

    Choose $h=tu$, where $t\in\mathbb{R}$
    and $t\neq0$.

    Substituting into the remainder representation,
    we obtain
    """)

    st.latex(r"""
    f(a+tu)
    =
    f(a)+t\nabla f(a)\cdot u+E(tu).
    """)

    st.markdown(r"""
    Subtracting $f(a)$ and dividing by $t$ gives
    """)

    st.latex(r"""
    \frac{f(a+tu)-f(a)}{t}
    =
    \nabla f(a)\cdot u+\frac{E(tu)}{t}.
    """)

    st.markdown(r"""
    We now examine the remainder term.

    Since $\|u\|=1$, we have
    $\|tu\|=|t|$, and therefore
    $tu\to0$ as $t\to0$.

    By the remainder condition,
    """)

    st.latex(r"""
    \begin{aligned}
    \left|\frac{E(tu)}{t}\right|
    &=\frac{|E(tu)|}{|t|}\\[6pt]
    &=\frac{|E(tu)|}{\|tu\|}\\[6pt]
    &=\left|\frac{E(tu)}{\|tu\|}\right|\\[6pt]
    &\longrightarrow0
    \qquad(t\to0).
    \end{aligned}
    """)

    st.markdown(r"""
    Hence,
    """)

    st.latex(r"""
    \lim_{t\to0}\frac{E(tu)}{t}=0.
    """)

    st.markdown(r"""
    Taking the limit in the difference quotient,
    we conclude that
    """)

    st.latex(r"""
    \begin{aligned}
    D_uf(a)
    &=
    \lim_{t\to0}
    \frac{f(a+tu)-f(a)}{t}\\[6pt]
    &=\nabla f(a)\cdot u.
    \end{aligned}
    """)

    st.markdown(r"""
    Since $u$ was arbitrary, the result holds
    for every unit direction.

    $\square$
    """)



# ==========================================
# 3. DIRECTION OF STEEPEST ASCENT
# ==========================================

st.divider()

st.header("3. Direction of Steepest Ascent")

st.markdown(r"""
The directional derivative tells us how rapidly
a differentiable function changes in a given direction.

A natural question is:

**In which direction does the function increase
most rapidly?**
""")

st.subheader("Geometric Interpretation")

st.markdown(r"""
Suppose $\nabla f(a)\neq0$.

Let $\theta$ be the angle between the gradient
$\nabla f(a)$ and a unit vector $u$.

By the geometric interpretation of the dot product,
""")

st.latex(r"""
\begin{aligned}
D_uf(a)
&=\nabla f(a)\cdot u\\[6pt]
&=\|\nabla f(a)\|\|u\|\cos\theta\\[6pt]
&=\|\nabla f(a)\|\cos\theta.
\end{aligned}
""")

st.markdown(r"""
Since $\cos\theta\leq1$, we obtain
""")

st.latex(r"""
\boxed{
D_uf(a)\leq\|\nabla f(a)\|.
}
""")

st.markdown(r"""
This gives an upper bound for the directional
derivative in every unit direction.

The question is whether this bound can be attained.
""")

st.subheader("Theorem — Direction of Steepest Ascent")

st.markdown(r"""
Let $f$ be differentiable at $a$ and suppose
that $\nabla f(a)\neq0$.

Then the direction of steepest instantaneous
ascent is
""")

st.latex(r"""
\boxed{
u_*=\frac{\nabla f(a)}{\|\nabla f(a)\|}.
}
""")

st.markdown(r"""
The maximum directional derivative is
""")

st.latex(r"""
\boxed{
\max_{\|u\|=1}D_uf(a)=\|\nabla f(a)\|.
}
""")

with st.expander(
    "Proof — Direction of Steepest Ascent",
    expanded=False
):

    st.markdown("**Proof.**")

    st.markdown(r"""
    Let $u\in\mathbb{R}^n$ be an arbitrary
    unit vector.

    From the geometric interpretation,
    """)

    st.latex(r"""
    \begin{aligned}
    D_uf(a)
    &=\|\nabla f(a)\|\cos\theta\\[6pt]
    &\leq\|\nabla f(a)\|.
    \end{aligned}
    """)

    st.markdown(r"""
    Thus, $\|\nabla f(a)\|$ is an upper bound
    for all directional derivatives.

    **When is equality attained?**

    Equality holds precisely when
    $\cos\theta=1$, that is, when $\theta=0$.

    Consider the unit vector
    """)

    st.latex(r"""
    u_*=\frac{\nabla f(a)}{\|\nabla f(a)\|}.
    """)

    st.markdown(r"""
    This vector is well-defined because
    $\nabla f(a)\neq0$, and it points
    in the same direction as the gradient.

    Substituting into the directional derivative,
    we obtain
    """)

    st.latex(r"""
    \begin{aligned}
    D_{u_*}f(a)
    &=\nabla f(a)\cdot
    \frac{\nabla f(a)}{\|\nabla f(a)\|}\\[8pt]
    &=\frac{\|\nabla f(a)\|^2}
    {\|\nabla f(a)\|}\\[8pt]
    &=\|\nabla f(a)\|.
    \end{aligned}
    """)

    st.markdown(r"""
    Therefore, the upper bound is attained,
    and the maximizing unit direction is unique.

    Hence,
    """)

    st.latex(r"""
    \boxed{
    \operatorname*{arg\,max}_{\|u\|=1}D_uf(a)
    =
    \frac{\nabla f(a)}{\|\nabla f(a)\|}.
    }
    """)

    st.markdown(r"""
    $\square$
    """)

st.markdown(r"""
**Conclusion.**

The gradient points in the direction of steepest
instantaneous increase, and its magnitude gives
the maximum rate of increase.

If $\nabla f(a)=0$, every directional derivative
is zero, so no unique maximizing direction exists.
""")


# ==========================================
# 4. WORKED EXAMPLE
# ==========================================

st.divider()

st.header("4. Worked Example")

st.markdown(r"""
Consider the function
""")

st.latex(r"""
f(x,y)=x^2+xy+2y^2.
""")

st.markdown(r"""
Find the directional derivative at
$a=(1,-1)$ in the direction of the vector
$v=(3,4)$.
""")

with st.expander(
    "Solution — Computing a Directional Derivative",
    expanded=False
):

    st.markdown("**Solution.**")

    st.markdown(r"""
    **Step 1. Normalize the direction vector.**

    Since
    """)

    st.latex(r"""
    \|v\|=\sqrt{3^2+4^2}=5,
    """)

    st.markdown(r"""
    the unit vector in the direction of $v$ is
    """)

    st.latex(r"""
    u=\frac{v}{\|v\|}
    =\left(\frac35,\frac45\right).
    """)

    st.markdown(r"""
    **Step 2. Compute the gradient.**
    """)

    st.latex(r"""
    \begin{aligned}
    \partial_1f(x,y)&=2x+y,\\
    \partial_2f(x,y)&=x+4y.
    \end{aligned}
    """)

    st.markdown(r"""
    Hence,
    """)

    st.latex(r"""
    \nabla f(x,y)=(2x+y,\;x+4y).
    """)

    st.markdown(r"""
    Evaluating at $a=(1,-1)$ gives
    """)

    st.latex(r"""
    \nabla f(1,-1)=(1,-3).
    """)

    st.markdown(r"""
    **Step 3. Apply the directional derivative formula.**
    """)

    st.latex(r"""
    \begin{aligned}
    D_uf(1,-1)
    &=\nabla f(1,-1)\cdot u\\[6pt]
    &=(1,-3)\cdot
    \left(\frac35,\frac45\right)\\[6pt]
    &=\frac35-\frac{12}{5}\\[6pt]
    &=-\frac95.
    \end{aligned}
    """)

    st.markdown(r"""
    Therefore,
    """)

    st.latex(r"""
    \boxed{D_uf(1,-1)=-\frac95.}
    """)

    st.markdown(r"""
    The negative value means that the function
    decreases instantaneously in the chosen direction.

    **Verification from the definition.**

    Substituting
    $a=(1,-1)$ and
    $u=(3/5,4/5)$ into $f$, we obtain
    """)

    st.latex(r"""
    f(a+tu)
    =
    2-\frac95t+\frac{53}{25}t^2.
    """)

    st.markdown(r"""
    Since $f(a)=2$, it follows that
    """)

    st.latex(r"""
    \begin{aligned}
    D_uf(a)
    &=
    \lim_{t\to0}
    \frac{f(a+tu)-f(a)}{t}\\[6pt]
    &=
    \lim_{t\to0}
    \left(
    -\frac95+\frac{53}{25}t
    \right)\\[6pt]
    &=-\frac95.
    \end{aligned}
    """)

    st.markdown(r"""
    Both methods give the same result.
    """)


# ==========================================
# 5. COUNTEREXAMPLE — FOLLAND EXERCISE 7
# ==========================================

st.divider()

st.header("5. Do Directional Derivatives Imply Differentiability?")

st.markdown(r"""
We have proved that differentiability implies
the existence of all directional derivatives.

**Does the converse hold?**

The following counterexample, based on
Folland's Exercise 7, shows that it does not.
""")

st.subheader("Counterexample — Folland, Exercise 7")

st.markdown(r"""
Define $f:\mathbb{R}^2\to\mathbb{R}$ by
""")

st.latex(r"""
f(x,y)=
\begin{cases}
\dfrac{x^2y}{x^2+y^2},
& (x,y)\neq(0,0),\\[8pt]
0,
& (x,y)=(0,0).
\end{cases}
""")

st.markdown(r"""
We will show that:

1. $f$ is continuous at the origin.
2. Every directional derivative at the origin exists.
3. Nevertheless, $f$ is not differentiable at the origin.
""")

with st.expander(
    "Proof — Counterexample (Folland Exercise 7)",
    expanded=False
):

    st.markdown("**Proof.**")

    # --------------------------------------
    # PART A — CONTINUITY
    # --------------------------------------

    st.markdown("**Part A — Continuity at the origin.**")

    st.markdown(r"""
    For $(x,y)\neq(0,0)$, we have
    """)

    st.latex(r"""
    \begin{aligned}
    |f(x,y)|
    &=
    \left|\frac{x^2y}{x^2+y^2}\right|\\[6pt]
    &=
    \frac{x^2}{x^2+y^2}|y|\\[6pt]
    &\leq |y|,
    \end{aligned}
    """)

    st.markdown(r"""
    since $0\leq x^2/(x^2+y^2)\leq1$.

    As $(x,y)\to(0,0)$, we have $|y|\to0$.

    Therefore, by the squeeze theorem,
    """)

    st.latex(r"""
    \lim_{(x,y)\to(0,0)}f(x,y)
    =0=f(0,0).
    """)

    st.markdown(r"""
    Hence, $f$ is continuous at the origin.
    """)

    # --------------------------------------
    # PART B — DIRECTIONAL DERIVATIVES
    # --------------------------------------

    st.markdown(
        "**Part B — Existence of all directional derivatives.**"
    )

    st.markdown(r"""
    Let $u=(u_1,u_2)$ be an arbitrary unit vector,
    so that $u_1^2+u_2^2=1$.

    By definition,
    """)

    st.latex(r"""
    D_uf(0,0)
    =
    \lim_{t\to0}
    \frac{f(tu_1,tu_2)-f(0,0)}{t}.
    """)

    st.markdown(r"""
    For $t\neq0$, substituting into the
    definition of $f$ gives
    """)

    st.latex(r"""
    \begin{aligned}
    f(tu_1,tu_2)
    &=
    \frac{(tu_1)^2(tu_2)}
    {(tu_1)^2+(tu_2)^2}\\[8pt]
    &=
    \frac{t^3u_1^2u_2}
    {t^2(u_1^2+u_2^2)}\\[8pt]
    &=tu_1^2u_2.
    \end{aligned}
    """)

    st.markdown(r"""
    Since $f(0,0)=0$, we obtain
    """)

    st.latex(r"""
    \begin{aligned}
    D_uf(0,0)
    &=
    \lim_{t\to0}
    \frac{tu_1^2u_2}{t}\\[6pt]
    &=u_1^2u_2.
    \end{aligned}
    """)

    st.markdown(r"""
    Thus,
    """)

    st.latex(r"""
    \boxed{D_uf(0,0)=u_1^2u_2.}
    """)

    st.markdown(r"""
    This limit exists for every unit vector $u$.

    Therefore, all directional derivatives
    exist at the origin.
    """)

    # --------------------------------------
    # PART C — FAILURE OF DIFFERENTIABILITY
    # --------------------------------------

    st.markdown("**Part C — Failure of differentiability.**")

    st.markdown(r"""
    First, observe that the two partial
    derivatives at the origin are zero:
    """)

    st.latex(r"""
    \partial_1f(0,0)=0,
    \qquad
    \partial_2f(0,0)=0.
    """)

    st.markdown(r"""
    Indeed, $f(t,0)=f(0,t)=0$ for every $t$.

    Hence,
    """)

    st.latex(r"""
    \nabla f(0,0)=(0,0).
    """)

    st.markdown(r"""
    Suppose, for contradiction, that
    $f$ is differentiable at the origin.

    Then Theorem 2.23 would imply
    """)

    st.latex(r"""
    D_uf(0,0)
    =
    \nabla f(0,0)\cdot u
    =0
    """)

    st.markdown(r"""
    for every unit vector $u$.

    However, choose
    """)

    st.latex(r"""
    u=
    \left(
    \frac1{\sqrt2},
    \frac1{\sqrt2}
    \right).
    """)

    st.markdown(r"""
    From Part B, we know that
    """)

    st.latex(r"""
    \begin{aligned}
    D_uf(0,0)
    &=u_1^2u_2\\[6pt]
    &=
    \left(\frac1{\sqrt2}\right)^2
    \frac1{\sqrt2}\\[6pt]
    &=\frac1{2\sqrt2}\neq0.
    \end{aligned}
    """)

    st.markdown(r"""
    This contradicts the directional derivative
    formula that would hold under differentiability.

    Therefore, $f$ is **not differentiable**
    at the origin.

    $\square$
    """)

st.markdown(r"""
**Conclusion.**

The existence of all directional derivatives,
even together with continuity, does not guarantee
differentiability.

Differentiability is a stronger property:
it requires a single linear approximation
that works for increments approaching the point
from every direction.
""")


# ==========================================
# REFERENCE
# ==========================================

st.divider()

st.caption(
    "Mathematical reference: Gerald B. Folland, "
    "Advanced Calculus, 2nd ed., Section 2.2, "
    "Theorem 2.23 and Exercise 7."
)
