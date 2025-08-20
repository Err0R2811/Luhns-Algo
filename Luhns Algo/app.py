import streamlit as st
from main import luhn_check

st.set_page_config(page_title="Luhn Validator", page_icon="✅", layout="centered")
st.title("Luhn's Algorithm Validator")
st.caption("Checks card-like numbers using the Luhn algo. Spaces and dashes are allowed.")
st.image("amazon_visa.webp")
card_number = st.text_input("Enter card number", placeholder="7992 7398 713")

if st.button("Check"):
    cleaned = card_number.replace(" ", "").replace("-", "")
    if not cleaned:
        st.info("Please enter a number.")
    elif not cleaned.isdigit():
        st.warning("Please enter digits (you may include spaces or dashes).")
    else:
        is_valid = luhn_check(card_number)
        if is_valid:
            st.success("Valid number ✔ (passes Luhn check)")
            st.snow()
        else:
            st.error("Invalid number ✖ (fails Luhn check)")
            st.balloons()

with st.expander("How it works"):
    st.write(
        """
        1. Starting from the right, double every second digit.
        2. If doubling gives a two-digit number, subtract 9.
        3. Sum all digits. If total % 10 == 0, it's valid.
        """
    )
