import streamlit as st

#configure the application
st.set_page_config(
  page_title = "NeuroTrack",
  page_icon = "🧠",
  layout = "wide"
)

#application title
st.title("🧠 NeuroTrack")

st.subheader("Patient Health Tracking & Analytics")

st.write(
  """
  NeuroTrack is a patient - centred digital platform designed to organize symptom records, medication history and wellness information over time.
  """
)

st.info(
  "This application organizes patient - reported "
  "information. It does not provide medical diagnoses"
  "or medical recommendations."
)

st.success("Welcome to NeuroTrack!")
