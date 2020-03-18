from flask import Flask, flash, redirect, render_template, request, session, abort,jsonify
app = Flask(__name__,static_url_path='/static')

@app.route("/")
def charMap():
    return render_template(
    'index.html')
@app.route('/charMap/',methods = ['POST'])
def checkOneToOneMapping():
    s1 = str(request.form.get('s1', ''))
    s2= str(request.form.get('s2', ''))
        #If the length of first string is not equal to the second string return false
    Answer = 'Yes'
    if len(s1) != len(s2):
       Answer = 'No'
    else:
        mapDict ={}
        for i in range(0,len(s1)):
            #checking if the 
            if s1[i] not in mapDict:
                mapDict[s1[i]] = s2[i]
            else:
                if mapDict[s1[i]] != s2[i]:
                    Answer= 'No'
    data = {'answer' : Answer}
    data=jsonify(data)
    return data

if __name__ == "__main__":
    app.run()
