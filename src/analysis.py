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
    system_prompt = "You are a highly analytical real estate advisor. Provide a structured, data-driven analysis."

    # User's query prompt
    user_prompt = f"""
    Given the following market data, analyze whether buying or renting is a better financial decision.
    Consider:
    - Monthly mortgage costs (loan, interest, taxes, insurance, maintenance)
    - Monthly rent
    - Long-term financial implications (equity, appreciation, flexibility)

    Market Data: {market_data}

    Provide a structured, detailed reasoning followed by a final recommendation.
    """

    # Define messages for the Claude 3.7 API
    messages = [{"role": "user", "content": user_prompt}]

    # API request payload with "Thinking Blocks" enabled
    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "system": system_prompt,
        "messages": messages,
        "max_tokens": 4096, # should be greater then budegt_tokens
        "temperature": 1, # temp can only be set 1 when thinkig is enabled 
        "thinking": {  # Enables AI's internal reasoning
            "type": "enabled",
            "budget_tokens": 1024 # default value (min value)
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

# Example function to retrieve real estate data (mocked for testing)
# def get_market_data(zip_code):
#     return {
#         "zip_code": zip_code,
#         "property_price": 500000,
#         "monthly_rent": 2500,
#         "interest_rate": 7.0,
#         "tax_rate": 1.2
#     }

# Function to decide between buying or renting
def decide_buy_or_rent(market_data):
    decision = ask_claude_for_decision(market_data)  # Directly pass user input
    return decision

# Run analysis for a sample ZIP code (for testing)
if __name__ == "__main__":
    zip_code = "10001"
    result = decide_buy_or_rent(zip_code)
    print(result)
