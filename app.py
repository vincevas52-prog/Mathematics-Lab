import streamlit as st

st.set_page_config(
    page_title="Math Lab",
    page_icon="📐",
    layout="wide"
)


# ==========================================
# CUSTOM STYLING
# ==========================================

st.markdown("""
<style>

/* Hero section */

.mathlab-hero {
    background: linear-gradient(
        120deg,
        #21172F 0%,
        #302044 55%,
        #17151F 100%
    );
    border: 1px solid #55406E;
    border-radius: 18px;
    padding: 38px 42px;
    margin-bottom: 30px;
}

.mathlab-brand {
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 3px;
    color: #BEA5E8;
    margin-bottom: 12px;
}

.mathlab-title {
    font-size: 56px;
    font-weight: 750;
    letter-spacing: -1.5px;
    color: #FFFFFF;
    margin-bottom: 12px;
}

.mathlab-motto {
    font-size: 23px;
    font-weight: 500;
    color: #DDC8FF;
    margin-bottom: 16px;
}

.mathlab-description {
    font-size: 16px;
    line-height: 1.7;
    color: #C8C0D3;
    max-width: 760px;
}

/* Module descriptions */

.module-description {
    color: #B5AABD;
    font-size: 15px;
    line-height: 1.7;
    margin-bottom: 14px;
}

/* Learning path */

.mathlab-learning-path {
    background: #211A2D;
    border-left: 3px solid #8965B6;
    border-radius: 8px;
    padding: 20px 24px;
    color: #E8E2EF;
    line-height: 2;
}

/* Mobile */

@media (max-width: 700px) {

    .mathlab-hero {
        padding: 26px 22px;
    }

    .mathlab-title {
        font-size: 39px;
    }

    .mathlab-motto {
        font-size: 18px;
    }

    .mathlab-description {
        font-size: 14px;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HOME PAGE
# ==========================================

def home():

    # ======================================
    # HERO SECTION
    # ======================================

    hero_html = (
        '<div class="mathlab-hero">'
        '<div class="mathlab-brand">'
        'INTERACTIVE MATHEMATICS'
        '</div>'
        '<div class="mathlab-title">'
        'Σ Math Lab'
        '</div>'
        '<div class="mathlab-motto">'
        'Visualize the idea. Understand the proof.'
        '</div>'
        '<div class="mathlab-description">'
        'Explore university-level mathematics through '
        'interactive visualizations, rigorous mathematical '
        'theory, and carefully explained proofs.'
        '</div>'
        '</div>'
    )

    st.markdown(hero_html, unsafe_allow_html=True)

    # ======================================
    # MODULES
    # ======================================

    st.header("Explore Mathematics")

    st.markdown(
        "Choose a topic to explore its concepts, "
        "visualizations, and mathematical foundations."
    )

    st.write("")

    left, right = st.columns(2, gap="large")

    # ======================================
    # DERIVATIVES
    # ======================================

    with left:

        with st.container(border=True):

            st.subheader("📚 Derivatives")

            st.markdown(
                '<div class="module-description">'
                'Build a rigorous understanding of derivatives, '
                'differentiability, and the rules of differentiation.'
                '</div>',
                unsafe_allow_html=True
            )

            st.page_link(
                "derivative.py",
                label="Understanding Derivatives",
                icon="📐"
            )

            st.page_link(
                "differentiability.py",
                label="Differentiability & Rules",
                icon="📖"
            )

            st.page_link(
                "a_deeper_look_at_differentiability.py",
                label="A Deeper Look at Differentiability",
                icon="🔬"
            )

    # ======================================
    # TAYLOR POLYNOMIALS
    # ======================================

    with right:

        with st.container(border=True):

            st.subheader("📈 Taylor Polynomials")

            st.markdown(
                '<div class="module-description">'
                'Understand polynomial approximations, '
                "Taylor's theorem, and the behavior "
                'of approximation errors.'
                '</div>',
                unsafe_allow_html=True
            )

            st.page_link(
                "Taylor.py",
                label="Interactive Visualization",
                icon="📈"
            )

            st.page_link(
                "taylor_theory.py",
                label="Theory & Proof",
                icon="📖"
            )

            st.page_link(
                "taylor_error.py",
                label="Error Analysis",
                icon="📊"
            )

    # ======================================
    # SECOND ROW
    # ======================================

    left2, right2 = st.columns(2, gap="large")

    # ======================================
    # MULTIVARIABLE DIFFERENTIATION
    # ======================================

    with left2:

        with st.container(border=True):

            st.subheader(
                "🧭 Multivariable Differentiation"
            )

            st.markdown(
                '<div class="module-description">'
                'Extend differentiation to several variables '
                'and explore gradients, directional derivatives, '
                'and the multivariable chain rule.'
                '</div>',
                unsafe_allow_html=True
            )

            st.page_link(
                "partial_derivatives.py",
                label="Partial Derivatives",
                icon="📐"
            )

            st.page_link(
                "multivariable_differentiability.py",
                label="Differentiability in Several Variables",
                icon="📖"
            )

            st.page_link(
                "directional_derivatives.py",
                label="Gradient & Directional Derivatives",
                icon="🧭"
            )

            st.page_link(
                "multivariable_chain_rule.py",
                label="The Multivariable Chain Rule",
                icon="🔗"
            )

    # ======================================
    # GRADIENT DESCENT
    # ======================================

    with right2:

        with st.container(border=True):

            st.subheader("📉 Gradient Descent")

            st.markdown(
                '<div class="module-description">'
                'Explore iterative optimization algorithms, '
                'convergence principles, and the mathematical '
                'theory behind gradient descent.'
                '</div>',
                unsafe_allow_html=True
            )

            st.page_link(
                "gradient.py",
                label="Interactive Visualization",
                icon="📉"
            )

            st.page_link(
                "gradient_theory.py",
                label="Theory & Proof",
                icon="📖"
            )

    # ======================================
    # SUGGESTED LEARNING PATHS
    # ======================================

    st.write("")

    st.divider()

    st.subheader("Suggested Learning Paths")

    learning_html = (
        '<div class="mathlab-learning-path">'
        '<strong>Foundations:</strong> '
        'Derivatives → Differentiability → Taylor Polynomials'
        '<br>'
        '<strong>Multivariable Analysis:</strong> '
        'Partial Derivatives → Differentiability → '
        'Directional Derivatives → Chain Rule'
        '<br>'
        '<strong>Optimization:</strong> '
        'Gradient & Directional Derivatives → Gradient Descent'
        '</div>'
    )

    st.markdown(learning_html, unsafe_allow_html=True)

    st.write("")

    st.caption(
        "Math Lab — Explore. Understand. Prove."
    )


# ==========================================
# PAGE NAVIGATION
# ==========================================

pages = {

    "": [

        st.Page(
            home,
            title="Home",
            icon="🏠",
            default=True
        )

    ],

    "Taylor Polynomials": [

        st.Page(
            "Taylor.py",
            title="Visualization",
            icon="📈"
        ),

        st.Page(
            "taylor_theory.py",
            title="Theory & Proof",
            icon="📖"
        ),

        st.Page(
            "taylor_error.py",
            title="Error Analysis",
            icon="📊"
        )

    ],

    "Gradient Descent": [

        st.Page(
            "gradient.py",
            title="Visualization",
            icon="📉"
        ),

        st.Page(
            "gradient_theory.py",
            title="Theory & Proof",
            icon="📖"
        )

    ],

    "Derivatives": [

        st.Page(
            "derivative.py",
            title="Understanding Derivatives",
            icon="📐"
        ),

        st.Page(
            "differentiability.py",
            title="Differentiability & Rules",
            icon="📖"
        ),

        st.Page(
            "a_deeper_look_at_differentiability.py",
            title="A Deeper Look at Differentiability",
            icon="🔬"
        )

    ],

    "Multivariable Differentiation": [

        st.Page(
            "partial_derivatives.py",
            title="Partial Derivatives",
            icon="📐"
        ),

        st.Page(
            "multivariable_differentiability.py",
            title="Differentiability in Several Variables",
            icon="📖"
        ),

        st.Page(
            "directional_derivatives.py",
            title="Gradient & Directional Derivatives",
            icon="🧭"
        ),

        st.Page(
            "multivariable_chain_rule.py",
            title="The Multivariable Chain Rule",
            icon="🔗"
        )

    ]

}


# ==========================================
# RUN NAVIGATION
# ==========================================

pg = st.navigation(
    pages,
    position="top"
)

pg.run()
