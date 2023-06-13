from flask import Flask,redirect,render_template,request
import flipkart_data

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        user_search = request.form['usearch']
        star = request.form['star']
        price = request.form['price']
        cdata = flipkart_data.extract_data(user_search)
        csdata = req_sort(cdata,star,price)
        tot = len(csdata)
        return render_template('view.html',cdata=csdata,tot=tot,u=user_search)
    return render_template('home.html')
    

def req_sort(cdata,star,price):
    fin_list = []

    if star and price:
        for each in cdata:
            if (each['rate'] >star) and (each['price'] < int(price) ):
                fin_list.append(each)
    elif star:
        for each in cdata:
            if (each['rate'] >star) :
                fin_list.append(each)
    
    elif price:
        for each in cdata:
            if (each['price']< int(price)) :
                fin_list.append(each)
    else :
        fin_list = cdata   
    return fin_list











if __name__ == '__main__':
    app.run(debug=True)









