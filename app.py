import streamlit as st
import pandas as pd
import plotly.express as px

#page configuration
st.set_page_config(
  page_title = "NeuroTrack",
  page_icon = "🧠",
  layout="wide"
)

#sidebar
st.sidebar.title("🧠 NeuroTrack")
st.sidebar.caption("Patient Health Tracking & Analytics")

page = st.sidebar.radio(
  "Navigation",
  ["Dashboard", "Symptom Tracking", "Medication Tracking", "Wellness"]
)

#dashboard header
st.title("NeuroTrack")
st.write("Your health information, organized over time.")

st.info(
  "NeuroTrack organizes patient-reported information "
  "to support conversations with healthcare professionals. "
  "It does not provide medical diagnoses or medication advice."
)

#dashboard metrics
st.subheader("Health Overview")
col1, col2, col3 = st.columns(3)

with col1:
  st.metric ("Symptom Entries", "0")

with col2:
  st.metric ("Medication Records", "0")

with col3:
  st.metric("Wellness Entries", "0")

st.divider()

#navigation content
if page == "Dashboard":
  st.subheader("Welcome to your dashboard")
  st.write("Your health tracking activity will appear here.")

elif page == "Symptom Tracking":
  st.subheader("Symptom Tracking")
  st.write("Record and review symptom experiences.")

  #initalize symptom records
  if "symptoms" not in st.session_state:
    st.session_state.symptoms = []
  
  #symptom entry form
  with st.form("symptom_form"):
  
    symptom_type = st.selectbox(
      "Symptom Type", ["Headache", "Facial Pain", "Numbness", "Tingling", "Dizziness", "Other"]
    )
    
    severity = st.slider(
      "Symptom Severity",
      min_value = 0,
      max_value = 10,
      value = 5
    )
    
    duration = st.number_input(
      "Duration (minutes)",
      min_value = 1,
      value = 30
    )
    
    symptom_date = st.date_input("Date")
    
    symptom_time = st.time_input("Time")
    
    triggers = st.text_area(
      "Possible Triggers or Notes"
    )
    submitted = st.form_submit_button("Save Symptom Entry")
    
    if submitted:
      symptom_record = {
        "Type": symptom_type,
        "Severity": severity,
        "Duration": duration,
        "Date": str(symptom_date),
        "Time": str(symptom_time),
        "Notes": triggers
      }
    
      st.session_state.symptoms.append(symptom_record)
      st.success("Symptom entry saved!")
  
  #display saved records
  st.subheader ("Symptom History")
  
  if st.session_state.symptoms:
    symptom_df = pd.DataFrame(st.session_state.symptoms)
    
    st.dataframe(symptom_df, use_container_width=True)
  else:
    st.info("No symptom entries recorded yet.")


elif page == "Medication Tracking":
  st.subheader("Medication Tracking")
  st.write("Keep a structured record of medication history.")

elif page == "Wellness":
  st.subheader("Wellness Tracking")
  st.write("Explore sleep, stress, mood and daily functioning.")
