import ast
import operator

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import sympy as sp


x = sp.Symbol("x", real=True)

# ==========================================
# MATHEMATICAL FUNCTIONS
# ==========================================

FUNCTIONS = {
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "exp": sp.exp,
    "log": sp.log,
    "sqrt": sp.sqrt,
}

CONSTANTS = {
    "x": x,
    "pi": sp.pi,
    "E": sp.E,
}

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


# ==========================================
# FUNCTION INPUT
# ==========================================

def read_function(text):

    text = text.strip().replace("^", "**")

    if not text or len(text) > 120:
        raise ValueError("Formula must be at most 120 characters.")

    tree = ast.parse(text, mode="eval")

    if len(list(ast.walk(tree))) > 60:
        raise ValueError("Formula is too complex.")

    def convert(node):

        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            if not np.isfinite(node.value) or abs(node.value) > 10000:
                raise ValueError("Numerical constant is too large.")
            return sp.sympify(node.value)

        if isinstance(node, ast.Name) and node.id in CONSTANTS:
            return CONSTANTS[node.id]

        if isinstance(node, ast.UnaryOp) and isinstance(
            node.op, (ast.UAdd, ast.USub)
        ):
            value = convert(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value

        if isinstance(node, ast.BinOp):

            left = convert(node.left)
            right = convert(node.right)

            if isinstance(node.op, ast.Pow):

                if right.is_number is not True or right.is_real is not True:
                    raise ValueError("Exponent must be a real constant.")

                exponent = float(right)

                if not np.isfinite(exponent) or abs(exponent) > 12:
                    raise ValueError("Exponent must be between -12 and 12.")

                return left ** right

            operation = OPERATORS.get(type(node.op))

            if operation is not None:
                return operation(left, right)

        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in FUNCTIONS
            and len(node.args) == 1
            and not node.keywords
        ):
            return FUNCTIONS[node.func.id](convert(node.args[0]))

        raise ValueError(
            "Unsupported notation. Try sin(x), x**2, exp(x)."
        )

    result = convert(tree.body)

    if sp.count_ops(result) > 120:
        raise ValueError("Formula is too complex.")

    return result


# ==========================================
# TAYLOR POLYNOMIAL
# ==========================================

def taylor_polynomial(function, center, degree):

    derivative = function
    polynomial = sp.Integer(0)

    for k in range(degree + 1):

        coefficient = (
            derivative.subs(x, center) / sp.factorial(k)
        )

        if (
            coefficient.is_finite is not True
            or coefficient.is_real is not True
        ):
            raise ValueError(
                "The Taylor polynomial does not exist at this point."
            )

        polynomial += coefficient * (x - center) ** k

        if k < degree:
            derivative = sp.diff(derivative, x)

    return polynomial


# ==========================================
# NUMERICAL EVALUATION
# ==========================================

def plot_values(expression, points):

    evaluator = sp.lambdify(
        x, expression, modules="numpy"
    )

    with np.errstate(all="ignore"):

        values = np.asarray(
            evaluator(points), dtype=np.complex128
        )

        values = np.broadcast_to(
            values, points.shape
        )

        result = values.real.copy()

        invalid = (
            ~np.isfinite(values.real)
            | ~np.isfinite(values.imag)
            | (np.abs(values.imag) > 1e-9)
            | (np.abs(result) > 1e50)
        )

        result[invalid] = np.nan

    return result


# ==========================================
# STREAMLIT INTERFACE
# ==========================================

st.title("📊 Taylor Error Analysis")

st.write(
    "Compare a function with its Taylor polynomial "
    "and examine the absolute approximation error."
)

choices = [
    "sin(x)",
    "cos(x)",
    "exp(x)",
    "log(1+x**2)",
    "1/(1+x**2)",
    "Custom function",
]

choice = st.selectbox(
    "Function",
    choices
)

if choice == "Custom function":

    formula = st.text_input(
        "Enter f(x)",
        value="sin(x)*exp(-x**2)"
    )

else:
    formula = choice

st.caption(
    "Notation: x**2, 2*x, sin(x), cos(x), "
    "exp(x), log(x), sqrt(x), pi"
)


# ==========================================
# SLIDERS
# ==========================================

left, right = st.columns(2)

with left:

    a = st.slider(
        "Expansion point (a)",
        min_value=-3.0,
        max_value=3.0,
        value=0.0,
        step=0.25
    )

with right:

    n = st.slider(
        "Polynomial degree (n)",
        min_value=0,
        max_value=20,
        value=4
    )


# ==========================================
# MATHEMATICAL CALCULATIONS
# ==========================================

try:

    f = read_function(formula)

    center = sp.Rational(str(a))

    polynomial = taylor_polynomial(
        f, center, n
    )

    # Large domain for interactive zooming
    xs = np.linspace(
        a - 60,
        a + 60,
        6001
    )

    f_values = plot_values(f, xs)

    t_values = plot_values(polynomial, xs)

    # Absolute approximation error
    with np.errstate(all="ignore"):
        errors = np.abs(f_values - t_values)

    errors[~np.isfinite(errors)] = np.nan

    f_at_a = float(
        sp.N(f.subs(x, center))
    )

    if not np.isfinite(f_at_a):
        raise ValueError(
            "Function is not finite at the expansion point."
        )

except (
    ValueError,
    SyntaxError,
    TypeError,
    ZeroDivisionError,
    OverflowError
) as error:

    st.error(
        f"Could not calculate approximation: {error}"
    )
    st.stop()


# ==========================================
# FORMULAS
# ==========================================

st.latex(
    r"f(x)=" + sp.latex(f)
)

with st.expander("Calculated Taylor polynomial"):

    st.latex(
        r"T_{" + str(n) + r"}(x;a)="
        + sp.latex(polynomial)
    )


# ==========================================
# VISUALIZATION
# ==========================================

RED = "#FF304F"
GREEN = "#39FF73"
YELLOW = "#F5C451"
ORANGE = "#FFB347"
TEXT = "#E8EDF5"


# Create two vertically stacked graphs
fig = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.13,
    row_heights=[0.62, 0.38],
    subplot_titles=(
        "Original Function and Taylor Approximation",
        "Absolute Approximation Error"
    )
)


# ==========================================
# GRAPH 1: ORIGINAL FUNCTION
# ==========================================

fig.add_trace(
    go.Scatter(
        x=xs,
        y=f_values,
        mode="lines",
        name="Original function",
        line=dict(
            color=RED,
            width=2.8
        ),
        hovertemplate=(
            "x = %{x:.3f}<br>"
            "f(x) = %{y:.6g}"
            "<extra></extra>"
        )
    ),
    row=1,
    col=1
)


# Taylor approximation
fig.add_trace(
    go.Scatter(
        x=xs,
        y=t_values,
        mode="lines",
        name=f"Taylor polynomial (n={n})",
        line=dict(
            color=GREEN,
            width=2.8,
            dash="dash"
        ),
        hovertemplate=(
            "x = %{x:.3f}<br>"
            "T(x) = %{y:.6g}"
            "<extra></extra>"
        )
    ),
    row=1,
    col=1
)


# Expansion point
fig.add_trace(
    go.Scatter(
        x=[a],
        y=[f_at_a],
        mode="markers",
        name="Expansion point",
        marker=dict(
            color=YELLOW,
            size=10
        ),
        hovertemplate=(
            "a = %{x:.2f}<br>"
            "f(a) = %{y:.6g}"
            "<extra></extra>"
        )
    ),
    row=1,
    col=1
)


# ==========================================
# GRAPH 2: ABSOLUTE ERROR
# ==========================================

fig.add_trace(
    go.Scatter(
        x=xs,
        y=errors,
        mode="lines",
        name="Absolute error",
        line=dict(
            color=ORANGE,
            width=2.5
        ),
        hovertemplate=(
            "x = %{x:.3f}<br>"
            "Error = %{y:.6g}"
            "<extra></extra>"
        )
    ),
    row=2,
    col=1
)


# ==========================================
# EXPANSION POINT ON BOTH GRAPHS
# ==========================================

fig.add_vline(
    x=a,
    line_color=YELLOW,
    line_dash="dot",
    line_width=1.4,
    row=1,
    col=1
)

fig.add_vline(
    x=a,
    line_color=YELLOW,
    line_dash="dot",
    line_width=1.4,
    row=2,
    col=1
)


# ==========================================
# AUTOMATIC INITIAL VIEW
# ==========================================

window = (
    (xs >= a - 6)
    & (xs <= a + 6)
)

local_y = np.concatenate([
    f_values[window],
    t_values[window]
])

local_y = local_y[
    np.isfinite(local_y)
]

if local_y.size:

    ymin, ymax = np.percentile(
        local_y,
        [3, 97]
    )

    margin = max(
        (ymax - ymin) * 0.15,
        0.2
    )

    upper_range = [
        ymin - margin,
        ymax + margin
    ]

else:
    upper_range = [-2, 2]


# Automatic error-axis scaling
local_error = errors[window]

local_error = local_error[
    np.isfinite(local_error)
]

if local_error.size:
    error_max = float(
        np.percentile(local_error, 98)
    )
else:
    error_max = 0.0

lower_range = [
    0,
    max(error_max * 1.2, 1e-8)
]


# ==========================================
# PLOTLY DESIGN
# ==========================================

fig.update_layout(

    height=820,

    paper_bgcolor="#08090C",
    plot_bgcolor="#000000",

    font=dict(
        color=TEXT
    ),

    # Horizontal legend above the graphs
    legend=dict(
        orientation="h",
        x=0.5,
        xanchor="center",
        y=1.075,
        yanchor="bottom",
        bgcolor="rgba(15,18,25,0.9)"
    ),

    margin=dict(
        l=65,
        r=30,
        t=145,
        b=55
    ),

    hovermode="closest",

    dragmode="pan"
)


# Subplot titles
fig.update_annotations(
    font=dict(
        color=TEXT,
        size=14
    )
)


# Shared horizontal axes
fig.update_xaxes(
    range=[a - 7, a + 7],
    gridcolor="#303641",
    zerolinecolor="#7F8894",
    linecolor="#7F8894"
)


# Vertical axes
fig.update_yaxes(
    gridcolor="#303641",
    zerolinecolor="#7F8894",
    linecolor="#7F8894"
)

fig.update_yaxes(
    title_text="y",
    range=upper_range,
    row=1,
    col=1
)

fig.update_yaxes(
    title_text="|f(x) - T(x)|",
    range=lower_range,
    row=2,
    col=1
)

fig.update_xaxes(
    title_text="x",
    row=2,
    col=1
)


# ==========================================
# DISPLAY GRAPHS
# ==========================================

st.plotly_chart(
    fig,
    use_container_width=True,
    theme=None,
    config={
        "scrollZoom": True,
        "displaylogo": False,
        "doubleClick": "reset"
    }
)

st.caption(
    "Mouse wheel: zoom | "
    "Click and drag: pan | "
    "Double-click: reset. "
    "The two graphs share the same horizontal scale."
)


# ==========================================
# ERROR INTERPRETATION
# ==========================================

st.markdown("### Interpretation")

st.latex(
    r"E_n(x)=|f(x)-T_n(x;a)|"
)

st.write(
    "The approximation error is zero at the expansion "
    "point. Near this point, it is often small, "
    "but increasing the polynomial degree does not "
    "necessarily decrease the error everywhere."
)
