import streamlit as st
from PIL import Image
from components import sidebar
import os

st.set_page_config(
	page_title="Home",
	page_icon="🏥",
	layout="wide"
)

# Define the HTML and CSS for the first line
html_first_line = """
<!DOCTYPE html>
<html>
<head>
  <style>
    /* CSS Styles */
    .title {
      font-size: 72px;
      font-weight: 900; /* Extremely Bold */
      text-align: center;
      color: white;
    }
  </style>
</head>
<body>
  <!-- HTML Content for the first line -->
  <div class="title center">
    <span>Hello. I am</span>
  </div>
"""

# Define the HTML and CSS for the rest of the content
html_rest_of_content = """
<head>
  <style>
    /* CSS Styles */

    .subheading {
      font-size: 60px; /* Almost as big as the title */
      text-align: center;
    }

    .body-heading1 {
      font-size: 28px; /* Slightly bigger than body text */
      font-weight: bold; /* Emphatic */
      margin-top: 20px; /* Create space from the previous text */
    }

    .body-text1 {
      font-size: 18px; /* Easily readable size */
      margin-top: 10px; /* Space from the heading */
      line-height: 1.5; /* Line spacing for readability */
    }

    .body-heading2 {
      font-size: 28px; /* Slightly bigger than body text */
      font-weight: bold; /* Emphatic */
      margin-top: 20px; /* Create space from the previous text */
    }

    .body-text2 {
      font-size: 18px; /* Easily readable size */
      margin-top: 10px; /* Space from the heading */
      line-height: 1.5; /* Line spacing for readability */
    }

    .tagline {
      font-weight: bold; /* Stand out */
    }

    .tagline-subheading {
      font-size: 18px; /* Similar to body text */
      margin-top: 10px; /* Space from the previous text */
      line-height: 1.5; /* Line spacing for readability */
    }

    .ending-line {
      font-weight: bold; /* Stand out */
      text-align: center;
      margin-top: 20px; /* Space from the previous text */
    }

    /* Centered text */
    .center {
      text-align: center;
    }

    /* Clickable definitions */
    .definition {
      cursor: pointer;
      text-decoration: underline;
      color: #ff495C;
    }

    .definition:hover {
      color: orange;
    }

    /* Definition tooltip */
    .tooltip {
      position: absolute;
      background-color: #f9f9f9;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
      visibility: hidden;
      opacity: 0;
      transition: opacity 0.2s;
      z-index: 1;
    }

    .definition:hover + .tooltip {
      visibility: visible;
      opacity: 1;
    }
  </style>
</head>
  <!-- Rest of your HTML content (subheading, body text, etc.) -->
  <div class="subheading center">
    An AI Designed Specifically to Help You.
  </div><br>

  <div class="body-heading1">
    Unlocking the Potential of Your Daily Health Data.
  </div>

  <div class="body-text1">
    We're on a mission to redefine the doctor-patient relationship by harnessing the power of your daily health data. Your iPhone and Apple Watch generate a wealth of valuable health information every day, and we believe that data can be the key to a faster and more precise diagnoses.
  </div><br>

  <div class="body-heading2">
    Your Data, Your Control.
  </div>

  <div class="body-text2">
    Your health data is personal, and we respect your privacy. Rest assured that we never share your data with anyone, including your doctor, without your explicit consent. Your trust and control over your information are at the heart of what we do.
  </div><br>

  <div class="body-heading2">
    Join Us in Shaping the Future of Healthcare.
  </div>

  <div class="tagline-subheading">
    By partnering with us, you're taking a step into the future of healthcare. Together, we can empower doctors with the insights they need to provide you with the best possible care, all while putting you in the driver's seat of your own health journey.
  </div>

  <div class="body-heading1"><br>
    Experience the revolution in healthcare. Join Panacea today.
  </div><br>
</body>
</html>
"""

#Display the first line HTML
st.markdown(html_first_line, unsafe_allow_html=True)

#Display the panacea logo
st.image("static\Logo_Redone.png") 

#Display the rest of the content HTML
st.markdown(html_rest_of_content, unsafe_allow_html=True)

# Define the key features and their descriptions
features = {
    "Live Dashboards": "Real-time visual representations of patients' health data.",
    "Anomaly Detection": "Identifying unusual spikes or drops in health metrics.",
    "Prediction Module": "Utilizing historical data to predict potential health risks.",
    "Virtual Health Diary": "Allowing patients to input daily information about their well-being, diet, exercise, and more, providing context to their health metrics."
}

# Display clickable definitions
st.write("Key Features:")
for feature, description in features.items():
    st.write(f"- <span class='definition'>{feature}</span>: {description}</br><div class='tooltip'>{description}</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Define the file path
file_path = os.path.join('pages', '1_🧑_Medical_History.py')

# Create a button that redirects to the file_path
redirect_button = f"""
    <button onclick="window.location.href='{file_path}'" 
        style="color: white; background-color: #E01A4F; font-size: 20px; font-family: monospace; padding: 10px 20px; text-align: center; display: block; margin: 0 auto; cursor: pointer;">
        Try It
    </button>
"""

st.markdown(redirect_button, unsafe_allow_html=True)