import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.markdown("""
<style>
button[kind="primary"] {
    background-color: #E63946 !important;
    color: white !important;
    border: none !important;
    font-weight: 600 !important;
}

button[kind="primary"]:hover {
    background-color: #C62839 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# MATPLOTLIB STYLE
# ==========================================

def style_axes(ax):
    ax.set_facecolor("black")
    ax.tick_params(colors="white", labelsize=9)

    for spine in ax.spines.values():
        spine.set_color("#777777")

    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")

    ax.grid(True, color="#444444", alpha=0.35)


# ==========================================
# FUNCTION
# ==========================================

def f(x):
    return x**2


# ==========================================
# 1. SLOPE
# ==========================================

st.subheader("Motivation — The Origins of Differentiation")

st.markdown(r"""
The concept of differentiation emerged in the 17th century,
most notably through the work of **Isaac Newton and
Gottfried Wilhelm Leibniz**. One of the fundamental questions was: **How can we measure the instantaneous rate of change?**
This seems almost paradoxical. Change requires an interval,
yet we want to measure it at a single instant.
For example, how can we determine the exact velocity
of an object at a particular moment?
The key idea is to measure change over increasingly
smaller intervals and investigate what happens as
the interval approaches zero.
This leads naturally to the concept of a **limit**,
and ultimately, to the **derivative**.
""")


st.title("Derivatives — Intuition & Definition")

# ==========================================
# 1. SLOPE
# ==========================================

st.header("1. Slope")


def draw_slope():

    fig, ax = plt.subplots(
        figsize=(6, 3.4),
        facecolor="black"
    )

    style_axes(ax)

    x = np.linspace(0, 6, 300)
    y = 0.75*x + 1

    ax.plot(
        x, y,
        color="#00BFFF",
        linewidth=2.5
    )

    xA, xB = 1, 4.5
    yA, yB = 0.75*xA + 1, 0.75*xB + 1

    ax.scatter(
        [xA, xB],
        [yA, yB],
        color="#FF5555",
        s=65,
        zorder=5
    )

    ax.plot(
        [xA, xB],
        [yA, yA],
        "--",
        color="#FFD166",
        linewidth=1.5
    )

    ax.plot(
        [xB, xB],
        [yA, yB],
        "--",
        color="#FFD166",
        linewidth=1.5
    )

    ax.text(
        xA-0.2, yA+0.3, "A",
        color="white", fontsize=11
    )

    ax.text(
        xB+0.1, yB+0.2, "B",
        color="white", fontsize=11
    )

    ax.text(
        (xA+xB)/2,
        yA-0.35,
        r"$\Delta x$",
        color="#FFD166",
        ha="center",
        fontsize=12
    )

    ax.text(
        xB+0.15,
        (yA+yB)/2,
        r"$\Delta y$",
        color="#FFD166",
        fontsize=12
    )

    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)

    ax.set_xlabel("x")
    ax.set_ylabel("y")

    fig.tight_layout()

    return fig


# ==========================================
# TWO-COLUMN LAYOUT
# ==========================================

text_col, plot_col = st.columns(
    [1, 1.5],
    gap="large",
    vertical_alignment="center"
)

# LEFT: Explanation
with text_col:

    st.markdown("""
The **slope** measures how steep a straight line is.

It describes the ratio between the vertical
change and the horizontal change between two points.
""")

    st.latex(
    r"\frac{\text{vertical change}}{\text{horizontal change}} = \frac{\Delta y}{\Delta x}"
)

    st.markdown("""
The slope is constant along a straight line.

For a curved function, however, the slope between
two points generally depends on which points
we choose.

This motivates the **derivative**.
""")


# RIGHT: Figure
with plot_col:

    slope_fig = draw_slope()

    st.pyplot(
        slope_fig,
        use_container_width=True
    )

    plt.close(slope_fig)


st.divider()



# ==========================================
# 2. DERIVATIVE — DEFINITION
# ==========================================

st.header("2. Derivative — Definition")

def draw_secant_explanation():

    fig, ax = plt.subplots(
        figsize=(6.2, 4.2),
        facecolor="black"
    )

    style_axes(ax)

    # Curve
    xs = np.linspace(-0.2, 2.8, 400)
    ys = xs**2
    ax.plot(xs, ys, color="#00BFFF", linewidth=2.5)

    # Chosen points
    x0 = 1.0
    h = 0.9
    x1 = x0 + h

    y0 = x0**2
    y1 = x1**2

    # Secant line
    m = (y1 - y0) / (x1 - x0)
    secant_y = y0 + m * (xs - x0)
    ax.plot(xs, secant_y, color="#FF9F43", linewidth=2.2)

    # Points
    ax.scatter([x0, x1], [y0, y1], color="#FF5555", s=65, zorder=5)

    ax.text(x0 - 0.18, y0 - 0.35, "P", color="white", fontsize=11)
    ax.text(x1 + 0.05, y1 + 0.10, "Q", color="white", fontsize=11)

    # Horizontal difference
    ax.plot(
        [x0, x1],
        [y0, y0],
        "--",
        color="#FFD166",
        linewidth=1.5
    )

    # Vertical difference
    ax.plot(
        [x1, x1],
        [y0, y1],
        "--",
        color="#FFD166",
        linewidth=1.5
    )

    ax.text(
        (x0 + x1)/2,
        y0 - 0.45,
        r"$h$",
        color="#FFD166",
        ha="center",
        fontsize=12
    )

    ax.text(
        x1 + 0.08,
        (y0 + y1)/2,
        r"$f(x_0+h)-f(x_0)$",
        color="#FFD166",
        fontsize=11,
        va="center"
    )

    ax.text(
        x0 - 0.05,
        y0 + 0.18,
        r"$x_0$",
        color="white",
        fontsize=10
    )

    ax.text(
        x1 - 0.12,
        y1 + 0.18,
        r"$x_0+h$",
        color="white",
        fontsize=10
    )

    ax.text(
        1.75,
        0.55,
        "secant line",
        color="#FF9F43",
        fontsize=10
    )

    ax.set_xlim(-0.1, 2.6)
    ax.set_ylim(-0.2, 4.8)

    ax.set_xlabel("x")
    ax.set_ylabel("y")

    fig.tight_layout()
    return fig


text_col, plot_col = st.columns(
    [1, 1.7],
    gap="large",
    vertical_alignment="center"
)

with text_col:

    st.markdown("Consider the function")

    st.latex(r"f(x)=x^2.")

    st.markdown(
    r"Choose a fixed point $x_0$ and a second point $x_0+h$."
    )

    st.markdown(
        "The slope of the **secant line** is computed as:"
    )

    st.latex(
        r"\frac{\text{vertical change}}{\text{horizontal change}}"
    )

    st.markdown(
        "In this case, the vertical change is:"
    )

    st.latex(r"f(x_0+h)-f(x_0)")

    st.markdown(
        "and the horizontal change is:"
    )

    st.latex(r"(x_0+h)-x_0=h")

    st.markdown(
        "Therefore, the secant slope is:"
    )

    st.latex(
        r"\frac{f(x_0+h)-f(x_0)}{h}"
    )

    st.markdown(
        """
As the second point approaches the first, the
secant line approaches the tangent line.
"""
    )



with plot_col:

    secant_fig = draw_secant_explanation()

    st.pyplot(
        secant_fig,
        use_container_width=True
    )

    plt.close(secant_fig)

# ==========================================
# DERIVATIVE DEFINITION — CENTERED
# ==========================================

st.markdown(
    "<h3 style='text-align: center;'>"
    "This leads to the derivative:"
    "</h3>",
    unsafe_allow_html=True
)

st.latex(
    r"\boxed{f'(x_0)=\lim_{h\to 0}"
    r"\frac{f(x_0+h)-f(x_0)}{h}}"
)

st.divider()

# ==========================================
# SLIDERS
# ==========================================

st.subheader("Interactive Visualization")

col1, col2 = st.columns(2)

with col1:
    x0 = st.slider(
        "Choose x₀ — Derivative location",
        min_value=-2.0,
        max_value=2.0,
        value=1.0,
        step=0.1
    )

with col2:
    x1 = st.slider(
        "Choose x₁ — Second point",
        min_value=-2.5,
        max_value=2.5,
        value=2.0,
        step=0.1
    )


h_initial = x1 - x0

if abs(h_initial) < 1e-10:
    st.warning(
        "Choose two different points before starting."
    )


# ==========================================
# CREATE DERIVATIVE GRAPH
# ==========================================

def create_derivative_graph(x0, x1):

    fig, ax = plt.subplots(
        figsize=(6.5, 4),
        facecolor="black"
    )

    style_axes(ax)

    xs = np.linspace(-2.75, 2.75, 600)

    # Function
    ax.plot(
        xs,
        f(xs),
        color="#00BFFF",
        linewidth=2.6,
        label=r"$f(x)=x^2$"
    )

    y0 = f(x0)
    y1 = f(x1)

    # For x^2:
    # (f(x0+h)-f(x0))/h = 2*x0+h

    h = x1 - x0
    secant_slope = 2*x0 + h
    tangent_slope = 2*x0

    # Tangent line
    tangent_y = y0 + tangent_slope*(xs-x0)

    tangent_line, = ax.plot(
        xs,
        tangent_y,
        color="#A78BFA",
        linestyle="--",
        linewidth=2,
        label="Tangent line"
    )

    # Secant line
    secant_y = y0 + secant_slope*(xs-x0)

    secant_line, = ax.plot(
        xs,
        secant_y,
        color="#FF9F43",
        linewidth=2.2,
        label="Secant line"
    )

    # Fixed point P
    ax.scatter(
        [x0], [y0],
        color="#FF5555",
        s=75,
        zorder=6
    )

    ax.annotate(
        "P",
        (x0, y0),
        xytext=(-15, 12),
        textcoords="offset points",
        color="white",
        fontsize=11
    )

    # Moving point Q
    moving_point, = ax.plot(
        [x1], [y1],
        "o",
        color="#FFD166",
        markersize=8,
        zorder=7
    )

    q_label = ax.annotate(
        "Q",
        (x1, y1),
        xytext=(10, 12),
        textcoords="offset points",
        color="white",
        fontsize=11
    )

    ax.set_xlim(-2.75, 2.75)
    ax.set_ylim(-0.8, 8)

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    legend = ax.legend(
        facecolor="#111111",
        edgecolor="#555555",
        loc="upper center",
        fontsize=9
    )

    for txt in legend.get_texts():
        txt.set_color("white")

    fig.tight_layout()

    return (
        fig,
        xs,
        secant_line,
        moving_point,
        q_label
    )



# ==========================================
# GRAPH AND CONTROLS LAYOUT
# ==========================================

left_col, right_col = st.columns(
    [1, 2.5],
    gap="large"
)

# Create the figure only once
fig, xs, secant_line, moving_point, q_label = (
    create_derivative_graph(x0, x1)
)

# ==========================================
# LEFT SIDE: BUTTON + CURRENT VALUES
# ==========================================

with left_col:

    start = st.button(
        "▶ Start Animation",
        type="primary",
        disabled=abs(h_initial) < 1e-10,
        use_container_width=True
    )

    st.markdown("### Current Values")

    values_placeholder = st.empty()

    initial_slope = x0 + x1

    values_placeholder.markdown(
        rf"""
- $x_0={x0:.3f}$
- $h={h_initial:.3f}$
- **Secant slope:** {initial_slope:.4f}
- **Tangent slope:** {2*x0:.4f}
"""
    )


# ==========================================
# RIGHT SIDE: GRAPH
# ==========================================

with right_col:

    graph_placeholder = st.empty()

    graph_placeholder.pyplot(
        fig,
        clear_figure=False,
        use_container_width=True
    )


# ==========================================
# ANIMATION
# ==========================================

if start:

    frames = 55

    for i in range(frames):

        t = i / (frames - 1)

        remaining = 0.001 + 0.999*(1-t)**2

        h_current = h_initial * remaining

        x1_current = x0 + h_current

        y0 = f(x0)
        y1_current = f(x1_current)

        slope_current = 2*x0 + h_current

        # Update secant line
        new_secant_y = (
            y0 + slope_current*(xs-x0)
        )

        secant_line.set_ydata(new_secant_y)

        # Update moving point
        moving_point.set_data(
            [x1_current],
            [y1_current]
        )

        q_label.xy = (
            x1_current,
            y1_current
        )

        q_label.set_visible(
            abs(h_current) > 0.08
        )

        # Update graph in its original position
        graph_placeholder.pyplot(
            fig,
            clear_figure=False,
            use_container_width=True
        )

        # Update values on the left
        values_placeholder.markdown(
            rf"""
- \(x_0={x0:.3f}\)
- \(h={h_current:.5f}\)
- **Secant slope:** {slope_current:.5f}
- **Tangent slope:** {2*x0:.5f}
"""
        )

        time.sleep(0.055)

    with left_col:
        st.success(
            "Secant line has approached the tangent!"
        )

plt.close(fig)




# ==========================================
# MATHEMATICAL CONCLUSION
# ==========================================

st.divider()

st.subheader("Sample calculation")

st.markdown(r"""
For the function $f(x)=x^2$, we can explicitly
calculate the difference quotient:
""")

st.latex(r"""
\begin{aligned}
\frac{f(x_0+h)-f(x_0)}{h}
&= \frac{(x_0+h)^2-x_0^2}{h} \\[10pt]
&= \frac{x_0^2+2x_0h+h^2-x_0^2}{h} \\[10pt]
&= \frac{2x_0h+h^2}{h} \\[10pt]
&= 2x_0+h, \qquad h\neq 0.
\end{aligned}
""")

st.markdown(r"""
Taking the limit as $h\to 0$, we obtain:
""")

st.latex(r"""
\boxed{
f'(x_0)=\lim_{h\to 0}(2x_0+h)=2x_0
}
""")

st.markdown(r"""
Thus, the derivative of $f(x)=x^2$ at any point
$x_0\in\mathbb{R}$ is $f'(x_0)=2x_0$.
""")
