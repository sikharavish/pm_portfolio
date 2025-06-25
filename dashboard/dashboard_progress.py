import streamlit as st

# Title and subtitle
st.title("💼 90-Day Product & Tech Portfolio Journey")
st.subheader("By Ravish Sikha | July 1 – September 30, 2025")

# Intro text
st.markdown("""
This dashboard tracks my weekly progress across a 90-day build focused on technical fluency, product sense, and real-world projects.  
Each week blends coding, product strategy, and reflection — targeting IC7+ PM roles at top-tier tech companies.
""")

# Define completed tasks
completed_tasks = [
    # Week 0
    "Set up Python, Node.js, Git, Docker, PostgreSQL locally",
    "Set up VS Code as IDE + GitHub repo",
    "Streamlit 'Hello World' dashboard created",
    "Started CS50P (Units 0–2)"
]

# Weekly tasks
weeks = {
    "Week 0 (Jun 24–30)": [
        "Set up Python, Node.js, Git, Docker, PostgreSQL locally",
        "Set up VS Code as IDE + GitHub repo",
        "Streamlit 'Hello World' dashboard created",
        "Started CS50P (Units 0–2)",
    ],
    "Week 1 (Jul 1–7)": [
        "Streamlit dashboard updated with Week 1 tracker",
        "CS50P Units 3–4 completed",
        "Drafted personal product thesis",
        "Planned MVP for first Flask app",
    ],
    "Week 2 (Jul 8–14)": [
        "Built Flask API for basic To-Do app",
        "React frontend scaffolded via Vite",
        "Connected frontend to Flask backend",
        "CS50P Unit 5 (Testing) completed",
    ],
    "Week 3 (Jul 15–21)": [
        "Integrated PostgreSQL into backend",
        "Dockerized full-stack app",
        "Deployment to AWS or Render started",
        "CS50P Unit 6 (File I/O) completed",
    ],
    "Week 4 (Jul 22–31)": [
        "Built and exposed ML model API",
        "Streamlit demo app for ML insights",
        "Posted Week 4 Substack reflection",
    ]
}

# Display each week's section with read-only checkboxes
for week, tasks in weeks.items():
    st.markdown(f"### {week}")
    for task in tasks:
        checked = task in completed_tasks
        st.checkbox(label=task, value=checked, disabled=True, key=f"{week}_{task}")

# Footer
st.markdown("---")
st.caption("🔁 Updated weekly | Follow progress on GitHub and Substack")
