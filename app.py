import streamlit as st
from datetime import date

# ---------------------------------------------------------
# 1. Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Job Application Tracker",
    page_icon="💼",
    layout="wide"
)

# ---------------------------------------------------------
# 2. Session State Initialization
# Store job applications in session state (in-memory)
# ---------------------------------------------------------
if "applications" not in st.session_state:
    st.session_state.applications = []

# ---------------------------------------------------------
# 3. Sidebar: Form to Add Application
# ---------------------------------------------------------
st.sidebar.header("➕ Add Job Application")

with st.sidebar.form("application_form", clear_on_submit=True):
    company = st.text_input("Company *")
    role = st.text_input("Role *")
    salary = st.text_input("Salary")
    stage = st.selectbox("Stage", ["Applied", "QA", "Interview", "Offer", "Rejected"])
    date_applied = st.date_input("Date Applied", value=date.today())
    job_link = st.text_input("Job Link")

    submitted = st.form_submit_button("Add Application")
    if submitted:
        if company.strip() and role.strip():
            # Append new application details to session state
            st.session_state.applications.append({
                "company": company.strip(),
                "role": role.strip(),
                "salary": salary.strip() if salary.strip() else "Not Specified",
                "stage": stage,
                "date_applied": str(date_applied),
                "job_link": job_link.strip(),
            })
            st.sidebar.success(f"Added application for {company}!")
        else:
            st.sidebar.error("Please provide both Company and Role.")

# ---------------------------------------------------------
# 4. Main Area: Display Applications List
# ---------------------------------------------------------
st.title("💼 Job Application Tracker")
st.write("Track and organize your job applications.")

if not st.session_state.applications:
    st.info("No applications added yet. Use the sidebar form to add one!")
else:
    st.subheader(f"Applications ({len(st.session_state.applications)})")
    
    # Iterate and display each application as a styled card in the list
    for idx, app in enumerate(st.session_state.applications, start=1):
        with st.container(border=True):
            col1, col2, col3 = st.columns([3, 2, 2])
            
            with col1:
                st.markdown(f"### {idx}. {app['company']}")
                st.markdown(f"**Role:** {app['role']}")
                if app["job_link"]:
                    st.markdown(f"🔗 [Job Link]({app['job_link']})")

            with col2:
                st.write(f"📅 **Date Applied:** {app['date_applied']}")
                st.write(f"💰 **Salary:** {app['salary']}")

            with col3:
                # Stage tag representation
                st.write(f"📌 **Stage:** `{app['stage']}`")
