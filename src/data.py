import random

def generate_sample_data(zip_code):
    """Generate sample real estate data for a given ZIP code."""
    
    # Define reasonable value ranges
    property_price = random.randint(400000, 800000)  # Property prices range
    monthly_rent = random.randint(2000, 5000)        # Monthly rent range
    interest_rate = round(random.uniform(4.0, 7.5), 2)  # Interest rate %
    tax_rate = round(random.uniform(1.0, 2.0), 2)       # Property tax %
    
    return {
        "zip_code": zip_code,
        "property_price": property_price,
        "monthly_rent": monthly_rent,
        "interest_rate": interest_rate,
        "tax_rate": tax_rate
    }

if __name__ == "__main__":
    zip_code = "10001"  # Test with a sample ZIP code
    sample_data = generate_sample_data(zip_code)
    print("Generated Sample Data:", sample_data)