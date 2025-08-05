from flask import Flask, redirect, url_for, request, render_template

app=Flask(__name__)
#initializing images
images=['static/ai1.png','static/real1.png','static/ai2.png','static/real2.png','static/ai3.png','static/real3.png',
        'static/ai4.png','static/real4.png','static/ai5.png','static/real5.png']
#assigns answers per question
answers=[False,True,False,True,False,True,False,True,False,True]
roundList=[1,2,3,4,5,6,7,8,9,10]


@app.route('/game', methods=['POST',"GET"])
def game():
    print("game")
    if request.method == 'POST':
        print('PO')
        real = request.form.get('real')
        fake = request.form.get('fake')
        if real in request.form:
            print('test')
            return render_template('game.html',Ans = answers, message = 'Incorrect.')
        elif fake in request.form:
            print('FAKE PRESSED')
        
    return render_template('game.html',Ans = answers, message = ' ')


@app.route('/')
def index():
    return render_template('index.html')




if __name__=='__main__':
    app.run(debug=True,port=8000)