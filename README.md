# Buy vs. Rent Decision Advisor

This project uses Amazon Bedrock Claude 3.7 to analyze real estate data and recommend whether to buy or rent.

## Features
- Uses Claude 3.7 via Amazon Bedrock
- Compares mortgage costs vs. rent costs
- Evaluates long-term financial implications

## High Level Architecture Diagram

![Architecture Diagram](https://github.com/Nav25oct/buy-or-rent-decision/blob/main/buyvsrent_highlevel_architecure.png)

## Installation

### Clone the Repository:
```bash
git clone https://github.com/nav25oct/buy-or-rent-decision.git
cd buy-or-rent-decision
```

### Install Dependencies:
```bash
pip install -r requirements.txt
playwright install
```

### Configure AWS Credentials:
Ensure your AWS credentials are set up correctly. If you are using a specific AWS profile, configure it using:

```bash
aws configure --profile bedrock
```

Or, export credentials for the session:

```bash
export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
export AWS_REGION=us-east-1
```

### update the cofig file (config.py):
Ensure your MODEL ID are set up correctly.
```bash
AWS_REGION = "us-east-1"
MODEL_ID = "arn:aws:bedrock:us-east-1:xxxx:inference-profile/us.anthropic.claude-3-7-sonnet-20250219-v1:0" # under Inference and assessement --> corss-region inference --> claude 3.7 " # under Inference and assessement --> corss-region inference --> claude 3.7 eg. 
```

## Understanding the Project Structure:
```
buy-vs-rent/
│── main.py             # Entry point for analysis
│── analyze.py          # Core logic to call Amazon Bedrock
│── requirements.txt    # Python dependencies
│── sample_data.json    # Sample real estate market data
│── README.md           # Instructions (this file)
```

## Running the Analysis through steamlit app:
```bash
streamlit run src/app.py
```

## Contributing:
Feel free to submit issues or pull requests for improvements.

## License:
This project is licensed under the MIT License.
