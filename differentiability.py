import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page configuration is handled by app.py.

st.markdown(
    """
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
    """,
    unsafe_allow_html=True,
)

st.title("Differentiability & Rules")
st.markdown(
    "We have seen how derivatives arise from secant slopes. "
    "Now we ask **when a derivative exists** and **how to compute it**."
)

# =========================================================
# 1. DEFINITION
# =========================================================

st.header("1. Differentiability — Definition")

st.markdown(
    r"""
**Definition.** Let $f$ be a real-valued function defined on an open
interval containing $x_0$. We say that $f$ is **differentiable at $x_0$**
if the following **finite limit exists**:
"""
)

st.latex(
    r"\boxed{f'(x_0)=\lim_{h\to0}"
    r"\frac{f(x_0+h)-f(x_0)}{h}.}"
)

st.markdown(
    r"""
Here $h\neq0$ in the difference quotient. Because $h\to0$ is a
**two-sided limit**, the left-hand and right-hand limits must both
exist and agree.
"""
)


# =========================================================
# 2. INTERACTIVE COUNTEREXAMPLE
# =========================================================

st.divider()

st.header("2. Does the Derivative Always Exist?")

st.markdown(
    "**No.** A classic counterexample is the absolute value function."
)

text_col, plot_col = st.columns(
    [1, 1.45],
    gap="large",
    vertical_alignment="center"
)

with text_col:

    st.latex(r"f(x)=|x|")

    st.markdown(
        r"""
At $x_0=0$, examine the difference quotient from both sides:
"""
    )

    st.latex(
        r"\lim_{h\to0^-}\frac{|h|}{h}=-1"
    )

    st.latex(
        r"\lim_{h\to0^+}\frac{|h|}{h}=1"
    )

    st.markdown(
        "Since these limits are different, "
        "**the derivative at zero does not exist**."
    )

    distance = st.slider(
        "Distance of the moving points from zero",
        min_value=0.05,
        max_value=1.50,
        value=1.00,
        step=0.05,
        key="abs_distance",
    )

    st.caption(
        "Move the slider toward zero to compare the two secants."
    )

    st.markdown(
        f"Left secant slope: **-1**  \n\n"
        f"Right secant slope: **+1**  \n\n"
        rf"Distance: $|h|={distance:.2f}$"
    )


with plot_col:

    fig, ax = plt.subplots(
        figsize=(7.2, 4.6),
        facecolor="black"
    )

    ax.set_facecolor("black")

    xs = np.linspace(-2.1, 2.1, 600)

    ax.plot(
        xs,
        np.abs(xs),
        color="#00BFFF",
        lw=2.8,
        label=r"$f(x)=|x|$"
    )

    # Left secant
    ax.plot(
        [-1.85, 0],
        [1.85, 0],
        color="#FF9F43",
        lw=2.2,
        ls="--",
        label="Left secant"
    )

    # Right secant
    ax.plot(
        [0, 1.85],
        [0, 1.85],
        color="#AD8BFA",
        lw=2.2,
        ls="--",
        label="Right secant"
    )

    # Fixed point
    ax.scatter(
        [0],
        [0],
        color="#FF5555",
        s=70,
        zorder=6
    )

    # Moving points
    ax.scatter(
        [-distance],
        [distance],
        color="#FF9F43",
        s=82,
        zorder=7
    )

    ax.scatter(
        [distance],
        [distance],
        color="#AD8BFA",
        s=82,
        zorder=7
    )

    ax.annotate(
        "P",
        (0, 0),
        xytext=(7, -17),
        textcoords="offset points",
        color="white",
        fontsize=11
    )

    ax.annotate(
        r"$Q_-$",
        (-distance, distance),
        xytext=(-24, 9),
        textcoords="offset points",
        color="#FF9F43",
        fontsize=12
    )

    ax.annotate(
        r"$Q_+$",
        (distance, distance),
        xytext=(9, 9),
        textcoords="offset points",
        color="#AD8BFA",
        fontsize=12
    )

    ax.axhline(
        0,
        color="#777777",
        lw=0.9
    )

    ax.axvline(
        0,
        color="#777777",
        lw=0.9
    )

    ax.set_xlim(-2, 2)
    ax.set_ylim(-0.35, 2.35)

    ax.set_xlabel("x", color="white")
    ax.set_ylabel("f(x)", color="white")

    ax.tick_params(colors="white")
    ax.grid(color="#555555", alpha=0.25)

    for spine in ax.spines.values():
        spine.set_color("#777777")

    legend = ax.legend(
        loc="upper center",
        facecolor="#111111",
        edgecolor="#666666",
        fontsize=9
    )

    for label in legend.get_texts():
        label.set_color("white")

    fig.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


st.info(
    "The moving points approach the same point, but the secant slopes "
    "approach different values. This is why a two-sided derivative cannot exist."
)


# =========================================================
# 3. CONTINUITY
# =========================================================

st.divider()

st.header("3. Differentiability and Continuity")

st.markdown(
    "**Theorem.** If a function is differentiable at a point, "
    "then it is continuous at that point."
)

st.latex(
    r"\boxed{\text{Differentiability at }x_0"
    r"\ \Longrightarrow\ \text{Continuity at }x_0}"
)

with st.expander(
    "Proof — Differentiability implies continuity"
):

    st.markdown(
        r"""
**Proof.** Since $f$ is differentiable at $x_0$, the difference quotient
has a finite limit $f'(x_0)$. For $h\neq0$,
"""
    )

    st.latex(
        r"f(x_0+h)-f(x_0)="
        r"h\,\frac{f(x_0+h)-f(x_0)}{h}."
    )

    st.markdown(
        r"""
As $h\to0$, the first factor tends to zero and the second
factor tends to the finite number $f'(x_0)$. Therefore,
"""
    )

    st.latex(
        r"\lim_{h\to0}"
        r"\bigl(f(x_0+h)-f(x_0)\bigr)=0."
    )

    st.markdown(
        r"Hence $f$ is continuous at $x_0$. $\square$"
    )


st.markdown(
    r"""
**Is the converse true?** No. The function $f(x)=|x|$ is continuous at
zero, but, as we saw above, it is not differentiable there.
"""
)


# =========================================================
# 4. DIFFERENTIATION RULES
# =========================================================

st.divider()

st.header("4. Differentiation Rules — Theory & Proof")

st.markdown(
    r"Throughout this section, assume that $f$ and $g$ are "
    r"differentiable at the point in question."
)


# =========================================================
# 4.1 LINEARITY
# =========================================================

st.subheader("4.1 Constant, Scalar Multiple & Sum Rules")

st.latex(
    r"\boxed{(c)'=0,\qquad (cf)'=cf',\qquad (f+g)'=f'+g'}"
)

with st.expander("Proof — Linearity"):

    st.markdown(
        r"""
**Proof.** The difference quotient of a constant is zero.
For a scalar $c$ we can take the constant outside the limit:
"""
    )

    st.latex(
        r"\begin{aligned}"
        r"(cf)'(x_0)"
        r"&=\lim_{h\to0}"
        r"\frac{cf(x_0+h)-cf(x_0)}{h}\\"
        r"&=c\,f'(x_0)."
        r"\end{aligned}"
    )

    st.markdown(
        "Similarly, the limit of a sum is the sum of the limits:"
    )

    st.latex(
        (r"""\begin{aligned}
        (f+g)'(x_0)
        &=\lim_{h\to0}
        \frac{(f+g)(x_0+h)-(f+g)(x_0)}{h}\\[8pt]
        &=\lim_{h\to0}\left(\frac{f(x_0+h)-f(x_0)}{h}
        +\frac{g(x_0+h)-g(x_0)}{h}
        \right)\\[8pt]
        &=f'(x_0)+g'(x_0).
        \end{aligned}
        """)

    )

    st.markdown(r"$\square$")


# =========================================================
# 4.2 PRODUCT RULE
# =========================================================

st.subheader("4.2 Product Rule")

st.latex(
    r"\boxed{(fg)'(x)=f'(x)g(x)+f(x)g'(x)}"
)


with st.expander("Proof — Product Rule"):

    st.markdown(r"""
**Proof.** By the definition of the derivative,
""")

    st.latex(r"""
(fg)'(x_0)
=\lim_{h\to0}
\frac{(fg)(x_0+h)-(fg)(x_0)}{h}.
""")

    st.markdown(r"""
For $h\neq 0$, expanding the products gives
""")

    st.latex(r"""
\frac{
f(x_0+h)g(x_0+h)-f(x_0)g(x_0)
}{h}.
""")

    st.markdown(r"""
Now add and subtract $f(x_0+h)g(x_0)$
in the numerator:
""")

    st.latex(r"""
\frac{
\begin{aligned}
f(x_0+h)g(x_0+h)-f(x_0+h)g(x_0)
+f(x_0+h)g(x_0)-f(x_0)g(x_0)
\end{aligned}
}{h}.
""")

    st.markdown(r"""
Grouping the terms and factoring, we obtain
""")

    st.latex(r"""
\begin{aligned}
f(x_0+h)
\frac{g(x_0+h)-g(x_0)}{h}
+g(x_0)
\frac{f(x_0+h)-f(x_0)}{h}.
\end{aligned}
""")

    st.markdown(r"""
Finally, since differentiability implies continuity,
$f(x_0+h)\to f(x_0)$ as $h\to0$.

Taking the limit and applying the definition
of the derivative yields
""")

    st.latex(r"""
\begin{aligned}
(fg)'(x_0)
&=\lim_{h\to0}
\left[
f(x_0+h)
\frac{g(x_0+h)-g(x_0)}{h}
\right]\\[10pt]
&\quad+\lim_{h\to0}
\left[
g(x_0)
\frac{f(x_0+h)-f(x_0)}{h}
\right]\\[10pt]
&=f(x_0)g'(x_0)+f'(x_0)g(x_0).
\end{aligned}
""")

    st.markdown(r"$\square$")


# =========================================================
# 4.3 QUOTIENT RULE
# =========================================================

st.subheader("4.3 Quotient Rule")

st.latex(
    r"\boxed{\left(\frac{f}{g}\right)'(x)="
    r"\frac{f'(x)g(x)-f(x)g'(x)}{g(x)^2},"
    r"\quad g(x)\neq0}"
)

with st.expander("Proof — Quotient Rule"):

    st.markdown(
        r"""
**Proof.** Assume $g(x_0)\neq0$.

By continuity, $g(x_0+h)\neq0$
for all sufficiently small $h$. First,
"""
    )

    st.latex(r"""
\left(\frac{1}{g}\right)'(x_0)
=
\lim_{h\to0}
\frac{
\frac{1}{g(x_0+h)}-\frac{1}{g(x_0)}
}{h}
""")

    st.markdown(
        "Combining the fractions in the numerator gives"
    )

    st.latex(r"""
\lim_{h\to0}
\frac{
g(x_0)-g(x_0+h)
}{
h\,g(x_0+h)g(x_0)
}
""")

    st.markdown(
        "Factoring out the minus sign, we obtain"
    )

    st.latex(r"""
-\lim_{h\to0}
\left[
\frac{g(x_0+h)-g(x_0)}{h}
\cdot
\frac{1}{g(x_0+h)g(x_0)}
\right]
""")

    st.markdown(r"""
Since differentiability implies continuity,
$g(x_0+h)\to g(x_0)$.

Applying the limit laws and the definition
of the derivative yields
""")

    st.latex(r"""
\boxed{
\left(\frac1g\right)'(x_0)
=
-\frac{g'(x_0)}{g(x_0)^2}
}
""")


    st.markdown(
        r"Apply the product rule to $f\cdot(1/g)$:"
    )

    
    st.latex(r"""
\boxed{
\begin{aligned}
\left(\frac{f}{g}\right)'(x_0)
=\frac{f'(x_0)}{g(x_0)}
-\frac{f(x_0)g'(x_0)}{g(x_0)^2}
=\frac{f'(x_0)g(x_0)-f(x_0)g'(x_0)}
{g(x_0)^2}.
\end{aligned}
}
""")


    st.markdown(r"$\square$")
