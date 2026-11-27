import streamlit as st

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

# ==========================================
# GRADIENT DESCENT - MATHEMATICAL THEORY
# ==========================================

st.title("Gradient Descent — Theory & Proof")

st.write(
    "Gradient descent is an iterative optimization "
    "algorithm for minimizing differentiable functions."
)

# ==========================================
# 2. STEEPEST DESCENT DIRECTION
# ==========================================

st.markdown("### Theorem — Direction of Steepest Descent")

st.markdown(
    r"Suppose that $f:\mathbb{R}^d\to\mathbb{R}$ "
    r"is differentiable at $x$ and "
    r"$\nabla f(x)\neq 0$. "
    r"Among all unit vectors $v$, the directional derivative "
    r"$D_vf(x)$ is minimized when $v$ points in the direction "
    r"of the negative gradient."
)

st.latex(
    r"\boxed{"
    r"\arg\min_{\|v\|=1} D_vf(x)"
    r"="
    r"-\frac{\nabla f(x)}{\|\nabla f(x)\|}"
    r"}"
)
st.markdown(
    "In other words, the negative gradient "
    "determines the direction of steepest "
    "instantaneous descent."
)

# ==========================================
# 3. PROOF
# ==========================================

with st.expander("Proof", expanded=False):

    st.markdown("**Proof.**")

    st.markdown(
        r"Let $v\in\mathbb{R}^d$ be an arbitrary "
        r"unit vector, so that $\|v\|=1$."
    )

    st.markdown(
        "Recall the Cauchy–Schwarz inequality:"
    )

    st.latex(
        r"|\langle u,v\rangle|"
        r"\leq\|u\|\|v\|."
    )

    st.markdown(
        r"Since $- |c|\leq c$ for every real "
        r"number $c$, we obtain"
    )

    st.latex(
        r"\langle u,v\rangle"
        r"\geq-|\langle u,v\rangle|"
        r"\geq-\|u\|\|v\|."
    )

    st.markdown(
        r"Applying this inequality with "
        r"$u=\nabla f(x)$ gives"
    )

    st.latex(
        r"\begin{aligned}"
        r"D_vf(x)"
        r"&=\langle\nabla f(x),v\rangle\\"
        r"&\geq-\|\nabla f(x)\|\|v\|\\"
        r"&=-\|\nabla f(x)\|."
        r"\end{aligned}"
    )

    st.markdown(
        "Thus, the directional derivative "
        "is bounded below by the negative "
        "norm of the gradient."
    )

    st.markdown("**When does equality hold?**")

    st.markdown(
        "Consider the unit vector"
    )

    st.latex(
        r"v_*=-\frac{\nabla f(x)}"
        r"{\|\nabla f(x)\|}."
    )

    st.markdown(
        r"This vector is well-defined because "
        r"$\nabla f(x)\neq 0$, and it has norm one."
    )

    st.markdown(
        "Substituting this vector into the "
        "directional derivative, we obtain"
    )

    st.latex(
        r"\begin{aligned}"
        r"D_{v_*}f(x)"
        r"&=\left\langle\nabla f(x),"
        r"-\frac{\nabla f(x)}{\|\nabla f(x)\|}"
        r"\right\rangle\\[6pt]"
        r"&=-\frac{\langle\nabla f(x),"
        r"\nabla f(x)\rangle}"
        r"{\|\nabla f(x)\|}\\[6pt]"
        r"&=-\frac{\|\nabla f(x)\|^2}"
        r"{\|\nabla f(x)\|}\\[6pt]"
        r"&=-\|\nabla f(x)\|."
        r"\end{aligned}"
    )

    st.markdown(
        "Therefore, among all unit directions, the "
        "direction of steepest instantaneous descent is "
        "the negative gradient direction."
    )

    st.latex(
        r"\boxed{"
        r"\arg\min_{\|v\|=1} D_vf(x)"
        r"="
        r"-\frac{\nabla f(x)}{\|\nabla f(x)\|}"
        r"}"
    )

# ==========================================
# 4. GRADIENT DESCENT ALGORITHM
# ==========================================

st.header("1. Gradient Descent Algorithm")

st.markdown(
    "The theorem motivates the gradient "
    "descent iteration:"
)

st.latex(
    r"\boxed{x_{k+1}=x_k-\alpha_k\nabla f(x_k).}"
)

st.markdown(
    r"Here $x_k$ is the current iterate, "
    r"$\nabla f(x_k)$ is the gradient, and "
    r"$\alpha_k>0$ is the step size."
)

st.markdown(
    "The normalized negative gradient and "
    "the unnormalized negative gradient point "
    "in the same direction. Their difference "
    "in magnitude can be absorbed into "
    "the step size."
)

st.markdown(
    "A suitable step size is important: "
    "the steepest descent direction guarantees "
    "local decrease, but an arbitrarily large "
    "step need not decrease the function value."
)

st.info(
    "If the gradient is zero, every directional "
    "derivative is zero. In this case, the "
    "first-order argument does not determine "
    "a descent direction or guarantee "
    "that the point is a minimum."
)


# ==========================================
# DESCENT LEMMA
# ==========================================

st.markdown("---")

st.markdown("### Does Gradient Descent Always Decrease the Function Value?")

st.markdown(
    "Recall the gradient descent iteration:"
)

st.latex(
    r"x_{k+1}=x_k-\alpha_k\nabla f(x_k),"
    r"\qquad \alpha_k>0."
)

st.markdown(
    "Although the negative gradient determines the "
    "direction of steepest instantaneous descent, "
    "this does not guarantee that an arbitrary "
    "step size decreases the function value. "
    "In particular, we would like to know "
    "under which conditions"
)

st.latex(
    r"\boxed{f(x_{k+1})\leq f(x_k)}"
)

st.markdown(
    "To answer this question, we first establish "
    "an important result known as the Descent Lemma."
)

# ==========================================
# THEOREM
# ==========================================

st.markdown("### Lemma — Descent Lemma")

st.markdown(
    r"Let $f:\mathbb{R}^d\to\mathbb{R}$ be "
    r"continuously differentiable, and suppose "
    r"that its gradient is $L$-Lipschitz continuous "
    r"for some $L>0$, i.e."
)

st.latex(
    r"\|\nabla f(x)-\nabla f(y)\|"
    r"\leq L\|x-y\|"
    r"\qquad \forall x,y\in\mathbb{R}^d."
)

st.markdown(
    r"Then, for all $x,y\in\mathbb{R}^d$,"
)

st.latex(
    r"\boxed{"
    r"f(y)\leq f(x)"
    r"+\langle\nabla f(x),y-x\rangle"
    r"+\frac{L}{2}\|y-x\|^2"
    r"}"
)

# ==========================================
# PROOF
# ==========================================

with st.expander("Proof", expanded=False):

    st.markdown("**Proof.**")

    st.markdown(
        r"Let $x,y\in\mathbb{R}^d$ be arbitrary "
        r"and set $h=y-x$. "
        r"Define the function $g:[0,1]\to\mathbb{R}$ by"
    )

    st.latex(
        r"g(t)=f(x+th)."
    )

    st.markdown(
        "By the chain rule, we have"
    )

    st.latex(
        r"g'(t)=\langle\nabla f(x+th),h\rangle."
    )

    st.markdown(
        "Since $g(0)=f(x)$ and $g(1)=f(y)$, "
        "the Fundamental Theorem of Calculus gives"
    )

    st.latex(
        r"\begin{aligned}"
        r"f(y)-f(x)"
        r"&=g(1)-g(0)\\"
        r"&=\int_0^1g'(t)\,dt\\"
        r"&=\int_0^1"
        r"\langle\nabla f(x+th),h\rangle\,dt."
        r"\end{aligned}"
    )

    st.markdown(
        r"Subtracting $\langle\nabla f(x),h\rangle$ "
        r"from both sides, we obtain"
    )

    st.latex(
        r"\begin{aligned}"
        r"&f(y)-f(x)-\langle\nabla f(x),h\rangle\\"
        r"&=\int_0^1"
        r"\langle\nabla f(x+th)-\nabla f(x),h\rangle\,dt."
        r"\end{aligned}"
    )

    st.markdown(
        "Now we apply the Cauchy–Schwarz inequality:"
    )

    st.latex(
        r"\begin{aligned}"
        r"&f(y)-f(x)-\langle\nabla f(x),h\rangle\\"
        r"&\leq\int_0^1"
        r"\|\nabla f(x+th)-\nabla f(x)\|"
        r"\|h\|\,dt."
        r"\end{aligned}"
    )

    st.markdown(
        "By the Lipschitz continuity of the gradient,"
    )

    st.latex(
        r"\begin{aligned}"
        r"\|\nabla f(x+th)-\nabla f(x)\|"
        r"&\leq L\|th\|\\"
        r"&=Lt\|h\|,"
        r"\qquad 0\leq t\leq 1."
        r"\end{aligned}"
    )

    st.markdown(
        "Substituting this estimate into the integral yields"
    )

    st.latex(
        r"\begin{aligned}"
        r"&f(y)-f(x)-\langle\nabla f(x),h\rangle\\"
        r"&\leq\int_0^1Lt\|h\|^2\,dt\\"
        r"&=L\|h\|^2\int_0^1t\,dt\\"
        r"&=\frac{L}{2}\|h\|^2."
        r"\end{aligned}"
    )

    st.markdown(
        r"Finally, substituting $h=y-x$ and "
        r"rearranging the inequality gives"
    )

    st.latex(
        r"\boxed{"
        r"f(y)\leq f(x)"
        r"+\langle\nabla f(x),y-x\rangle"
        r"+\frac{L}{2}\|y-x\|^2"
        r"}"
    )

    st.markdown(r"$\square$")

    st.caption(
        "Proof based on the standard Descent Lemma argument. "
        "Reference: Cornell University, "
        "CS4787 — Gradient Descent, Lecture 6."
    )

    
# ==========================================
# SUFFICIENT STEP SIZE FOR DESCENT
# ==========================================

st.markdown("---")

st.header("2. Sufficient Step Size for Descent")

st.markdown(
    "We are now ready to answer our original question: "
    "under which conditions does gradient descent "
    "actually decrease the objective function?"
)

st.markdown(
    "The Descent Lemma provides an upper bound "
    "for the function value at any new point. "
    "By applying this result to the gradient "
    "descent iteration, we can derive a sufficient "
    "condition on the step size that guarantees descent."
)

# ==========================================
# THEOREM
# ==========================================

st.markdown("### Theorem — Sufficient Step Size for Descent")

st.markdown(
    r"Let $f:\mathbb{R}^d\to\mathbb{R}$ be "
    r"continuously differentiable, and suppose "
    r"that its gradient is $L$-Lipschitz continuous "
    r"for some $L>0$."
)

st.markdown(
    "Consider the gradient descent iteration"
)

st.latex(
    r"x_{k+1}=x_k-\alpha_k\nabla f(x_k),"
    r"\qquad \alpha_k>0."
)

st.markdown(
    "If the step size satisfies"
)

st.latex(
    r"\boxed{0<\alpha_k<\frac{2}{L},}"
)

st.markdown(
    "then the objective function decreases strictly "
    "at every iteration for which the gradient is nonzero:"
)

st.latex(r"\boxed{\nabla f(x_k)\neq 0 \quad\Longrightarrow\quad f(x_{k+1})<f(x_k)}")

st.markdown(
    r"If $\nabla f(x_k)=0$, then $x_{k+1}=x_k$, "
    r"so the function value remains unchanged."
)

# ==========================================
# PROOF
# ==========================================

with st.expander("Proof", expanded=False):

    st.markdown("**Proof.**")

    st.markdown(
        "Recall the Descent Lemma:"
    )

    st.latex(
        r"f(y)\leq f(x)"
        r"+\langle\nabla f(x),y-x\rangle"
        r"+\frac{L}{2}\|y-x\|^2."
    )

    st.markdown(
        "We apply this inequality with"
    )

    st.latex(
    r"x=x_k,\qquad y=x_{k+1}=x_k-\alpha_k\nabla f(x_k)."
    )

    st.markdown(
        "Observe that"
    )

    st.latex(
        r"x_{k+1}-x_k=-\alpha_k\nabla f(x_k)."
    )

    st.markdown(
        "Substituting into the Descent Lemma gives"
    )

    st.latex(
        r"\begin{aligned}"
        r"f(x_{k+1})"
        r"&\leq f(x_k)"
        r"+\langle\nabla f(x_k),"
        r"-\alpha_k\nabla f(x_k)\rangle\\"
        r"&\quad+\frac{L}{2}"
        r"\|-\alpha_k\nabla f(x_k)\|^2."
        r"\end{aligned}"
    )

    st.markdown(
        "Using the properties of the inner product "
        "and the norm, we obtain"
    )

    st.latex(
        r"\begin{aligned}"
        r"f(x_{k+1})"
        r"&\leq f(x_k)"
        r"-\alpha_k\|\nabla f(x_k)\|^2\\"
        r"&\quad+\frac{L\alpha_k^2}{2}"
        r"\|\nabla f(x_k)\|^2."
        r"\end{aligned}"
    )

    st.markdown(
        "Factoring the last two terms yields"
    )

    st.latex(
        r"\boxed{"
        r"f(x_{k+1})"
        r"\leq f(x_k)"
        r"-\alpha_k\left(1-\frac{L\alpha_k}{2}\right)"
        r"\|\nabla f(x_k)\|^2."
        r"}"
    )

    st.markdown(
        "Now suppose that"
    )

    st.latex(
        r"0<\alpha_k<\frac{2}{L}."
    )

    st.markdown(
        "Then"
    )

    st.latex(
        r"\alpha_k>0,"
        r"\qquad"
        r"1-\frac{L\alpha_k}{2}>0."
    )

    st.markdown(
        r"Furthermore, if $\nabla f(x_k)\neq 0$, then"
    )

    st.latex(
        r"\|\nabla f(x_k)\|^2>0."
    )

    st.markdown(
        "Consequently, the subtracted quantity "
        "is strictly positive, and therefore"
    )

    st.latex(
        r"\boxed{f(x_{k+1})<f(x_k).}"
    )

    st.markdown(
        "Thus, every nonstationary gradient descent "
        "iteration strictly decreases the objective "
        "function whenever the step size satisfies "
        "the stated condition."
    )

    st.markdown(r"$\square$")


# ==========================================
# INTERPRETATION
# ==========================================

st.markdown("### Interpretation")

st.markdown(
    "The theorem explains why the step size is crucial. "
    "The negative gradient determines a locally "
    "decreasing direction, but taking a step that "
    "is too large may increase the function value."
)

st.markdown(
    r"When the gradient is $L$-Lipschitz continuous, "
    r"the condition $0<\alpha_k<2/L$ guarantees "
    r"strict descent at every nonstationary iteration."
)

st.info(
    "This result guarantees a decrease in the "
    "objective function, but it does not by itself "
    "guarantee convergence to a global minimizer."
)


st.caption(
    "References: Gradient Descent and Its Analysis "
    "(University of Wisconsin–Madison); "
    "Boyd & Vandenberghe, Convex Optimization."
)
