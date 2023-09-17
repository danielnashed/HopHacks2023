import streamlit as st
# from PIL import Image
from components import sidebar
import os

st.set_page_config(
	page_title="Home",
	page_icon="🏥",
	layout="wide"
)

# ⚕ 
sidebar.display()
# Header Section
st.title("Welcome to Panacea, Your Personal Medical Assistant")
#st.write("Transforming Healthcare with Advanced AI")
filePath = os.path.join("static","Logo.png")
st.image(filePath, width= 1000)

# Banner Section
#st.image("medical_professional_image.jpg", use_container_width=True)
st.header("Revolutionizing Healthcare with AI")

# Introduction Section

st.markdown("<h3 style='text-align: left;'>Unlocking the Potential of Your Daily Health Data.</h3>", unsafe_allow_html=True)

st.markdown("""
At Panacea, we're on a mission to redefine the doctor-patient relationship by harnessing the power of your daily health data. Your iPhone and 
Apple Watch generate a wealth of valuable health information every day, and we believe that data can be the key to faster and more precise diagnoses.
""")

st.markdown("<h3 style='text-align: left;'>Your Data, Your Control.</h3>", unsafe_allow_html=True)            

st.markdown("""
Your health data is personal, and we respect your privacy. Rest assured that we never share your data with anyone, including your doctor, without your explicit consent. Your trust and control over your information are at the heart of what we do.
""")

st.markdown("<h3 style='text-align: left;'>Join Us in Shaping the Future of Healthcare.</h3>", unsafe_allow_html=True)   

st.markdown("""			
By partnering with us, you're taking a step into the future of healthcare. Together, we can empower doctors with the insights they need to 
provide you with the best possible care, all while putting you in the driver's seat of your own health journey.
""")
            
st.markdown("""
Experience the revolution in healthcare. Join Panacea today."
""")

# Key Features Section
st.header("Key Features")

# Define the key features and their descriptions
features = {
    "Live Dashboards": "Real-time visual representations of patients' health data.",
    "Anomaly Detection": "Identifying unusual spikes or drops in health metrics.",
    "Prediction Module": "Utilizing historical data to predict potential health risks.",
    "Virtual Health Diary": "Allowing patients to input daily information about their well-being, diet, exercise, and more, providing context to their health metrics."
}

# Display the features with descriptions
for feature, description in features.items():
    st.subheader(feature)
    st.write(description)
