
import ast
import operator

import numpy as np
import plotly.graph_objects as go
import streamlit as st
import sympy as sp

x = sp.Symbol("x", real=True)

# ==========================================
# FÜGGVÉNYEK ÉS MATEMATIKAI MŰVELETEK
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
# FELHASZNÁLÓI FÜGGVÉNY BEOLVASÁSA
# ==========================================

def read_function(text):

    text = text.strip().replace("^", "**")

    if not text or len(text) > 120:
        raise ValueError(
            "A képlet legfeljebb 120 karakteres lehet."
        )

    tree = ast.parse(text, mode="eval")

    if len(list(ast.walk(tree))) > 60:
        raise ValueError("Túl összetett képlet.")

    def convert(node):

        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            if abs(node.value) > 10000:
                raise ValueError("Túl nagy szám a képletben.")
            return sp.sympify(node.value)

        if isinstance(node, ast.Name) and node.id in CONSTANTS:
            return CONSTANTS[node.id]

        if isinstance(node, ast.UnaryOp) and isinstance(
            node.op, (ast.UAdd, ast.USub)
        ):
            val = convert(node.operand)
            return val if isinstance(node.op, ast.UAdd) else -val

        if isinstance(node, ast.BinOp):

            left = convert(node.left)
            right = convert(node.right)

            if isinstance(node.op, ast.Pow):
                if (
                    not right.is_number
                    or right.is_real is not True
                    or abs(float(right)) > 12
                ):
                    raise ValueError(
                        "A kitevő -12 és 12 között lehet."
                    )

                return left ** right

            op = OPERATORS.get(type(node.op))

            if op is not None:
                return op(left, right)

        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in FUNCTIONS
            and len(node.args) == 1
            and not node.keywords
        ):
            return FUNCTIONS[node.func.id](
                convert(node.args[0])
            )

        raise ValueError(
            "Nem támogatott képlet. "
            "Például: sin(x), x**2, exp(x)."
        )

    return convert(tree.body)


# ==========================================
# TAYLOR-POLINOM KISZÁMÍTÁSA
# ==========================================

def taylor_polynomial(f, center, degree):

    derivative = f
    polynomial = sp.Integer(0)

    for k in range(degree + 1):

        coefficient = sp.simplify(
            derivative.subs(x, center) / sp.factorial(k)
        )

        if (
            coefficient.is_finite is not True
            or coefficient.is_real is not True
        ):
            raise ValueError(
                "Ebben a pontban a kért Taylor-polinom nem létezik."
            )

        polynomial += coefficient * (x - center) ** k

        if k < degree:
            derivative = sp.diff(derivative, x)

    return polynomial


# ==========================================
# NUMERIKUS KIÉRTÉKELÉS
# ==========================================

def plot_values(expression, points):

    numeric = sp.lambdify(
        x, expression, modules="numpy"
    )

    with np.errstate(all="ignore"):

        values = np.asarray(
            numeric(points),
            dtype=np.complex128
        )

        values = np.broadcast_to(
            values, points.shape
        ).copy()

    result = values.real.copy()

    result[
        (np.abs(values.imag) > 1e-9)
        | (~np.isfinite(result))
    ] = np.nan

    return result


# ==========================================
# STREAMLIT FELÜLET
# ==========================================

st.title("📈 Taylor Polynomials")

st.write(
    "Explore how Taylor polynomials approximate "
    "functions around a chosen expansion point."
)

# Függvény kiválasztása

options = [
    "sin(x)",
    "cos(x)",
    "exp(x)",
    "log(1+x**2)",
    "1/(1+x**2)",
    "Custom function",
]

choice = st.selectbox(
    "Function",
    options
)

if choice == "Custom function":

    formula = st.text_input(
        "Enter f(x):",
        "sin(x)*exp(-x**2)"
    )

else:
    formula = choice

st.caption(
    "Notation: 2*x, x**2, sin(x), cos(x), "
    "exp(x), log(x), sqrt(x), pi"
)


# ==========================================
# CSÚSZKÁK
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
        "Taylor polynomial degree (n)",
        min_value=0,
        max_value=20,
        value=4
    )


# ==========================================
# MATEMATIKAI SZÁMÍTÁSOK
# ==========================================

try:

    f = read_function(formula)

    a_exact = sp.Rational(str(a))

    taylor = taylor_polynomial(
        f, a_exact, n
    )

    # Nagy számítási tartomány a távolításhoz
    xs = np.linspace(
        a - 80,
        a + 80,
        8001
    )

    ys = plot_values(f, xs)
    ts = plot_values(taylor, xs)

    y_at_a = float(
        sp.N(f.subs(x, a_exact))
    )

    if not np.isfinite(y_at_a):
        raise ValueError(
            "A függvény nem véges a kifejtési pontban."
        )

except (
    ValueError,
    SyntaxError,
    TypeError,
    OverflowError,
    ZeroDivisionError
) as error:

    st.error(
        f"Could not calculate approximation: {error}"
    )

    st.stop()


# Függvény megjelenítése LaTeX-ben

st.latex(
    r"f(x)=" + sp.latex(f)
)


# ==========================================
# PLOTLY INTERAKTÍV GRAFIKON
# ==========================================

RED = "#FF304F"
GREEN = "#39FF73"
YELLOW = "#F5C451"
TEXT = "#E8EDF5"

fig = go.Figure()


# Eredeti függvény - piros

fig.add_trace(
    go.Scatter(
        x=xs,
        y=ys,
        mode="lines",
        name="Original function",
        line=dict(
            color=RED,
            width=3
        ),
        hovertemplate=(
            "x = %{x:.3f}<br>"
            "f(x) = %{y:.5g}"
            "<extra></extra>"
        )
    )
)


# Taylor-közelítés - neonzöld

fig.add_trace(
    go.Scatter(
        x=xs,
        y=ts,
        mode="lines",
        name=f"Taylor polynomial (n={n})",
        line=dict(
            color=GREEN,
            width=3,
            dash="dash"
        ),
        hovertemplate=(
            "x = %{x:.3f}<br>"
            "T(x) = %{y:.5g}"
            "<extra></extra>"
        )
    )
)


# Kifejtési pont - sárga függőleges vonal

fig.add_vline(
    x=a,
    line_color=YELLOW,
    line_dash="dot",
    line_width=1.5
)


# Kifejtési pont a görbén

fig.add_trace(
    go.Scatter(
        x=[a],
        y=[y_at_a],
        mode="markers",
        name=f"Expansion point (a={a:g})",
        marker=dict(
            color=YELLOW,
            size=11,
            line=dict(
                color="#000000",
                width=1.5
            )
        ),
        hovertemplate=(
            "a = %{x:.2f}<br>"
            "f(a) = %{y:.5g}"
            "<extra></extra>"
        )
    )
)


# ==========================================
# KEZDŐ NÉZET AUTOMATIKUS BEÁLLÍTÁSA
# ==========================================

near_center = (
    (xs >= a - 3)
    & (xs <= a + 3)
)

local_values = np.concatenate([
    ys[near_center],
    ts[near_center]
])

local_values = local_values[
    np.isfinite(local_values)
]

if local_values.size:

    lower, upper = np.percentile(
        local_values,
        [5, 95]
    )

    center_y = (lower + upper) / 2

    half_height = max(
        (upper - lower) * 0.85,
        1.0
    )

else:

    center_y = 0.0
    half_height = 5.0


# ==========================================
# GRAFIKON KINÉZETE
# ==========================================

fig.update_layout(

    height=650,

    paper_bgcolor="#08090C",
    plot_bgcolor="#000000",

    font=dict(
        color=TEXT
    ),

    title=dict(
        text="Function and Taylor approximation",
        x=0.5
    ),

    xaxis=dict(
        title="x",
        range=[a - 7, a + 7],
        showgrid=True,
        gridcolor="#303641",
        zeroline=True,
        zerolinecolor="#7F8894",
        linecolor="#7F8894"
    ),

    yaxis=dict(
        title="y",
        range=[
            center_y - half_height,
            center_y + half_height
        ],
        showgrid=True,
        gridcolor="#303641",
        zeroline=True,
        zerolinecolor="#7F8894",
        linecolor="#7F8894"
    ),

    
    legend=dict(
        orientation="h",
        x=0.5,
        xanchor="center",
        y=1.03,
        yanchor="bottom",
        bgcolor="rgba(15,18,25,0.92)",
        bordercolor="#485261",
        borderwidth=1,
        font=dict(size=12)
    ),


    hovermode="closest",

    # Egérrel húzható grafikon
    dragmode="pan",

    margin=dict(
        l=50,
        r=25,
        t=125,
        b=50
    ),

    uirevision=f"{formula}|{a}"
)


# ==========================================
# GRAFIKON MEGJELENÍTÉSE
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
    "🖱️ Mouse wheel: zoom in/out | "
    "Left click + drag: move graph | "
    "Double click: reset view"
)


# ==========================================
# TAYLOR-POLINOM MEGJELENÍTÉSE
# ==========================================

with st.expander("Calculated Taylor polynomial"):

    st.latex(
        r"T_{" + str(n) + r"}(x;a)="
        + sp.latex(taylor)
    )


# ==========================================
# MATEMATIKAI MEGJEGYZÉS
# ==========================================

st.info(
    "Taylor polynomials provide local approximations. "
    "Higher polynomial degrees do not necessarily "
    "improve the approximation far from "
    "the expansion point."
)