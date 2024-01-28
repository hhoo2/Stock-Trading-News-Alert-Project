# Stock Price Alert System

## Overview

This Python program is designed to monitor the daily stock prices of a specified company, analyze the percentage change, and send email alerts if the change exceeds a certain threshold. Additionally, it fetches 3 relevant news articles about the company using the News API and includes them in the email alerts.

Author:** Hay Oo

<b><a href="https://replit.com/@HayOo1/Stock-Trading-News-Alert-Project/" style="color:purple;">Click here to use this program in Replit</a></b>

![alt text](/program_result.png)

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `smtplib` (for email alerts)

## Configuration

### Email Settings

1. Set up a Gmail account to be used for sending email alerts.
2. Replace the `MY_EMAIL` and `MY_PASSWORD` variables with your Gmail email address and password.

### Recipient Information

1. Replace the `RECEIPIENT` variable with the email address where you want to receive the alerts.

### Company Stock Information

1. Replace the `STOCK_NAME` and `COMPANY_NAME` variables with the desired stock symbol and company name.

### API Keys

1. Obtain API keys for Alpha Vantage (stock prices) https://www.alphavantage.co/ and News API (related news) https://newsapi.org/.
2. Replace the `STOCK_API_key` and `NEWS_API_key` variables with your respective API keys.

### Percentage Trigger

1. Adjust the `diff_percent_threshold` variable to set the percentage change threshold that triggers email alerts. The program sends an alert only if the percentage change is greater than this threshold.

### Number of Articles

1. Adjust the `num_articles` variable to specify the number of news articles you want to receive in the email alerts.

If you have ideas for improvement, found a bug, or want to add a new feature, feel free to contact me. Thank!
