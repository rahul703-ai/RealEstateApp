import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above")

# Inject custom CSS for dark theme styling
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #e0e0e0;
    }
    .main {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
    }
    .header {
        font-size: 50px;
        font-weight: bold;
        color: #bb86fc;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 24px;
        color: #a0a0a0;
        text-align: center;
        margin-bottom: 20px;
    }
    .highlight {
        background-color: #03dac6;
        color: #121212;
        font-weight: bold;
        padding: 10px 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        display: inline-block;
    }
    .section-title {
        font-size: 30px;
        font-weight: bold;
        color: #ff0266;
        margin-top: 40px;
        margin-bottom: 20px;
        border-bottom: 3px solid #ff0266;
        padding-bottom: 10px;
    }
    .property-card {
        background-color: #2a2a2a;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
        color: #e0e0e0;
    }
    .footer {
        font-size: 14px;
        color: #888;
        text-align: center;
        margin-top: 50px;
        padding: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main container for the content
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Header section
st.markdown("<div class='header'>Welcome to Our Real Estate Website</div>", unsafe_allow_html=True)

# Subheader section
st.markdown("<div class='subheader'>Find Your Dream Home Today!</div>", unsafe_allow_html=True)

# Highlight section
st.markdown("<div class='highlight'>Explore the properties at one place </div>", unsafe_allow_html=True)

# Adding an image (Replace with your image URL)
st.image("datasets/House.png", use_column_width=True)

# Featured properties section
st.markdown("<div class='section-title'>Featured Properties</div>", unsafe_allow_html=True)

# Example of property cards (You can add more details and style them)
st.markdown("<div class='property-card'>feature 1: Know price as your choice </div>", unsafe_allow_html=True)
st.markdown("<div class='property-card'>feature 2: Analyze the gurgaon properties </div>", unsafe_allow_html=True)
st.markdown("<div class='property-card'>feature 3: Top 5 recommendation as your preferred society </div>"
              , unsafe_allow_html=True)

# Close main container
st.markdown("</div>", unsafe_allow_html=True)

# Footer section
st.markdown("<div class='footer'>© 2024 Real Estate Co. All rights reserved.</div>", unsafe_allow_html=True)

