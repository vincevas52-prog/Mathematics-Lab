
import streamlit as st

# Page configuration is defined in app.py.
# This module is loaded through st.navigation().

st.title("The Multivariable Chain Rule")
st.caption("Theory & Proof · Based on Folland, Advanced Calculus, §2.3")

st.markdown(
    "The chain rule explains how to differentiate a **composition** when "
    "one or several intermediate variables depend on other variables. "
    "Its central idea is that the derivative of a composition is the "
    "composition of the derivatives."
)

# ==========================================
# EXPANDER STYLING
# ==========================================

st.markdown(
    """
    <style>
    div[data-testid="stExpander"] {
        background-color: #211A2D;
        border: 1px solid #382A56;
        border-radius: 10px;
    }
    div[data-testid="stExpander"] details summary:hover {
        background-color: #4B396E;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.divider()

# ==========================================
# 1. MATHEMATICAL BACKGROUND
# ==========================================

st.header("1. Mathematical Background")

st.markdown(
    "Let $U\\subseteq\\mathbb{R}^n$ be open, let "
    "$f:U\\to\\mathbb{R}$, and suppose that a differentiable map "
    "$g$ takes its values in $U$. We want to study the composite function"
)
st.latex(r"\varphi = f\circ g,\qquad \varphi(t)=f(g(t)).")

st.markdown(
    "We begin with a single independent variable, "
    "then move to the general case with several independent variables."
)

st.markdown("**Differentiability is a linear approximation.** For a scalar-valued function:")
st.latex(
    r"f(b+v)=f(b)+\nabla f(b)\cdot v+r_f(v),"
)
st.latex(
    r"\lim_{v\to 0}\frac{r_f(v)}{\|v\|}=0."
)
st.markdown(
    "The chain rule follows by substituting the linear approximation "
    "of the inner function into that of the outer function."
)

# ==========================================
# 2. CHAIN RULE I
# ==========================================

st.divider()
st.header("2. Chain Rule I — One Independent Variable")
st.markdown("**Theorem 2.26 (Folland).**")

st.markdown(
    "Suppose $g:I\\to U\\subseteq\\mathbb{R}^n$ is differentiable at "
    "$a\\in I$, and $f:U\\to\\mathbb{R}$ is differentiable at "
    "$b=g(a)$. Then $\\varphi=f\\circ g$ is differentiable at $a$, and"
)
st.latex(r"\boxed{\varphi'(a)=\nabla f(g(a))\cdot g'(a)}")

st.markdown("In coordinates, if $g(t)=(g_1(t),\\ldots,g_n(t))$:")
st.latex(
    r"\frac{d}{dt}f(g(t))="
    r"\sum_{j=1}^{n}\frac{\partial f}{\partial x_j}(g(t))\,g_j'(t)."
)
st.markdown(
    "Geometrically, $g(t)$ traces a curve in $\\mathbb{R}^n$. "
    "The vector $g'(t)$ is its velocity, and the dot product "
    "measures the rate of change of $f$ along the curve."
)

with st.expander("Proof — Chain Rule I (Folland, Theorem 2.26)", expanded=False):
    st.markdown("**Step 1. Write both differentiability expansions.**")
    st.latex(r"f(b+v)=f(b)+\nabla f(b)\cdot v+r_f(v),")
    st.latex(r"\frac{r_f(v)}{\|v\|}\longrightarrow 0\quad (v\to0).")
    st.latex(r"g(a+u)=b+u\,g'(a)+r_g(u),")
    st.latex(r"\frac{\|r_g(u)\|}{|u|}\longrightarrow 0\quad (u\to0).")

    st.markdown("**Step 2. Substitute the inner increment.**")
    st.latex(r"v(u):=g(a+u)-g(a)=u\,g'(a)+r_g(u).")
    st.latex(
        r"\begin{aligned}"
        r"\varphi(a+u)-\varphi(a)"
        r"&=f(b+v(u))-f(b)\\"
        r"&=u\,\nabla f(b)\cdot g'(a)"
        r"+\nabla f(b)\cdot r_g(u)+r_f(v(u))."
        r"\end{aligned}"
    )

    st.markdown("**Step 3. Show that both remainder terms are negligible.**")
    st.markdown("For the first remainder, the Cauchy–Schwarz inequality gives")
    st.latex(
        r"\frac{|\nabla f(b)\cdot r_g(u)|}{|u|}"
        r"\le \|\nabla f(b)\|\frac{\|r_g(u)\|}{|u|}"
        r"\longrightarrow 0."
    )
    st.markdown(
        "For sufficiently small nonzero $u$, the differentiability of $g$ "
        "implies $\\|r_g(u)\\|\\le |u|$. Consequently,"
    )
    st.latex(
        r"\frac{\|v(u)\|}{|u|}"
        r"\le \|g'(a)\|+1."
    )
    st.markdown(
        "Since $v(u)\\to0$ and $r_f(v)=o(\\|v\\|)$, we obtain "
        "(with the expression understood as zero when $v(u)=0$)"
    )
    st.latex(
        r"\frac{|r_f(v(u))|}{|u|}="
        r"\frac{|r_f(v(u))|}{\|v(u)\|}"
        r"\frac{\|v(u)\|}{|u|}\longrightarrow 0."
    )
    st.markdown("**Step 4. Take the difference quotient.**")
    st.latex(
        r"\frac{\varphi(a+u)-\varphi(a)}{u}"
        r"\longrightarrow \nabla f(b)\cdot g'(a)."
    )
    st.markdown("This proves the theorem.")

# ==========================================
# 3. CHAIN RULE II
# ==========================================

st.divider()
st.header("3. Chain Rule II — Several Independent Variables")
st.markdown("**Theorem 2.29 (Folland).**")

st.markdown(
    "Let $g=(g_1,\\ldots,g_n):V\\subseteq\\mathbb{R}^m\\to U$ "
    "and $f:U\\subseteq\\mathbb{R}^n\\to\\mathbb{R}$, where "
    "$U$ and $V$ are open. Suppose $g$ is differentiable at $a\\in V$ "
    "and $f$ is differentiable at $b=g(a)$. Then "
    "$\\varphi=f\\circ g$ is differentiable at $a$, and"
)
st.latex(
    r"\boxed{\frac{\partial\varphi}{\partial t_k}(a)="
    r"\sum_{j=1}^{n}"
    r"\frac{\partial f}{\partial x_j}(g(a))"
    r"\frac{\partial g_j}{\partial t_k}(a)}"
)
st.markdown(
    "Here $t_1,\\ldots,t_m$ are the independent variables, "
    "and $g_1,\\ldots,g_n$ are the intermediate variables. "
    "Differentiability of the component functions $g_j$ at $a$ "
    "is equivalent to differentiability of the vector-valued map $g$ there."
)

with st.expander("Proof — Chain Rule II (full proof)", expanded=False):
    st.markdown(
        "Folland states this theorem without writing out the general proof. "
        "Here is the argument using the same linear-approximation idea "
        "as in Chain Rule I."
    )
    st.markdown("**Step 1. Differentiate both maps in the linear sense.**")
    st.latex(
        r"g(a+h)=b+Dg(a)h+r_g(h),\qquad"
        r"\frac{\|r_g(h)\|}{\|h\|}\to0."
    )
    st.latex(
        r"f(b+v)=f(b)+Df(b)[v]+r_f(v),\qquad"
        r"\frac{r_f(v)}{\|v\|}\to0."
    )
    st.markdown(
        "The symbols $Dg(a)$ and $Df(b)$ denote the linear maps "
        "that provide the first-order approximations."
    )

    st.markdown("**Step 2. Compose the expansions.**")
    st.latex(r"v(h):=g(a+h)-b=Dg(a)h+r_g(h).")
    st.latex(
        r"\begin{aligned}"
        r"\varphi(a+h)-\varphi(a)"
        r"&=Df(b)[v(h)]+r_f(v(h))\\"
        r"&=Df(b)[Dg(a)h]"
        r"+Df(b)[r_g(h)]+r_f(v(h))."
        r"\end{aligned}"
    )

    st.markdown("**Step 3. Control the remainder terms.**")
    st.markdown("Since a linear map in finite dimensions is bounded,")
    st.latex(
        r"\frac{|Df(b)[r_g(h)]|}{\|h\|}"
        r"\le\|Df(b)\|\frac{\|r_g(h)\|}{\|h\|}"
        r"\longrightarrow0."
    )
    st.markdown(
        "For sufficiently small $h\\ne0$, "
        "$\\|r_g(h)\\|\\le\\|h\\|$, and therefore"
    )
    st.latex(
        r"\frac{\|v(h)\|}{\|h\|}\le\|Dg(a)\|+1."
    )
    st.latex(
        r"\frac{|r_f(v(h))|}{\|h\|}"
        r"=\frac{|r_f(v(h))|}{\|v(h)\|}"
        r"\frac{\|v(h)\|}{\|h\|}\longrightarrow0."
    )
    st.caption(
        "As above, the product is taken to be zero when v(h) = 0."
    )

    st.markdown("**Step 4. Identify the derivative.**")
    st.latex(
        r"\boxed{D(f\circ g)(a)=Df(g(a))\circ Dg(a).}"
    )
    st.markdown(
        "Applying this linear map to the coordinate vector $e_k$ "
        "produces the formula for $\\partial\\varphi/\\partial t_k$."
    )

st.markdown("**Matrix interpretation (optional).**")
st.latex(
    r"Dg(a)=\left(\frac{\partial g_j}{\partial t_k}(a)\right)"
    r"_{\substack{1\le j\le n\\1\le k\le m}}"
    r"\in\mathbb{R}^{n\times m}."
)
st.latex(
    r"D\varphi(a)="
    r"\underbrace{Df(g(a))}_{1\times n}"
    r"\underbrace{Dg(a)}_{n\times m}."
)
st.markdown(
    "This is the familiar Jacobian matrix formulation. "
    "The order of multiplication matters."
)

# ==========================================
# 4. WORKED EXAMPLE FROM FOLLAND
# ==========================================

st.divider()
st.header("4. Worked Example — Folland, Example 2")

st.markdown(
    "Let $f(x,y)$ be differentiable, and define two intermediate variables:"
)
st.latex(r"x(s,t)=s\log(1+t^2),\qquad y(s,t)=\cos(s^3+5t).")
st.latex(r"z(s,t)=f\bigl(x(s,t),y(s,t)\bigr).")

st.markdown("The partial derivatives of the intermediate variables are")
st.latex(
    r"\begin{aligned}"
    r"x_s&=\log(1+t^2), & x_t&=\frac{2st}{1+t^2},\\"
    r"y_s&=-3s^2\sin(s^3+5t), & y_t&=-5\sin(s^3+5t)."
    r"\end{aligned}"
)

with st.expander("Derivation — apply the chain rule", expanded=False):
    st.latex(r"z_s=f_x(x,y)x_s+f_y(x,y)y_s.")
    st.latex(
        r"\boxed{\frac{\partial z}{\partial s}="
        r"f_x(x,y)\log(1+t^2)"
        r"-3s^2f_y(x,y)\sin(s^3+5t)}"
    )
    st.latex(r"z_t=f_x(x,y)x_t+f_y(x,y)y_t.")
    st.latex(
        r"\boxed{\frac{\partial z}{\partial t}="
        r"f_x(x,y)\frac{2st}{1+t^2}"
        r"-5f_y(x,y)\sin(s^3+5t)}"
    )
    st.markdown(
        "In these expressions, $f_x$ and $f_y$ are evaluated at "
        "$(x,y)=(s\\log(1+t^2),\\cos(s^3+5t))$, "
        "not at $(s,t)$."
    )

# ==========================================
# 5. INTERACTIVE WORKED EXAMPLE
# ==========================================

st.divider()
st.header("5. Interactive Example — Verify the Formula")
st.markdown(
    "We now choose explicit functions and compare the result of "
    "the chain rule with direct differentiation."
)
st.latex(r"f(x,y)=x^2+3xy,\qquad g(s,t)=(s+t^2,st).")
st.latex(r"\varphi(s,t)=f(g(s,t))=(s+t^2)^2+3(s+t^2)st.")

left, right = st.columns(2, gap="large")
with left:
    s = st.slider("Choose s", min_value=-2.0, max_value=2.0,
                  value=1.0, step=0.25)
with right:
    t = st.slider("Choose t", min_value=-2.0, max_value=2.0,
                  value=1.0, step=0.25)

x = s + t**2
y = s * t
fx = 2 * x + 3 * y
fy = 3 * x
dphi_ds = fx + t * fy
dphi_dt = 2 * t * fx + s * fy

# These formulas are obtained by differentiating the expanded composition.
direct_ds = 2 * x + 3 * t * (2 * s + t**2)
direct_dt = 4 * t * x + 3 * s * (x + 2 * t**2)

st.markdown("**Step 1. Evaluate the intermediate variables and the outer gradient.**")
st.latex(rf"g(s,t)=({x:.2f},{y:.2f})")
st.latex(rf"\nabla f(g(s,t))=({fx:.2f},{fy:.2f})")

st.markdown("**Step 2. Compute the Jacobian of the inner function.**")
st.latex(r"Dg(s,t)=\begin{pmatrix}1&2t\\t&s\end{pmatrix}")
st.latex(
    rf"Dg(s,t)=\begin{{pmatrix}}"
    rf"1&{2*t:.2f}\\{t:.2f}&{s:.2f}"
    rf"\end{{pmatrix}}"
)

st.markdown("**Step 3. Multiply the derivatives.**")
st.latex(r"D\varphi(s,t)=Df(g(s,t))\,Dg(s,t)")
st.latex(
    rf"D\varphi(s,t)=\begin{{pmatrix}}"
    rf"{dphi_ds:.2f}&{dphi_dt:.2f}"
    rf"\end{{pmatrix}}"
)

st.markdown("**Direct differentiation gives the same answer:**")
st.latex(
    rf"\left(\partial_s\varphi,\partial_t\varphi\right)"
    rf"=({direct_ds:.2f},{direct_dt:.2f})."
)

if abs(dphi_ds - direct_ds) < 1e-10 and abs(dphi_dt - direct_dt) < 1e-10:
    st.success("The chain rule agrees with direct differentiation.")

# ==========================================
# 6. DIRECT AND INDIRECT DEPENDENCE
# ==========================================

st.divider()
st.header("6. Direct and Indirect Dependence")
st.markdown(
    "An independent variable can appear both inside the intermediate "
    "variables and explicitly in the outer function. "
    "For example, consider"
)
st.latex(r"w(t)=f(x(t),y(t),t).")
st.markdown("The chain rule must account for **every** dependence on $t$:")
st.latex(
    r"\boxed{\frac{dw}{dt}="
    r"\frac{\partial f}{\partial x}\,x'(t)"
    r"+\frac{\partial f}{\partial y}\,y'(t)"
    r"+\frac{\partial f}{\partial t}}"
)
st.markdown(
    "The last term describes the explicit dependence of $f$ on "
    "its third argument; the first two describe the indirect dependence "
    "through $x(t)$ and $y(t)$."
)

with st.expander("Example — direct and indirect dependence", expanded=False):
    st.latex(
        r"f(x,y,t)=x^2y+tx,\qquad x(t)=t^2,\quad y(t)=\sin t."
    )
    st.latex(r"w(t)=t^4\sin t+t^3.")
    st.markdown("Differentiating the expression directly gives")
    st.latex(r"w'(t)=4t^3\sin t+t^4\cos t+3t^2.")
    st.markdown("The multivariable chain rule gives the same result:")
    st.latex(
        r"\begin{aligned}"
        r"w'(t)&=f_x x'(t)+f_y y'(t)+f_t\\"
        r"&=(2xy+t)(2t)+x^2\cos t+x\\"
        r"&=4t^3\sin t+t^4\cos t+3t^2."
        r"\end{aligned}"
    )

# ==========================================
# 7. DIFFERENTIAL INTERPRETATION
# ==========================================

st.divider()
st.header("7. Why the Differential Notation Works")
st.markdown(
    "Folland also expresses the chain rule using differentials. "
    "The rigorous interpretation is that the differential at a point "
    "is a **linear map**, not merely a formal symbol."
)
st.latex(r"df_b(v)=Df(b)[v]=\nabla f(b)\cdot v.")
st.latex(r"d(f\circ g)_a=df_{g(a)}\circ dg_a.")
st.markdown(
    "If $g=(g_1,\\ldots,g_n)$, the usual notation"
)
st.latex(r"dw=\sum_{j=1}^n\frac{\partial f}{\partial x_j}\,dx_j")
st.markdown(
    "is shorthand for an identity between linear maps. "
    "Substituting the differentials of the intermediate functions "
    "is valid precisely because linear maps compose."
)

# ==========================================
# 8. OPTIONAL APPLICATION
# ==========================================

st.divider()
st.header("8. Application — Euler's Theorem")
st.markdown(
    "The chain rule leads to a useful identity for homogeneous functions "
    "(Folland, Theorem 2.36). A function $f$ is homogeneous of degree "
    "$\\alpha$ if"
)
st.latex(r"f(tx)=t^\alpha f(x)\qquad(t>0).")
st.markdown("If $f$ is differentiable at $x\\ne0$, then")
st.latex(
    r"\boxed{\sum_{j=1}^n x_j\frac{\partial f}{\partial x_j}(x)"
    r"=\alpha f(x).}"
)

with st.expander("Proof — Euler's Theorem", expanded=False):
    st.markdown("Fix $x\\ne0$ and define $\\psi(t)=f(tx)$ for $t>0$.")
    st.markdown("By homogeneity,")
    st.latex(r"\psi'(1)=\left.\frac{d}{dt}t^\alpha f(x)\right|_{t=1}=\alpha f(x).")
    st.markdown("On the other hand, the chain rule gives")
    st.latex(r"\psi'(1)=\nabla f(x)\cdot x.")
    st.markdown("Equating the two expressions proves the identity.")

st.divider()
st.caption(
    "Reference: G. B. Folland, Advanced Calculus, 2nd edition, "
    "§2.3, Theorems 2.26, 2.29, and 2.36. "
    "The full proof of Theorem 2.29 and the interactive example "
    "are additional explanations written for Math Lab."
)
