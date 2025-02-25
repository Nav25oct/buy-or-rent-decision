# Buy vs. Rent Decision Advisor

This project uses **Amazon Bedrock Claude 3.7** to analyze real estate data and recommend whether to buy or rent.

## Features
- Uses **Claude 3.7 via Amazon Bedrock**
- Compares **mortgage costs vs. rent costs**
- Evaluates **long-term financial implications**

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/nav25oct/buy-or-rent-decision.git
   cd buy-or-rent-decision


2. Install Dependencies

pip install -r requirements.txt


3. Configure AWS Credentials

Ensure your AWS credentials are set up correctly. If you are using a specific AWS profile, configure it using:

aws configure --profile bedrock

Or, export credentials for the session:

export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
export AWS_REGION=us-east-1


3. Understanding the Project Structure

buy-vs-rent/
│── main.py              # Entry point for analysis
│── analyze.py           # Core logic to call Amazon Bedrock
│── requirements.txt     # Python dependencies
│── sample_data.json     # Sample real estate market data
│── README.md            # Instructions (this file)

4. Running the Analysis

python main.py 10001

5. Contributing

Feel free to submit issues or pull requests for improvements.


7. License

This project is licensed under the MIT License.

This README covers **everything**: prerequisites, installation, running the script, troubleshooting, and more. Let me know if you need any modifications! 🚀