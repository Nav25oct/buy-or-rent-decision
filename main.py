from src.data import generate_sample_data
from src.analysis import ask_claude_for_decision

def decide_buy_or_rent(zip_code):
    """Generates market data and runs buy vs. rent analysis"""
    market_data = generate_sample_data(zip_code)
    print(f"Market Data for {zip_code}: {market_data}")  # Debugging output
    decision = ask_claude_for_decision(market_data)
    return decision

if __name__ == "__main__":
    zip_code = "10001"  # Change ZIP code for different test cases
    result = decide_buy_or_rent(zip_code)
    print("\nClaude's Analysis:\n", result)