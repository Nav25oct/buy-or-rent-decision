import boto3
import json

# Import configurations
from config import AWS_REGION, MODEL_ID

# Initialize Amazon Bedrock Runtime client
session = boto3.Session(profile_name="bedrock")  # Ensure AWS credentials are set
bedrock_runtime = session.client("bedrock-runtime", region_name=AWS_REGION)

# Function to call Claude 3.7 using Amazon Bedrock Messages API
def ask_claude_for_decision(market_data):
    # Define the system instruction separately
    system_prompt = "You are a highly analytical real estate and financial advisor. Provide structured, data-driven analysis."

    # Updated User Prompt with Tabular Comparison
    user_prompt = f"""
    Given the following financial and market data, analyze whether buying or renting is a better financial decision.

    **Key Considerations:**
    1️⃣ **Monthly mortgage costs** (loan payment, interest, property taxes, insurance, maintenance)
    2️⃣ **Monthly rent vs. affordability** (compare with user's maximum affordable rent)
    3️⃣ **Down payment impact** (how much capital is tied up in a home purchase)
    4️⃣ **Long-term financial implications**:
       - Home equity growth and appreciation potential 📈
       - Opportunity cost: If the down payment were invested in the S&P 500 (historical avg ~7-10% annual return), what could be the projected value? 📊
       - Flexibility: Buying ties capital to real estate; renting provides liquidity.

    **Market Data:**
    ```json
    {json.dumps(market_data, indent=2)}
    ```

    **Final Output Required:**
    - Provide a structured, detailed financial breakdown.
    - Compare renting vs. buying using real-world financial projections.
    - Structure your recommendation into three parts:
      ✅ **Short-term (1-3 years)**: Immediate cash flow, liquidity, flexibility.
      ✅ **Medium-term (4-10 years)**: Equity growth, rent increases, mortgage impact.
      ✅ **Long-term (10+ years)**: Wealth accumulation, property appreciation, opportunity cost vs. market investments.
    - Present the comparison in a structured **tabular format** as follows:

    | Factor                  | Buying Scenario 🏠 | Renting Scenario 🏢 |
    |-------------------------|-------------------|---------------------|
    | Property Price          | ${market_data['property_price']:,} | N/A |
    | Monthly Cost (Mortgage) | Based on loan term | ${market_data['monthly_rent']:,} |
    | Down Payment Required   | ${market_data['down_payment']:,} | None |
    | Home Equity Potential   | ✅ Builds Over Time | ❌ No Equity Growth |
    | Investment Opportunity  | Down Payment Locked | Can Invest Savings |
    | Maintenance Costs       | ✅ Homeowner Pays | ❌ Covered by Landlord |
    | Flexibility             | ❌ Limited Mobility | ✅ Can Relocate Easily |
    | Tax Benefits            | ✅ Mortgage Deductions | ❌ No Tax Benefits |

    - End with a clear **final recommendation** ("Buy" or "Rent") and explain why.
    """

    # Define messages for the Claude 3.7 API
    messages = [{"role": "user", "content": user_prompt}]

    # API request payload with "Thinking Blocks" enabled
    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "system": system_prompt,
        "messages": messages,
        "max_tokens": 4096,  # Ensure enough tokens for deep analysis
        "temperature": 1,  # Enables diverse reasoning
        "thinking": {  # Enables AI's internal financial reasoning
            "type": "enabled",
            "budget_tokens": 1024
        }
    }

    # Invoke Claude 3.7 model
    response = bedrock_runtime.invoke_model(
        modelId=MODEL_ID,
        contentType="application/json",
        accept="application/json",
        body=json.dumps(payload)
    )

    # Extract response body
    response_body = json.loads(response["body"].read().decode("utf-8"))

    # Extract AI reasoning and final response
    ai_reasoning = ""
    final_response = ""

    for content_block in response_body.get("content", []):
        if content_block["type"] == "thinking":
            ai_reasoning += f"\n🧠 AI Thinking: {content_block['thinking']}\n"
        elif content_block["type"] == "text":
            final_response += f"\n📌 Recommendation: {content_block['text']}\n"

    return ai_reasoning + final_response

# Function to decide between buying or renting
def decide_buy_or_rent(market_data):
    decision = ask_claude_for_decision(market_data)  # Directly pass user input
    return decision

# Run analysis for a sample ZIP code (for testing)
if __name__ == "__main__":
    sample_market_data = {
        "zip_code": "10001",
        "property_price": 500000,
        "monthly_rent": 2500,
        "interest_rate": 7.0,
        "loan_term": 30,
        "tax_rate": 1.2,
        "down_payment": 100000,
        "max_rent_affordability": 3000
    }
    
    result = decide_buy_or_rent(sample_market_data)
    print(result)
