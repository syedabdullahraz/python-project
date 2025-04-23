import streamlit as st

# Conversion Functions
def length_converter(value, choice):
    if choice == "Kilometers to Miles":
        return f"{value} km = {value * 0.621371:.4f} miles"
    elif choice == "Miles to Kilometers":
        return f"{value} miles = {value * 1.60934:.4f} km"

def weight_converter(value, choice):
    if choice == "Kilograms to Pounds":
        return f"{value} kg = {value * 2.20462:.4f} pounds"
    elif choice == "Pounds to Kilograms":
        return f"{value} pounds = {value * 0.453592:.4f} kg"

def temperature_converter(value, choice):
    if choice == "Celsius to Fahrenheit":
        return f"{value}°C = {(value * 9/5) + 32:.2f}°F"
    elif choice == "Fahrenheit to Celsius":
        return f"{value}°F = {(value - 32) * 5/9:.2f}°C"

# App UI
def main():
    st.set_page_config(page_title="Unit Converter", layout="centered")
    st.markdown("<h1 style='text-align: center; color: teal;'>🧮 Smart Unit Converter</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Convert Length, Weight, and Temperature easily</h4>", unsafe_allow_html=True)
    st.markdown("---")

    option = st.selectbox("🔧 Choose Conversion Type", ["Length Converter", "Weight Converter", "Temperature Converter"])

    col1, col2 = st.columns(2)
    with col1:
        if option == "Length Converter":
            choice = st.radio("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
        elif option == "Weight Converter":
            choice = st.radio("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
        elif option == "Temperature Converter":
            choice = st.radio("🌡️ Select Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
    with col2:
        value = st.number_input("🔢 Enter Value", format="%.2f", step=0.1)

    st.markdown("")

    if st.button("🚀 Convert"):
        if option == "Length Converter":
            result = length_converter(value, choice)
        elif option == "Weight Converter":
            result = weight_converter(value, choice)
        elif option == "Temperature Converter":
            result = temperature_converter(value, choice)

        st.success(result)

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
