import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Future Career Trends Explorer",
    page_icon="🚀",
    layout="wide"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #180d25, #24113b, #32164d);
    color: white;
}

h1, h2, h3, h4, p, label, div {
    color: white;
}

.main-title {
    font-size: 45px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #e7d7f5;
    font-size: 18px;
    margin-bottom: 35px;
}

.card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 15px;
}

.metric-title {
    font-size: 15px;
    color: #d8c6e8;
}

.metric-value {
    font-size: 30px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# DATA
# ---------------------------------------------------------

career_data = {
    "Career": [
        "Data Scientist",
        "AI / ML Engineer",
        "Cybersecurity Analyst",
        "Software Developer",
        "Robotics Engineer",
        "Aerospace Engineer",
        "Renewable Energy Engineer",
        "Biomedical Engineer",
        "Cloud Engineer",
        "UX Designer",
        "Financial Analyst",
        "Environmental Scientist",
        "Game Developer",
        "Mechanical Engineer",
        "Electronics Engineer"
    ],

    "Field": [
        "Technology",
        "Technology",
        "Technology",
        "Technology",
        "Engineering",
        "Engineering",
        "Engineering",
        "Science",
        "Technology",
        "Design",
        "Finance",
        "Science",
        "Technology",
        "Engineering",
        "Engineering"
    ],

    "Growth": [
        88, 96, 91, 82, 86,
        75, 89, 78, 93, 72,
        68, 81, 79, 70, 84
    ],

    "Demand": [
        94, 98, 95, 91, 88,
        76, 87, 80, 96, 75,
        72, 79, 77, 74, 86
    ],

    "Salary": [
        1200000, 1500000, 1000000, 1100000, 900000,
        950000, 850000, 800000, 1300000, 750000,
        900000, 700000, 800000, 750000, 850000
    ],

    "Education": [
        "B.Tech / B.E.",
        "B.Tech / B.E.",
        "B.Tech / B.E.",
        "B.Tech / B.E.",
        "B.Tech / B.E.",
        "B.Tech / B.E.",
        "B.Tech / B.E.",
        "B.Tech / B.E.",
        "B.Tech / B.E.",
        "Degree / Diploma",
        "B.Com / BBA / Economics",
        "B.Sc / B.Tech",
        "B.Tech / Degree",
        "B.Tech / B.E.",
        "B.Tech / B.E."
    ],

    "Skills": [
        "Python, Statistics, Machine Learning",
        "Python, AI, Mathematics",
        "Networking, Security, Linux",
        "Programming, Problem Solving",
        "Robotics, CAD, Electronics",
        "Physics, CAD, Mathematics",
        "Energy Systems, Physics, Engineering",
        "Biology, Engineering, Research",
        "Cloud, Networking, Programming",
        "Design, Creativity, UX Research",
        "Finance, Excel, Statistics",
        "Biology, Research, Environment",
        "Programming, Creativity, Design",
        "CAD, Mechanics, Mathematics",
        "Electronics, Programming, Circuits"
    ]
}

df = pd.DataFrame(career_data)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🚀 Future Career Trends Explorer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Explore careers, skills, demand and future growth through interactive data.</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------------

st.sidebar.title("🔎 Explore Careers")

field_options = ["All"] + sorted(df["Field"].unique())

selected_field = st.sidebar.selectbox(
    "Choose a career field",
    field_options
)

growth_limit = st.sidebar.slider(
    "Minimum Future Growth",
    min_value=0,
    max_value=100,
    value=60
)

salary_limit = st.sidebar.slider(
    "Minimum Salary (₹ lakh)",
    min_value=5,
    max_value=15,
    value=7
)

search = st.sidebar.text_input(
    "Search for a career"
)


# ---------------------------------------------------------
# FILTER DATA
# ---------------------------------------------------------

filtered_df = df.copy()

if selected_field != "All":
    filtered_df = filtered_df[
        filtered_df["Field"] == selected_field
    ]

filtered_df = filtered_df[
    filtered_df["Growth"] >= growth_limit
]

filtered_df = filtered_df[
    filtered_df["Salary"] >= salary_limit * 100000
]

if search:
    filtered_df = filtered_df[
        filtered_df["Career"].str.contains(
            search,
            case=False,
            na=False
        )
    ]


# ---------------------------------------------------------
# TOP METRICS
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="card">
            <div class="metric-title">Careers Found</div>
            <div class="metric-value">{len(filtered_df)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    avg_growth = filtered_df["Growth"].mean() if len(filtered_df) else 0

    st.markdown(
        f"""
        <div class="card">
            <div class="metric-title">Average Growth</div>
            <div class="metric-value">{avg_growth:.1f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    avg_demand = filtered_df["Demand"].mean() if len(filtered_df) else 0

    st.markdown(
        f"""
        <div class="card">
            <div class="metric-title">Average Demand</div>
            <div class="metric-value">{avg_demand:.1f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    avg_salary = filtered_df["Salary"].mean() if len(filtered_df) else 0

    st.markdown(
        f"""
        <div class="card">
            <div class="metric-title">Average Salary</div>
            <div class="metric-value">₹{avg_salary/100000:.1f}L</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# CAREER TABLE
# ---------------------------------------------------------

st.subheader("📋 Career Explorer")

if len(filtered_df) == 0:

    st.warning(
        "No careers match your current filters. Try lowering the filters."
    )

else:

    display_df = filtered_df[
        ["Career", "Field", "Growth", "Demand", "Salary", "Education"]
    ].copy()

    display_df["Salary"] = (
        display_df["Salary"] / 100000
    ).round(1)

    display_df = display_df.rename(
        columns={
            "Growth": "Growth %",
            "Demand": "Demand %",
            "Salary": "Salary (₹ Lakh)"
        }
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )


# ---------------------------------------------------------
# CAREER SELECTION
# ---------------------------------------------------------

if len(filtered_df) > 0:

    st.subheader("🧭 Explore a Career")

    selected_career = st.selectbox(
        "Select a career to see more information",
        filtered_df["Career"].tolist()
    )

    career = df[
        df["Career"] == selected_career
    ].iloc[0]

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(
            f"""
            <div class="card">

            <h3>{career["Career"]}</h3>

            <p><b>Field:</b> {career["Field"]}</p>

            <p><b>Future Growth:</b> {career["Growth"]}%</p>

            <p><b>Demand:</b> {career["Demand"]}%</p>

            <p><b>Average Salary:</b>
            ₹{career["Salary"]/100000:.1f} Lakh</p>

            <p><b>Education:</b>
            {career["Education"]}</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            f"""
            <div class="card">

            <h3>🧠 Important Skills</h3>

            <p>{career["Skills"]}</p>

            <h3>📈 Career Indicators</h3>

            <p>Growth: {career["Growth"]}/100</p>

            <p>Demand: {career["Demand"]}/100</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# CHARTS
# ---------------------------------------------------------

if len(filtered_df) > 0:

    st.subheader("📊 Career Trends")

    chart_col1, chart_col2 = st.columns(2)

    # -------------------------
    # GROWTH CHART
    # -------------------------

    with chart_col1:

        fig, ax = plt.subplots(figsize=(8, 5))

        chart_data = filtered_df.sort_values(
            "Growth",
            ascending=True
        )

        ax.barh(
            chart_data["Career"],
            chart_data["Growth"]
        )

        ax.set_xlabel("Future Growth (%)")
        ax.set_title("Future Career Growth")

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)


    # -------------------------
    # DEMAND CHART
    # -------------------------

    with chart_col2:

        fig, ax = plt.subplots(figsize=(8, 5))

        chart_data = filtered_df.sort_values(
            "Demand",
            ascending=True
        )

        ax.barh(
            chart_data["Career"],
            chart_data["Demand"]
        )

        ax.set_xlabel("Demand (%)")
        ax.set_title("Industry Demand")

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)


# ---------------------------------------------------------
# CAREER COMPARISON
# ---------------------------------------------------------

st.subheader("⚖️ Compare Careers")

career_choices = st.multiselect(
    "Choose up to 3 careers",
    df["Career"].tolist(),
    max_selections=3
)

if len(career_choices) >= 2:

    comparison = df[
        df["Career"].isin(career_choices)
    ]

    fig, ax = plt.subplots(figsize=(9, 5))

    x = np.arange(len(comparison))
    width = 0.25

    ax.bar(
        x - width,
        comparison["Growth"],
        width,
        label="Growth"
    )

    ax.bar(
        x,
        comparison["Demand"],
        width,
        label="Demand"
    )

    salary_scaled = (
        comparison["Salary"] / 15000
    )

    ax.bar(
        x + width,
        salary_scaled,
        width,
        label="Salary indicator"
    )

    ax.set_xticks(x)
    ax.set_xticklabels(
        comparison["Career"],
        rotation=20,
        ha="right"
    )

    ax.set_ylabel("Score / Indicator")
    ax.set_title("Career Comparison")
    ax.legend()

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# ---------------------------------------------------------
# CAREER DATA
# ---------------------------------------------------------

with st.expander("📚 View Full Dataset"):

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <p style="text-align:center; color:#d8c6e8;">
    Future Career Trends Explorer • Built with Streamlit, Pandas,
    NumPy & Matplotlib
    </p>
    """,
    unsafe_allow_html=True
)
