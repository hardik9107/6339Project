from flask import Flask, request, render_template, redirect, url_for, session
import Ratings as r
import Recommendations as reco
import Authenticate as auth

app = Flask(__name__)

app.secret_key='asdftery'


@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/login',methods=['GET','POST'])
def login():     
    if request.method== 'POST':  
        param1=request.form['param1']
        session['user']=param1
        #globals()['param1']=request.form['param1']        
        param2=request.form['param2']
        x=auth.main(param1,param2)
        if(x==1):
            return redirect(url_for('loggedin'))
        else:
            return redirect(url_for('login'))
    
    return render_template('data.html')


@app.route('/loggedin',methods=['GET','POST'])
def loggedin(): 
    #print (session['user'])
    if request.method== 'POST':
            business=request.form['business']
            #param2=request.form['par2']
            rating = r.main(session['user'],business)
            session['business']=business
            return render_template('/Rating.html',obj = rating)
    #return session['user']       
    return render_template('loggedin.html')

@app.route('/Rating',methods=['GET','POST'])
def Rating():
    if request.method== 'POST':
        recommendations = reco.main(session['user'])        
        return render_template('Recommendation.html',obj = recommendations)
    return render_template('Rating.html')
    
@app.route('/Recommendation',methods=['GET','POST'])
def Recommendation():
#    if request.method== 'POST':
#        recommendations = reco.main(session['user'])        
#        return render_template('Recommendation.html',obj = recommendations)
    return render_template('Recommendation.html')

@app.route('/logout')
def logout():
    session['user']=''
    session['business']=''    
    return redirect(url_for('login'))
        
if __name__ == '__main__':
    app.run()