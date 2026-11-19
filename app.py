import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time
from contourpy import contour_generator
from plotly.colors import sample_colorscale

st.set_page_config(page_title="Mathematics Lab", layout="wide")
st.title("Gradient Descent Playground")

# Mathematical functions
def f(x, y):
    return (x-1)**2 + 3*(y-x**2/4)**2

def gradient(x, y):
    return np.array([
        2*(x-1) - 3*x*(y-x**2/4),
        6*(y-x**2/4)
    ])

# Sidebar
st.sidebar.header("Parameters")

alpha = st.sidebar.slider("Step size", 0.01, 0.15, 0.08)
x0 = st.sidebar.slider("Initial x", -4.0, 4.0, -3.0)
y0 = st.sidebar.slider("Initial y", -4.0, 4.0, 3.0)
n = st.sidebar.slider("Iterations", 1, 50, 10)

# Gradient descent
p = np.array([x0, y0])
points = [p.copy()]

for k in range(n):
    p = p - alpha * gradient(p[0], p[1])

    if not np.all(np.isfinite(p)) or np.linalg.norm(p) > 100:
        st.warning("Possible divergence detected!")
        break

    points.append(p.copy())

points = np.array(points)
z_max = np.max(f(points[:, 0], points[:, 1]))

# Surface
x = np.linspace(-4, 4, 200)
y = np.linspace(-4, 4, 200)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = go.Figure()

fig.add_trace(go.Surface(
    x=X, y=Y, z=Z,
    colorscale="Viridis",
    opacity=0.4,
    showscale=False
))

# Iteration points
fig.add_trace(go.Scatter3d(
    x=points[:, 0],
    y=points[:, 1],
    z=f(points[:, 0], points[:, 1]),
    mode="lines+markers",
    line=dict(color="red", width=6),
    marker=dict(size=5, color="red"),
    name="Gradient descent"
))

fig.update_layout(
    template="plotly_dark",
    height=700,
    scene=dict(
        xaxis_title="x",
        yaxis_title="y",
        zaxis_title="f(x,y)",
        zaxis=dict(range=[0, max(1, 1.2*z_max)])
    )
)

st.latex(r"f(x,y)=(x-1)^2+3\left(y-\frac{x^2}{4}\right)^2")
st.plotly_chart(fig)

fig2 = go.Figure()

cg = contour_generator(x=x, y=y, z=Z, line_type="Separate")

levels = np.arange(0.2, 70, 1)

for c in levels:
    curves = cg.lines(c)

    for curve in curves:
        fig2.add_trace(go.Scatter(
            x=curve[:, 0],
            y=curve[:, 1],
            mode="lines",
            line=dict(
                color=sample_colorscale("Viridis", c/70)[0],
                width=1.5
            ),
            showlegend=False,
            hoverinfo="skip"
        ))

path_index = len(fig2.data)

fig2.add_trace(go.Scatter(
    x=points[:, 0],
    y=points[:, 1],
    mode="lines+markers",
    line=dict(color="red", width=3),
    marker=dict(size=6, color="red"),
    name="Gradient descent"
))

fig2.update_layout(
    template="plotly_dark",
    height=700,
    xaxis_title="x",
    yaxis_title="y"
)

fig2.update_xaxes(
    range=[-4, 4],
    dtick=1,
    constrain="domain"
)

fig2.update_yaxes(
    range=[-4, 4],
    dtick=1,
    scaleanchor="x",
    scaleratio=1,
    constrain="domain"
)

# Animation
frames = []

for k in range(len(points)):
    frame = go.Frame(
        data=[go.Scatter(
            x=points[:k+1, 0],
            y=points[:k+1, 1]
        )],
        traces=[path_index]
    )

    frames.append(frame)

fig2.frames = frames

fig2.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            bgcolor="#dc2626",
            showactive=False,
            borderwidth=1,
            font=dict(color="white", size=15),
            buttons=[
                dict(
                    label="Start",
                    method="animate",
                    args=[None, dict(
                        frame=dict(duration=200, redraw=False),
                        transition=dict(duration=0),
                        fromcurrent=True
                    )]
                )
            ]
        )
    ]
)

st.plotly_chart(fig2)
