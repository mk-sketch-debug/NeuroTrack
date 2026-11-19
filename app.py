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

elif page == "Medication Tracking":
  st.subheader("Medication Tracking")
  st.write("Keep a structured record of medication history.")

elif page == "Wellness":
  st.subheader("Wellness Tracking")
  st.write("Explore sleep, stress, mood and daily functioning.")
