# Automated-Stock-News-Text-Messenger
If a stock moves more than five percent in the last two days, a text message will be sent to the user containing the exact percentage movement of the stock as well as three news articles to explain it.  This program utilises API for three functions: stock price by Alpha Vantage, news by NewsCatcher and text messaging services by Twilio.  Furthermore the JSON data is parsed to obtain the relevant information.

![image](https://user-images.githubusercontent.com/96390217/186712879-3cb52300-8cd7-4df4-9bb6-291deb523c36.png)
![image](https://user-images.githubusercontent.com/96390217/186713019-37b91b6b-de23-43f3-bfbd-5a96a074b24f.png)


Figure 1: The information recieved by the phone via sms

The top 3 news articles on the company (in this case Tesla) is sent to the user as seen in figure 1.
#
![image](https://user-images.githubusercontent.com/96390217/186744015-62359054-1d2a-4007-917e-a6bda890b5c7.png)
![image](https://user-images.githubusercontent.com/96390217/186744101-cfd600ba-df75-4b6b-afcb-88b00e1407aa.png)

Figure 2: The top 3 news articles for Nvidia
