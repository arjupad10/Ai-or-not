from flask import Flask, redirect, url_for, request, render_template

app=Flask(__name__)
#initializing images
images=['static/ai1.png','static/real1.png','static/ai2.png','static/real2.png','static/ai3.png','static/real3.png',
        'static/ai4.png','static/real4.png','static/ai5.mp4','static/real5.png']
#assigns answers per question
answers=[False,True,False,True,False,True,False,True,False,True]
roundList=[1,2,3,4,5,6,7,8,9,10]

i=-1
score=0
@app.route('/game', methods=['POST',"GET"])
def game():
    global i
    global score
    print("game")
    if request.method == 'POST':
        print('PO')
        real = request.form.get('real')
        fake = request.form.get('fake')
        if 'real' in request.form:
            print('test')
            if answers[i]==True:
            #i+=1
                score+=1
                return render_template('game.html',score=score, Ans = answers[i],round=roundList[i],img=images[i], message = 'Correct' )
            else:
            #i+=1
                return render_template('game.html',score=score, Ans = answers[i],round=roundList[i],img=images[i], message ='Incorrect' )
        
        elif 'fake' in request.form:
            if answers[i]==False:
            #i+=1
                score+=1
                return render_template('game.html',score=score, Ans = answers[i],round=roundList[i],img=images[i], message = 'Correct' )
            else:
            #i+=1
                return render_template('game.html',score=score, Ans = answers[i],round=roundList[i],img=images[i], message ='Incorrect' )

# Click the next button logic
    if i>=9:
        i=-1
        return render_template('gameover.html',score=score)
    else:
        i+=1    
        return render_template('game.html',Ans = answers[i], score=score,round=roundList[i],img=images[i], message = ' ')


@app.route('/')
def index():
    global score
    score=0
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__=='__main__':
    app.run(debug=True,port=8000)