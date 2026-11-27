
import streamlit as st

# ==========================================
# TAYLOR POLYNOMIALS — THEORY & PROOF
# Based on Folland, Advanced Calculus, §2.7
# ==========================================

st.title("Taylor Polynomials — Theory & Proof")

# ==========================================
# PROOF EXPANDER STYLING
# ==========================================

st.markdown(
    """
    <style>
    div[data-testid="stExpander"] > details > summary {
        background-color: #382A56;
        color: #FFFFFF;
        border-radius: 8px;
        padding: 12px 16px;
    }

    div[data-testid="stExpander"] > details > summary:hover {
        background-color: #4B396E;
    }

    div[data-testid="stExpander"] > details > summary * {
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("## Taylor's Theorem")
st.divider()
st.subheader("Mathematical Background")


# ==========================================
# 1. TAYLOR'S THEOREM
# ==========================================

st.markdown(
    "### Theorem (Taylor's Theorem with Integral Remainder)."
)

st.markdown(
    r"Let $f\in C^{n+1}(I)$, where $I$ is an interval "
    r"containing $a$ and $x$. Then"
)

st.latex(
    r"f(x)=T_n(x;a)+R_n(x;a)"
)

st.markdown(
    "The Taylor polynomial of degree $n$ is"
)

st.latex(
    r"T_n(x;a)=\sum_{k=0}^{n}"
    r"\frac{f^{(k)}(a)}{k!}(x-a)^k"
)

st.markdown(
    "The remainder admits the integral representation"
)

st.latex(
    r"R_n(x;a)=\frac{(x-a)^{n+1}}{n!}"
    r"\int_0^1(1-t)^n"
    r"f^{(n+1)}(a+t(x-a))\,dt"
)


# ==========================================
# PROOF — TAYLOR'S THEOREM
# ==========================================

with st.expander("Proof — Taylor's Theorem", expanded=False):

    st.markdown("**Proof.**")

    st.markdown(
        r"Set $h=x-a$. By the Fundamental Theorem of Calculus,"
    )

    st.latex(
        r"f(a+h)=f(a)+h\int_0^1 f'(a+th)\,dt."
    )

    st.markdown(
        "We now apply integration by parts using"
    )

    st.latex(
        r"\int_0^1 u(t)v'(t)\,dt"
        r"=[u(t)v(t)]_0^1"
        r"-\int_0^1 u'(t)v(t)\,dt."
    )

    st.markdown("We choose")

    st.latex(
        r"\begin{aligned}"
        r"u(t)&=f'(a+th),\\"
        r"u'(t)&=hf''(a+th),\\"
        r"v'(t)&=1."
        r"\end{aligned}"
    )

    st.markdown(
        r"Since $v'(t)=1$, any function of the form "
        r"$v(t)=t+C$ is an antiderivative of $1$. "
        r"We choose $C=-1$, so that $v(t)=t-1$. "
        r"This choice is convenient because $v(1)=0$, "
        r"which eliminates the boundary term at $t=1$."
    )

    st.markdown(
        "Applying integration by parts yields"
    )

    st.latex(
        r"\begin{aligned}"
        r"h\int_0^1 f'(a+th)\,dt"
        r"&=h[(t-1)f'(a+th)]_0^1\\"
        r"&\quad-h^2\int_0^1(t-1)f''(a+th)\,dt\\"
        r"&=hf'(a)+h^2\int_0^1(1-t)f''(a+th)\,dt."
        r"\end{aligned}"
    )

    st.markdown(
        "We now apply integration by parts once more "
        "to the remaining integral, assuming "
        r"$f\in C^3(I)$:"
    )

    st.latex(
        r"h^2\int_0^1(1-t)f''(a+th)\,dt."
    )

    st.markdown("This time, we choose")

    st.latex(
        r"\begin{aligned}"
        r"u(t)&=f''(a+th),\\"
        r"u'(t)&=hf'''(a+th),\\"
        r"v'(t)&=1-t,\\"
        r"v(t)&=-\frac{(1-t)^2}{2}."
        r"\end{aligned}"
    )

    st.markdown(
        "Again, the antiderivative is chosen so that "
        r"$v(1)=0$, eliminating the upper boundary term."
    )

    st.markdown(
        "Applying integration by parts yields"
    )

    st.latex(
        r"\begin{aligned}"
        r"&h^2\int_0^1(1-t)f''(a+th)\,dt\\"
        r"&=h^2\left[-\frac{(1-t)^2}{2}"
        r"f''(a+th)\right]_0^1\\"
        r"&\quad+\frac{h^3}{2}"
        r"\int_0^1(1-t)^2f'''(a+th)\,dt\\"
        r"&=\frac{h^2}{2!}f''(a)"
        r"+\frac{h^3}{2!}"
        r"\int_0^1(1-t)^2f'''(a+th)\,dt."
        r"\end{aligned}"
    )

    st.markdown(
        "Substituting this into the previous expression, "
        "we obtain"
    )

    st.latex(
        r"\begin{aligned}"
        r"f(a+h)={}&f(a)+hf'(a)"
        r"+\frac{h^2}{2!}f''(a)\\"
        r"&+\frac{h^3}{2!}"
        r"\int_0^1(1-t)^2f'''(a+th)\,dt."
        r"\end{aligned}"
    )

    st.markdown(
        "**The pattern is now clear.** "
        "Repeating the argument yields the general formula."
    )

    st.markdown(
        "Repeating integration by parts produces the "
        "successive Taylor terms. After $n$ steps, we obtain"
    )

    st.latex(
        r"f(a+h)=\sum_{k=0}^{n}"
        r"\frac{f^{(k)}(a)}{k!}h^k"
        r"+\frac{h^{n+1}}{n!}"
        r"\int_0^1(1-t)^n"
        r"f^{(n+1)}(a+th)\,dt."
    )

    st.markdown(
        r"Substituting $h=x-a$ proves the theorem. "
        r"$\square$"
    )

    st.info(
        r"""
        **Note — Mathematical Induction**

        The previous calculations establish the formula
        up to degree 2 and reveal a general pattern.
        However, observing a pattern does not prove
        that it holds for every degree.

        To establish the general formula, we use
        mathematical induction.

        We assume that the formula holds for some
        integer $k \geq 2$ and prove that it must
        also hold for $k+1$. This induction step
        follows by applying integration by parts
        once more to the remainder term.

        Since we have already verified the formula
        for $k=1$ and $k=2$, the induction step implies that
        it holds for $k=3$. Consequently, it also
        holds for $k=4$, then $k=5$, and so on.

        Thus, by mathematical induction, the formula
        holds for every integer $k \geq 2$.
        """
    )


# ==========================================
# 2. TAYLOR ERROR ESTIMATE
# ==========================================

st.divider()

st.markdown("### Theorem — Taylor Error Estimate")

st.markdown(
    r"Suppose that $f\in C^{n+1}(I)$ and "
    r"$|f^{(n+1)}(x)|\leq M$ for every $x\in I$. "
    r"Then, for all $a,x\in I$,"
)

st.latex(
    r"\boxed{|f(x)-T_n(x;a)|"
    r"\leq \frac{M}{(n+1)!}|x-a|^{n+1}}"
)


# ==========================================
# PROOF — TAYLOR ERROR ESTIMATE
# ==========================================

with st.expander("Proof — Taylor Error Estimate", expanded=False):

    st.markdown("**Proof.**")

    st.markdown(
        "Using the integral representation of the "
        "Taylor remainder and the assumed bound, we obtain"
    )

    st.latex(
        r"\begin{aligned}"
        r"|R_n(x;a)|"
        r"&\leq \frac{|x-a|^{n+1}}{n!}"
        r"\int_0^1(1-t)^n"
        r"|f^{(n+1)}(a+t(x-a))|\,dt\\[6pt]"
        r"&\leq \frac{M|x-a|^{n+1}}{n!}"
        r"\int_0^1(1-t)^n\,dt\\[6pt]"
        r"&=\frac{M}{(n+1)!}|x-a|^{n+1}."
        r"\end{aligned}"
    )

    st.markdown(r"$\square$")


# ==========================================
# 3. INTERPRETATION AND CONVERGENCE
# ==========================================

st.divider()

st.markdown("### Interpretation & Convergence")

st.markdown(
    "The Taylor error estimate explains why polynomial "
    "approximations are particularly accurate near the "
    "expansion point. The factor $|x-a|^{n+1}$ reflects "
    "the distance from the expansion point."
)

st.markdown(
    "### Theorem — Convergence of Taylor Polynomials"
)

st.markdown(
    r"Let $f\in C^\infty(I)$, where $I$ is an interval, "
    r"and suppose there exists a constant $K>0$ such that"
)

st.latex(
    r"|f^{(k)}(x)|\leq K"
    r"\qquad \forall k\geq 1,\ \forall x\in I."
)

st.markdown(
    r"Then, for every $a,x\in I$, the Taylor polynomials "
    r"of $f$ centered at $a$ converge to $f(x)$:"
)

st.latex(
    r"\boxed{\lim_{n\to\infty}T_n(x;a)=f(x)}"
)


# ==========================================
# PROOF — CONVERGENCE
# ==========================================

with st.expander(
    "Proof — Convergence of Taylor Polynomials",
    expanded=False
):

    st.markdown("**Proof.**")

    st.markdown(
        "By the Taylor error estimate, for every "
        r"$n\geq 0$ we have"
    )

    st.latex(
        r"0\leq |f(x)-T_n(x;a)|"
        r"\leq \frac{K|x-a|^{n+1}}{(n+1)!}."
    )

    st.markdown(
        r"Since $a$ and $x$ are fixed, the factorial "
        r"in the denominator dominates the power "
        r"in the numerator. Therefore,"
    )

    st.latex(
        r"\lim_{n\to\infty}"
        r"\frac{K|x-a|^{n+1}}{(n+1)!}=0."
    )

    st.markdown(
        "Consequently, by the squeeze theorem,"
    )

    st.latex(
        r"\boxed{\lim_{n\to\infty}T_n(x;a)=f(x).}"
    )

    st.markdown(r"$\square$")


# ==========================================
# INTERPRETATION NOTE
# ==========================================

st.info(
    "The common bound K is essential for this argument. "
    "Having derivatives of every order, even if each "
    "derivative is individually bounded, does not "
    "by itself guarantee convergence of the Taylor "
    "polynomials to the original function."
)


# ==========================================
# 4. EXAMPLE — THE SINE FUNCTION
# ==========================================

st.divider()

st.markdown("### Example — The Sine Function")

st.markdown(
    r"Consider the function $f(x)=\sin x$. "
    r"It is infinitely differentiable on $\mathbb{R}$, "
    r"and its derivatives repeat periodically:"
)

st.latex(
    r"\begin{aligned}"
    r"f'(x)&=\cos x,\\"
    r"f''(x)&=-\sin x,\\"
    r"f'''(x)&=-\cos x,\\"
    r"f^{(4)}(x)&=\sin x."
    r"\end{aligned}"
)

st.markdown(
    r"Since $|\sin x|\leq 1$ and $|\cos x|\leq 1$, "
    r"all derivatives satisfy the common bound"
)

st.latex(
    r"|f^{(k)}(x)|\leq 1"
    r"\qquad \forall k\geq 1,\ \forall x\in\mathbb{R}."
)

st.markdown(
    r"Thus, the assumptions of the convergence theorem "
    r"hold with $K=1$. In particular, for every "
    r"expansion point $a\in\mathbb{R}$ and every "
    r"$x\in\mathbb{R}$,"
)

st.latex(
    r"|\,\sin x-T_n(x;a)\,|"
    r"\leq\frac{|x-a|^{n+1}}{(n+1)!}"
    r"\longrightarrow 0."
)

st.markdown("Consequently,")

st.latex(
    r"\boxed{\lim_{n\to\infty}T_n(x;a)=\sin x.}"
)

st.markdown(
    "Therefore, increasing the polynomial degree "
    "allows us to approximate the sine function "
    "arbitrarily accurately at any fixed point."
)
