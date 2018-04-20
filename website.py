from flask import Flask
from flask import Flask, request, render_template

#create the flask web through random select the content 
app =Flask(__name__)

@app.route("/")
def display():

    import requests
    webcontent=requests.get("https://instructure-uploads.s3.amazonaws.com/account_13960000000000001/attachments/2742337/inspiration.txt?response-content-disposition=inline%3B%20filename%3D%22inspiration.txt%22%3B%20filename%2A%3DUTF-8%27%27inspiration.txt&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJFNFXH2V2O7RPCAA%2F20180420%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180420T024129Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c0998363bf21e2e56a88602b2aa5c24f7e76a6179ce45f796186f25c40fa33bes://instructure-uploads.s3.amazonaws.com/account_13960000000000001/attachments/2742337/inspiration.txt?response-content-disposition=inline%3B%20filename%3D%22inspiration.txt%22%3B%20filename%2A%3DUTF-8%27%27inspiration.txt&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJFNFXH2V2O7RPCAA%2F20180420%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180420T024913Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2ae44dac99b6a004458c471db6932753beae6fc7db5f86fdf7ea19c6fa803ed7")
    response=webcontent.content.decode('UTF-8')
    quote=response.split('\n')
    from random import randrange

    a=randrange(0,len(quote))
    quotes=quote[a]

    return render_template('quotes.html',quotes=quotes)
