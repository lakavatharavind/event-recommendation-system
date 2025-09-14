import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.title("📞 Contact Information")
st.markdown("Feel free to reach out to us using the details below:")

# Divider
st.markdown("---")

# Contact Info Section
st.markdown("""
### 📬 Get in Touch

- **Email**: ultronmegatron19@gmail.com  
- **Phone**: +91 8374466035 
- **Address**:  
  Event Recommender Inc.  
  CMR Engineering College Medchal-500401.
""")

# Optional: Footer or support notice
st.markdown("---")
st.info("We typically respond to emails within 24 hours.")
