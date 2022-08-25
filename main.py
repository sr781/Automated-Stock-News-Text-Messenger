import requests
from datetime import date
from twilio.rest import Client
import os
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]  # Using environment variables to store data locally for security
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
text_message = ""
STOCK = "TSLA"  # The stock we will need news for is tesla
API_KEY_STOCK = os.environ["API_KEY_STOCK"]  # API key for Alpha vantage
parameters_stock = {  # The parameters for Alpha vantage stock price tracker
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK,
}
parameters_news = {  # Parameters for the news api called Newscatcher
    "q": "Tesla",
    "lang": "en",
    "sort_by": "relevancy",
    "page": "1",
}
headers = {  # The api key needed to access the data for Newscatcher
    "x-api-key": os.environ["X-API-KEY"],
    }

stock_response = requests.get("https://www.alphavantage.co/query", params=parameters_stock)
stock_response.raise_for_status()
stock_data = stock_response.json()  # This will get the stock prices data for Tesla for the past few days and store it as a JSON

today = str(date.today())
today = today.split("-")  # Splits "25-08-2022" into ["25", "08", "2022"]

yesterdays_stock_close = float(stock_data["Time Series (Daily)"][f"{today[0]}-{today[1]}-{int(today[2])-1}"]["4. close"])  # Gets yesterdays close price for Tesla by parsing the JSON data
day_before_yesterdays_stock_close = float(stock_data["Time Series (Daily)"][f"{today[0]}-{today[1]}-{int(today[2])-2}"]["4. close"])  # Gets the day before yesterdays close price for Tesla in the exact same way
percent_change = ((yesterdays_stock_close - day_before_yesterdays_stock_close)/day_before_yesterdays_stock_close)*100  # Works out the percentage change because the text message will only be send if there is a +- 5% change in the stock price

if percent_change >= 5 or percent_change <= -5:  # If there is a more than 5% swing in the stock price from yesterday compared to the day before, this "if" statement is triggeredd
    text_message = f"{STOCK} change {percent_change}%"
    news_response = requests.get("https://api.newscatcherapi.com/v2/search", params=parameters_news, headers=headers)  # Get the relevant news data via the API
    news_response.raise_for_status()
    news_data = news_response.json()  # News data stored as a JSON
    for a in range(3):  # Only the first 3 news articles are needed
        title = news_data["articles"][a]["title"]  # The title of the news article is obtained
        news_link = news_data["articles"][a]["link"]  # The link is obtained if the user wants to view the article in more detail
        excerpt = news_data["articles"][a]["excerpt"] # An excerpt from the news article
        text_message = f"{text_message}\n\n------------------------------\nHeadline: {title}\n\nExcerpt: {excerpt}\n\nLink: {news_link}"  # The information is stored in this variable using f strings

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)  # This section is used to send the data via Twilio
    message = client.messages \
        .create(
        body=text_message,  # The message was created earlier and stored in the "text_message" variable
        from_='+13023376284',  # The host phone number from where it is sent
        to='+4407565211105'  # The recipient phone number from where it will be sent
    )
    print(message.status)




