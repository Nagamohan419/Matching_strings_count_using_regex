from flask import Flask,render_template,request
import re
name=""
regex=""

app=Flask(__name__)

#####################################
@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/search',methods=['POST','GET'])
def search():
    global name, regex,count
    if request.method == 'POST':
        name=request.form["in_1"]
        regex=request.form["in_2"]
        #count=0
        #for exp in name:
           # if exp in regex:
             #   count+=1
        x=re.findall(regex,name)
        y=len(x)
            
    return render_template('search1.html',n=name,c=y,i=regex)


if __name__=='__main__':
    app.run(debug=True,port='5001')