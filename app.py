from flask import Flask, redirect, render_template, request, url_for
import time
import random

app = Flask(__name__)

ailist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x_spot = []
o_spot = []

@app.route('/', methods=['POST', 'GET'])



def first():
    if request.method == 'POST':
        global x_spot
        global choice
        global ailist
        choice = int(request.form['spot'])
        ailist.remove(choice)
        x_spot.append(choice)
        return redirect('/second', code=302)
    return render_template('index.html')

@app.route('/second')



def second():
    global o_spot
    global choice2
    choice2 = random.choice(ailist)
    ailist.remove(choice2)
    o_spot.append(choice2)
    return redirect('/third', code=302)



@app.route('/third', methods=['POST', 'GET'])

def third():
    if request.method == 'POST':
        global x_spot
        global choice3
        global ailist
        choice3 = int(request.form['spot'])
        ailist.remove(choice3)
        x_spot.append(choice3)
        return redirect('/fourth', code=302)
    return render_template('index.html', choice=choice, choice2=choice2)

@app.route('/fourth')



def fourth():
    global o_spot
    global choice4
    choice4 = random.choice(ailist)
    ailist.remove(choice4)
    o_spot.append(choice4)
    return redirect('/fifth', code=302)

@app.route('/fifth', methods=['POST', 'GET'])

def fifth():
    if request.method == 'POST':
        global choice5
        global ailist
        global x_spot
        choice5 = int(request.form['spot'])
        x_spot.append(choice5)
        ailist.remove(choice5)
        return redirect('/sixth', code=302)
    return render_template('index.html', choice=choice, choice2=choice2, choice3=choice3, choice4=choice4)

@app.route('/sixth')

def sixth():
    global x_spot
    global winning
    global win
    if 1 in x_spot and 2 in x_spot and 3 in x_spot:
        win = 'You Win!'
        winning = 6
        return redirect('/winning', code=302)
    if 4 in x_spot and 5 in x_spot and 6 in x_spot:
        win = 'You Win!'
        winning = 6
        return redirect('/winning', code=302)
    if 7 in x_spot and 8 in x_spot and 9 in x_spot:
        win = 'You Win!'
        winning = 6
        return redirect('/winning', code=302)
    if 1 in x_spot and 5 in x_spot and 9 in x_spot:
        win = 'You Win!'
        winning = 6
        return redirect('/winning', code=302)
    if 3 in x_spot and 5 in x_spot and 7 in x_spot:
        win = 'You Win!'
        winning = 6
        return redirect('/winning', code=302)
    if 1 in x_spot and 4 in x_spot and 7 in x_spot:
        win = 'You Win!'
        winning = 6
        return redirect('/winning', code=302)
    if 2 in x_spot and 5 in x_spot and 8 in x_spot:
        win = 'You Win!'
        winning = 6
        return redirect('/winning', code=302)
    if 9 in x_spot and 6 in x_spot and 3 in x_spot:
        win = 'You Win!'
        winning = 6
        return redirect('/winning', code=302)
    
    global o_spot
    global choice6
    choice6 = random.choice(ailist)
    ailist.remove(choice6)
    o_spot.append(choice6)
    return redirect('/seventh', code=302)

@app.route('/seventh', methods=['POST', 'GET'])

def seventh():
    global winning
    global win
    if 1 in x_spot and 2 in x_spot and 3 in x_spot:
        win = 'You Win!'
        winning = 7
        return redirect('/winning', code=302)
    if 4 in x_spot and 5 in x_spot and 6 in x_spot:
        win = 'You Win!'
        winning = 7
        return redirect('/winning', code=302)
    if 7 in x_spot and 8 in x_spot and 9 in x_spot:
        win = 'You Win!'
        winning = 7
        return redirect('/winning', code=302)
    if 1 in x_spot and 5 in x_spot and 9 in x_spot:
        win = 'You Win!'
        winning = 7
        return redirect('/winning', code=302)
    if 3 in x_spot and 5 in x_spot and 7 in x_spot:
        win = 'You Win!'
        winning = 7
        return redirect('/winning', code=302)
    if 1 in x_spot and 4 in x_spot and 7 in x_spot:
        win = 'You Win!'
        winning = 7
        return redirect('/winning', code=302)
    if 2 in x_spot and 5 in x_spot and 8 in x_spot:
        win = 'You Win!'
        winning = 7
        return redirect('/winning', code=302)
    if 9 in x_spot and 6 in x_spot and 3 in x_spot:
        win = 'You Win!'
        winning = 7
        return redirect('/winning', code=302)
    
    if 1 in o_spot and 2 in o_spot and 3 in o_spot:
        win = 'You Lose!'
        winning = 7
        return redirect('/winning', code=302)
    if 4 in o_spot and 5 in o_spot and 6 in o_spot:
        win = 'You Lose!'
        winning = 7
        return redirect('/winning', code=302)
    if 7 in o_spot and 8 in o_spot and 9 in o_spot:
        win = 'You Lose!'
        winning = 7
        return redirect('/winning', code=302)
    if 1 in o_spot and 5 in o_spot and 9 in o_spot:
        win = 'You Lose!'
        winning = 7
        return redirect('/winning', code=302)
    if 3 in o_spot and 5 in o_spot and 7 in o_spot:
        win = 'You Lose!'
        winning = 7
        return redirect('/winning', code=302)
    if 1 in o_spot and 4 in o_spot and 7 in o_spot:
        win = 'You Lose!'
        winning = 7
        return redirect('/winning', code=302)
    if 2 in o_spot and 5 in o_spot and 8 in o_spot:
        win = 'You Lose!'
        winning = 7
        return redirect('/winning', code=302)
    if 9 in o_spot and 6 in o_spot and 3 in o_spot:
        win = 'You Lose!'
        winning = 7
        return redirect('/winning', code=302)
    if request.method == 'POST':
        global choice7
        global ailist
        choice7 = int(request.form['spot'])
        x_spot.append(choice7)
        ailist.remove(choice7)
        return redirect('/eighth', code=302)
    
    return render_template('index.html', choice=choice, choice2=choice2, choice3=choice3, choice4=choice4, choice5=choice5, choice6=choice6)

@app.route('/eighth')
def eighth():
    global x_spot
    global o_spot
    global winning
    global win
    if 1 in x_spot and 2 in x_spot and 3 in x_spot:
        win = 'You Win!'
        winning = 8
        return redirect('/winning', code=302)
    if 4 in x_spot and 5 in x_spot and 6 in x_spot:
        win = 'You Win!'
        winning = 8
        return redirect('/winning', code=302)
    if 7 in x_spot and 8 in x_spot and 9 in x_spot:
        win = 'You Win!'
        winning = 8
        return redirect('/winning', code=302)
    if 1 in x_spot and 5 in x_spot and 9 in x_spot:
        win = 'You Win!'
        winning = 8
        return redirect('/winning', code=302)
    if 3 in x_spot and 5 in x_spot and 7 in x_spot:
        win = 'You Win!'
        winning = 8
        return redirect('/winning', code=302)
    if 1 in x_spot and 4 in x_spot and 7 in x_spot:
        win = 'You Win!'
        winning = 8
        return redirect('/winning', code=302)
    if 2 in x_spot and 5 in x_spot and 8 in x_spot:
        win = 'You Win!'
        winning = 8
        return redirect('/winning', code=302)
    if 9 in x_spot and 6 in x_spot and 3 in x_spot:
        win = 'You Win!'
        winning = 8
        return redirect('/winning', code=302)
    
    if 1 in o_spot and 2 in o_spot and 3 in o_spot:
        win = 'You Lose'
        winning = 8
        return redirect('/winning', code=302)
    if 4 in o_spot and 5 in o_spot and 6 in o_spot:
        win = 'You Lose'
        winning = 8
        return redirect('/winning', code=302)
    if 7 in o_spot and 8 in o_spot and 9 in o_spot:
        win = 'You Lose'
        winning = 8
        return redirect('/winning', code=302)
    if 1 in o_spot and 5 in o_spot and 9 in o_spot:
        win = 'You Lose'
        winning = 8
        return redirect('/winning', code=302)
    if 3 in o_spot and 5 in o_spot and 7 in o_spot:
        win = 'You Lose'
        winning = 8
        return redirect('/winning', code=302)
    if 1 in o_spot and 4 in o_spot and 7 in o_spot:
        win = 'You Lose'
        winning = 8
        return redirect('/winning', code=302)
    if 2 in o_spot and 5 in o_spot and 8 in o_spot:
        win = 'You Lose'
        winning = 8
        return redirect('/winning', code=302)
    if 9 in o_spot and 6 in o_spot and 3 in o_spot:
        win = 'You Lose'
        winning = 8
        return redirect('/winning', code=302)
    global choice8
    choice8 = random.choice(ailist)
    ailist.remove(choice8)
    o_spot.append(choice8)
    return redirect('/nineth', code=302)

@app.route('/nineth', methods=['POST', 'GET'])

def nineth():
    global winning
    global win
    if 1 in x_spot and 2 in x_spot and 3 in x_spot:
        win = 'You Win!'
        winning = 9
        return redirect('/winning', code=302)
    if 4 in x_spot and 5 in x_spot and 6 in x_spot:
        win = 'You Win!'
        winning = 9
        return redirect('/winning', code=302)
    if 7 in x_spot and 8 in x_spot and 9 in x_spot:
        win = 'You Win!'
        winning = 9
        return redirect('/winning', code=302)
    if 1 in x_spot and 5 in x_spot and 9 in x_spot:
        win = 'You Win!'
        winning = 9
        return redirect('/winning', code=302)
    if 3 in x_spot and 5 in x_spot and 7 in x_spot:
        win = 'You Win!'
        winning = 9
        return redirect('/winning', code=302)
    if 1 in x_spot and 4 in x_spot and 7 in x_spot:
        win = 'You Win!'
        winning = 9
        return redirect('/winning', code=302)
    if 2 in x_spot and 5 in x_spot and 8 in x_spot:
        win = 'You Win!'
        winning = 9
        return redirect('/winning', code=302)
    if 9 in x_spot and 6 in x_spot and 3 in x_spot:
        win = 'You Win!'
        winning = 9
        return redirect('/winning', code=302)
    
    if 1 in o_spot and 2 in o_spot and 3 in o_spot:
        win = 'You Lose!'
        winning = 9
        return redirect('/winning', code=302)
    if 4 in o_spot and 5 in o_spot and 6 in o_spot:
        win = 'You Lose!'
        winning = 9
        return redirect('/winning', code=302)
    if 7 in o_spot and 8 in o_spot and 9 in o_spot:
        win = 'You Lose!'
        winning = 9
        return redirect('/winning', code=302)
    if 1 in o_spot and 5 in o_spot and 9 in o_spot:
        win = 'You Lose!'
        winning = 9
        return redirect('/winning', code=302)
    if 3 in o_spot and 5 in o_spot and 7 in o_spot:
        win = 'You Lose!'
        winning = 9
        return redirect('/winning', code=302)
    if 1 in o_spot and 4 in o_spot and 7 in o_spot:
        winning = 9
        win = 'You Lose!'
        return redirect('/winning', code=302)
    if 2 in o_spot and 5 in o_spot and 8 in o_spot:
        win = 'You Lose!'
        winning = 9
        return redirect('/winning', code=302)
    if 9 in o_spot and 6 in o_spot and 3 in o_spot:
        win = 'You Lose!'
        winning = 9
        return redirect('/winning', code=302)
    if request.method == 'POST':
        global choice9
        global ailist
        choice9 = int(request.form['spot'])
        x_spot.append(choice9)
        ailist.remove(choice9)
        return redirect('/tie', code=302)
    
    return render_template('index.html', choice=choice, choice2=choice2, choice3=choice3, choice4=choice4, choice5=choice5, choice6=choice6, choice7=choice7, choice8=choice8)
    
@app.route('/tie')
def tie():
    global winning
    global win
    if 1 in x_spot and 2 in x_spot and 3 in x_spot:
        win = 'You Win!'
        winning = 10
        return redirect('/winning', code=302)
    if 4 in x_spot and 5 in x_spot and 6 in x_spot:
        win = 'You Win!'
        winning = 10
        return redirect('/winning', code=302)
    if 7 in x_spot and 8 in x_spot and 9 in x_spot:
        win = 'You Win!'
        winning = 10
        return redirect('/winning', code=302)
    if 1 in x_spot and 5 in x_spot and 9 in x_spot:
        win = 'You Win!'
        winning = 10
        return redirect('/winning', code=302)
    if 3 in x_spot and 5 in x_spot and 7 in x_spot:
        win = 'You Win!'
        winning = 10
        return redirect('/winning', code=302)
    if 1 in x_spot and 4 in x_spot and 7 in x_spot:
        win = 'You Win!'
        winning = 10
        return redirect('/winning', code=302)
    if 2 in x_spot and 5 in x_spot and 8 in x_spot:
        win = 'You Win!'
        winning = 10
        return redirect('/winning', code=302)
    if 9 in x_spot and 6 in x_spot and 3 in x_spot:
        win = 'You Win!'
        winning = 10
        return redirect('/winning', code=302)
    
    if 1 in o_spot and 2 in o_spot and 3 in o_spot:
        win = 'You Lose!'
        winning = 10
        return redirect('/winning', code=302)
    if 4 in o_spot and 5 in o_spot and 6 in o_spot:
        win = 'You Lose!'
        winning = 10
        return redirect('/winning', code=302)
    if 7 in o_spot and 8 in o_spot and 9 in o_spot:
        win = 'You Lose!'
        winning = 10
        return redirect('/winning', code=302)
    if 1 in o_spot and 5 in o_spot and 9 in o_spot:
        win = 'You Lose!'
        winning = 10
        return redirect('/winning', code=302)
    if 3 in o_spot and 5 in o_spot and 7 in o_spot:
        win = 'You Lose!'
        winning = 10
        return redirect('/winning', code=302)
    if 1 in o_spot and 4 in o_spot and 7 in o_spot:
        winning = 10
        win = 'You Lose!'
        return redirect('/winning', code=302)
    if 2 in o_spot and 5 in o_spot and 8 in o_spot:
        win = 'You Lose!'
        winning = 10
        return redirect('/winning', code=302)
    if 9 in o_spot and 6 in o_spot and 3 in o_spot:
        win = 'You Lose!'
        winning = 10
        return redirect('/winning', code=302)
    winning = 10
    win = 'Tie!'
    return redirect('/winning')


@app.route('/winning', methods=['GET', 'POST'])

def winning():
    global winning
    global ailist
    global o_spot
    global x_spot
    if winning == 6:
        if request.method == 'POST':
            if request.form['spot'] == 'New Game':
                ailist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                x_spot = []
                o_spot = []
                return redirect('/', code=302)
        return render_template('index.html', choice=choice, choice2=choice2, choice3=choice3, choice4=choice4, choice5=choice5,submit=True, win=win)
    if winning == 7:
        if request.method == 'POST':
            if request.form['spot'] == 'New Game':
                ailist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                x_spot = []
                o_spot = []
                return redirect('/', code=302)
        return render_template('index.html', choice=choice, choice2=choice2, choice3=choice3, choice4=choice4, choice5=choice5, choice6=choice6, submit=True, win=win)
    if winning == 8:
        if request.method == 'POST':
            if request.form['spot'] == 'New Game':
                ailist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                x_spot = []
                o_spot = []
                return redirect('/', code=302)
        return render_template('index.html', choice=choice, choice2=choice2, choice3=choice3, choice4=choice4, choice5=choice5, choice6=choice6, choice7=choice7, submit=True, win=win)
    if winning == 9:
        if request.method == 'POST':
            if request.form['spot'] == 'New Game':
                ailist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                x_spot = []
                o_spot = []
                return redirect('/', code=302)
        return render_template('index.html', choice=choice, choice2=choice2, choice3=choice3, choice4=choice4, choice5=choice5, choice6=choice6, choice7=choice7,choice8=choice8, submit=True, win=win)
    
    if winning == 10:
        if request.method == 'POST':
            if request.form['spot'] == 'New Game':
                ailist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                x_spot = []
                o_spot = []
                return redirect('/', code=302)
        return render_template('index.html', choice=choice, choice2=choice2, choice3=choice3, choice4=choice4, choice5=choice5, choice6=choice6, choice7=choice7,choice8=choice8, choice9=choice9, submit=True, win=win)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)

        