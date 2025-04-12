import streamlit as st
import re 

def check_passwd_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        st.write("Password must be 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        st.write("Password must have at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        st.write("Password must have at least one lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        st.write("Password must have at least one numeric value")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.write("Use any special case symbol")

    if score == 5:
        st.success("✅ Strong Password")
    elif score >= 3:
        st.warning("⚠️ Moderate - Consider using more secure features")
    else:
        st.error("❌ Weak Password")

  
password = st.text_input("Enter your password:", type="password")

if st.button("Submit"):
    check_passwd_strength(password)