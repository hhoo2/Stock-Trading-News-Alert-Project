import json # importing json module
import smtplib  # For sending email
import requests # For getting data from API

# Set up email credentials
MY_EMAIL = "your_email@gmail.com" #Replace this variable with your email
MY_PASSWORD = "your_email_password" # Replace this variable with your password
RECIPIENT = "recipient_email@example.com" # Replace this variable with the recipient's email address

# Stock and company information
STOCK_NAME = "IBM" # Replace with your desired stock symbol
COMPANY_NAME = "IBM" # Replace with your desired company name
STOCK_API_key = "your_stock_api_key"  # Replace with your Alpha Vantage API key
NEWS_API_key = "your_news_api_key"  # Replace with your News API key

# API endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Construct the URL for stock data
url = f'{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_key}'
response = requests.get(url)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

# Get yesterday's and day before yesterday's closing stock prices
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Calculate the price difference and percentage change
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = round((difference / float(yesterday_closing_price)) * 100, 2)
up_down = "🔺" if difference > 0 else "🔻"

# Percentage change threshold to trigger email alerts
diff_percent_threshold = 1  # Replace with your desired threshold

# Check if the percentage change is greater than 1%
if diff_percent > diff_percent_threshold:
  # Fetch news articles related to the company
  news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_key
  }

  news_response = requests.get(NEWS_ENDPOINT, params=news_params)
  articles = news_response.json()["articles"]

  # Extract three articles, Adjust this variable to specify the number of news articles in email alerts
  three_articles = articles[:3]

  # Format the articles
  formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

  # Send emails for each article
  for article in formatted_articles:
    with smtplib.SMTP("smtp.gmail.com") as connection:
      connection.starttls()
      connection.login(MY_EMAIL, MY_PASSWORD)
      article_subject = f"Alert!! - {STOCK_NAME}: {up_down}{diff_percent}% "
      article_body = article
      msg = f"Subject: {article_subject}\n\n{article_body}"
      connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=RECIPIENT,
        msg=msg.encode('utf-8')
      )
