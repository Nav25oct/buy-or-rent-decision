import streamlit as st
import json
from analysis import decide_buy_or_rent  # Importing the function that calls Amazon Bedrock

# Streamlit App UI
st.title("🏡 Buy vs. Rent Decision Advisor")
st.markdown("---")
st.caption("🚀 **Powered by Amazon Bedrock & Claude 3.7 Reasoning Model**")

# User Inputs
zip_code = st.text_input("Enter Zip Code", "10001")
home_price = st.number_input("Home Price ($)", min_value=10000, value=500000, step=1000)
monthly_rent = st.number_input("Monthly Rent ($)", min_value=500, value=2500, step=50)
interest_rate = st.slider("Mortgage Interest Rate (%)", min_value=1.0, max_value=10.0, value=7.0, step=0.1)
loan_term = st.selectbox("Loan Term (Years)", [15, 30], index=1)
tax_rate = st.slider("Property Tax Rate (%)", min_value=0.5, max_value=3.0, value=1.2, step=0.1)

# Button to Get AI Analysis
if st.button("Analyze Decision"):
    # Create market data dictionary
    market_data = {
        "zip_code": zip_code,
        "property_price": home_price,
        "monthly_rent": monthly_rent,
        "interest_rate": interest_rate,
        "loan_term": loan_term,
        "tax_rate": tax_rate,
    }
    
    # Get AI response
    response = decide_buy_or_rent(market_data)

    # Display AI's reasoning process
    st.subheader("🤖 AI's Reasoning & Analysis")
    st.markdown(response)  # This will show Claude's step-by-step output

# Footer
st.markdown("---")
st.caption("🚀 **Powered by Amazon Bedrock & Claude 3.7 Reasoning Model**")