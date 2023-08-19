



import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests


# api keys and email details
# os.environ.get() is used for privacy
api_key_stockprice=os.environ.get('api_key_stockprice')
api_key_news=os.environ.get('api_key_news')
symbol = os.environ.get('symbol')
to_addrs=os.environ.get('to_addrs')
sender_email =os.environ.get('sender_email')
password_gmail= os.environ.get('password_gmail')


# function to send mail 
#the message is haing words in hindi so i have to encode it in utf-8 format as shown
def send_mail(message,sub):
    # Set up the SMTP server
    global to_addrs, sender_email, password_gmail
    smtp_server = "smtp.gmail.com"
    port = 587
    

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_addrs
    msg['Subject'] = sub

    # Add the Hindi text to the message
    body = MIMEText(message, 'plain', 'utf-8')
    msg.attach(body)

    # Start a secure connection with the server
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password_gmail)

    # Send the email
    server.sendmail(sender_email, msg['To'], msg.as_string())
    server.quit()




# taking stock data of perticular stock symbol is simply company name
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}.BSE&outputsize=full&apikey={api_key_stockprice}'
response = requests.get(url)
data=response.json()
latest_days=list(data['Time Series (Daily)'].keys())[:2]  # taking latest 2 days data

latest_days_data={ values: data["Time Series (Daily)"][values] for values in latest_days}# will get the latest 2 days data 
# print(latest_days_data)
previous_day_close=latest_days_data[latest_days[0]]['4. close']
prev_previous_day_close=latest_days_data[latest_days[1]]['4. close']

# calculation for percentage change in closing price of a stock from previous day and day before it
percentage_change=round((float(previous_day_close)-float(prev_previous_day_close))/float(prev_previous_day_close)*100,2)
# print(percentage_change)


# the logic is : if percentage change is more than 2% in previous section then send the news
# related to that company to the mail  

if percentage_change>=2:
    response=requests.get(f'https://newsapi.org/v2/everything?q=lic%20india&from={latest_days[1]}&to=&sortBy=po{latest_days[0]}pularity&apiKey={api_key_news}')
    data=response.json()
    msg='LICI: 🔺2%\n\n'
    for i in (data['articles']):
        msg+='headline:'+'\t'+i['title']+'\n\n'+'Brief:'+'\t'+i['description']+'\n'+'\n\n\n\n'
    send_mail(msg,'Stock info')
elif percentage_change<=-1:
    response=requests.get(f'https://newsapi.org/v2/everything?q=lic%20india&from={latest_days[1]}&to=&sortBy=po{latest_days[0]}pularity&apiKey={api_key_news}')
    data=response.json()
    msg='LICI: 🔻2%\n\n'
    for i in (data['articles']):
        msg+='headline:'+'\t'+i['title']+'\n\n'+'Brief:'+'\t'+i['description']+'\n'+'\n\n\n\n'    
    send_mail(msg,'Stock info')





