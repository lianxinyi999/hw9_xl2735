from flask import Flask
from flask import Flask, request, render_template

#create the flask web through random select the content 
app =Flask(__name__)

@app.route("/")
def display():

    with open("inspiration2.txt") as fp:
        quote=fp.read().split('\n')

    from random import randrange

    a=randrange(0,len(quote))
    quotes=quote[a]

    return render_template('quotes.html',quotes=quotes)
