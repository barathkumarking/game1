from flask import Flask,render_template,url_for,request,redirect
import random
app=Flask(__name__)
@app.route('/')
def game1():
  return render_template('base.html')  
@app.route('/game',methods=['POST','GET'])
def game():
    
    c=int(request.form['nm'])
    lis=[1,2,3,4,5,6]
    b=random.choice(lis)
    return render_template('base.html',a=b,d=c)


  
    
    
        
    

if __name__=='__main__':
     app.run(debug=True)
