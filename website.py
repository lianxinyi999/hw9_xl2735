from flask import Flask
from flask import Flask, request, render_template

#create the flask web through random select the content 
app =Flask(__name__)

@app.route("/")
def display():

    import requests
    webcontent=requests.get("https://instructure-uploads.s3.amazonaws.com/account_13960000000000001/attachments/2742337/inspiration.txt?response-content-disposition=inline%3B%20filename%3D%22inspiration.txt%22%3B%20filename%2A%3DUTF-8%27%27inspiration.txt&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJFNFXH2V2O7RPCAA%2F20180418%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180418T195256Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=23483cf36bc703f6bbeb7fffa040692cf3249a0091e5b285f13f15c9e6fef579s://instructure-uploads.s3.amazonaws.com/account_13960000000000001/attachments/2742337/inspiration.txt?response-content-disposition=inline%3B%20filename%3D%22inspiration.txt%22%3B%20filename%2A%3DUTF-8%27%27inspiration.txt&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJFNFXH2V2O7RPCAA%2F20180420%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180420T024129Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c0998363bf21e2e56a88602b2aa5c24f7e76a6179ce45f796186f25c40fa33be")
    response=webcontent.content.decode('UTF-8')
    quote=response.split('\n')
    from random import randrange

    a=randrange(0,len(quote))
    quotes=quote[a]

    return render_template('quotes.html',quotes=quotes)
