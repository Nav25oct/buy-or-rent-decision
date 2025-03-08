import streamlit as st
import json
from analysis import decide_buy_or_rent  # Importing the function that calls Amazon Bedrock

# Streamlit App UI
st.title("🏡 Buy vs. Rent Decision Advisor")
st.markdown("---")
st.caption("🚀 **Powered by Amazon Bedrock & Claude 3.7 Reasoning Model**")

# User Inputs
zip_code = st.text_input("Enter Zip Code", "10001")
home_price = st.number_input("Home Price ($)", min_value=10000, value=1000000, step=10000)
monthly_rent = st.number_input("Monthly Rent ($)", min_value=500, value=5000, step=500)
interest_rate = st.slider("Mortgage Interest Rate (%)", min_value=1.0, max_value=10.0, value=7.0, step=0.1)
loan_term = st.selectbox("Loan Term (Years)", [15, 30], index=1)
tax_rate = st.slider("Property Tax Rate (%)", min_value=0.5, max_value=3.0, value=1.2, step=0.1)

# New Inputs: Down Payment & Rent Affordability
down_payment = st.number_input("Down Payment ($)", min_value=0, value=200000, step=5000)
max_rent_affordability = st.number_input("Max Affordable Rent ($)", min_value=500, value=6000, step=500)

if st.button("Analyze Decision"):
    # Create market data dictionary from user input
    market_data = {
        "zip_code": zip_code,
        "property_price": home_price,
        "monthly_rent": monthly_rent,
        "interest_rate": interest_rate,
        "loan_term": loan_term,
        "tax_rate": tax_rate,
        "down_payment": down_payment,
        "max_rent_affordability": max_rent_affordability,
    }
    
    # Call AI model with user input
    response = decide_buy_or_rent(market_data)  # ✅ Now passing full data

    # Display AI response
    st.subheader("🤖 AI's Reasoning & Analysis")
    st.markdown(response)

# Footer
st.markdown("---")
st.caption("🚀 **Powered by Amazon Bedrock & Claude 3.7 Reasoning Model**")
