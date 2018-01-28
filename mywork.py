from flask import Flask, render_template, request, session
from wtforms import Form, StringField, validators, IntegerField, SelectField
import tkinter.messagebox
import Processing
import uobitems
app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/uobrewardtrending')
def uobrewardtrending():
    return render_template('uobrewardtrending.html')

@app.route('/uobrewardtrendingpt')
def uobrewardtrendingpt():
    return render_template('uobrewardtrendingpt.html')

@app.route('/uobrewardall')
def uobrewardall():
    return render_template('uobrewardall.html')

@app.route('/uobrewardallpt')
def uobrewardallpt():
    return render_template('uobrewardallpt.html')

@app.route('/uobrewardretail')
def uobrewardretail():
    return render_template('uobrewardretail.html')

@app.route('/uobrewardretailpt')
def uobrewardretailpt():
    return render_template('uobrewardretailpt.html')

@app.route('/uobrewarddining')
def uobrewarddining():
    return render_template('uobrewarddining.html')

@app.route('/uobrewarddiningpt')
def uobrewarddiningpt():
    return render_template('uobrewarddiningpt.html')

@app.route('/uobrewardleisure')
def uobrewardleisure():
    return render_template('uobrewardleisure.html')

@app.route('/uobrewardleisurept')
def uobrewardleisurept():
    return render_template('uobrewardleisurept.html')

@app.route('/cart')
def cart():
    uobcheckoutList=[]
    uobcheckoutList = Processing.checkout(session['user'],session["cardno"])
    return render_template('cart.html', uobcheckout=uobcheckoutList)

@app.route('/alldecredemption')
def alldecredemption():
    alldecredemptionList = []
    alldecredemptionList = Processing.processsalldecredemption(session['user'], session["cardno"])
    return render_template('alldecredemption.html', alldecredemption=alldecredemptionList)

@app.route('/uobdecredemption')
def uobdecredemption():
    uobdecredemptionList = []
    uobdecredemptionList = Processing.processuobdecredemption(session['user'], session["cardno"])
    return render_template('uobdecredemption.html', uobdecredemptions=uobdecredemptionList)


@app.route('/ocbcdecredemption')
def ocbcdecredemption():
    ocbcdecredemptionList = []
    ocbcdecredemptionList = Processing.processocbcdecredemption(session['user'], session["cardno"])
    return render_template('ocbcdecredemption.html', ocbcdecredemptions=ocbcdecredemptionList)

@app.route('/dbsdecredemption')
def dbsdecredemption():
    dbsdecredemptionList = []
    dbsdecredemptionList = Processing.processdbsdecredemption(session['user'], session["cardno"])
    return render_template('dbsdecredemption.html', dbsdecredemptions=dbsdecredemptionList)


@app.route('/allnovredemption')
def allnovredemption():
    allnovredemptionList = []
    allnovredemptionList = Processing.processsallnovredemption(session['user'], session["cardno"])
    return render_template('allnovredemption.html', allnovredemption=allnovredemptionList)


@app.route('/uobnovredemption')
def uobnovredemption():
    uobnovredemptionList = []
    uobnovredemptionList = Processing.processuobnovredemption(session['user'], session["cardno"])
    return render_template('uobnovredemption.html', uobnovredemptions=uobnovredemptionList)


@app.route('/ocbcnovredemption')
def ocbcnovredemption():
    ocbcnovredemptionList = []
    ocbcnovredemptionList = Processing.processocbcnovredemption(session['user'], session["cardno"])
    return render_template('ocbcnovredemption.html', ocbcnovredemptions=ocbcnovredemptionList)


@app.route('/dbsnovredemption')
def dbsnovredemption():
    dbsnovredemptionList = []
    dbsnovredemptionList = Processing.processdbsnovredemption(session['user'], session["cardno"])
    return render_template('dbsnovredemption.html', dbsnovredemptions=dbsnovredemptionList)


@app.route('/allredemption')
def allredemption():
    allredemptionList = []
    allredemptionList = Processing.processallredemption(session['user'],session["cardno"])
    return render_template('allredemption.html', allredemptions=allredemptionList)

@app.route('/alluobredemption')
def alluobredemption():
    alluobredemptionList = []
    alluobredemptionList = Processing.processalluobredemption(session['user'], session["cardno"])
    return render_template('alluobredemption.html', alluobredemptions=alluobredemptionList)


@app.route('/allocbcredemption')
def allocbcredemption():
    allocbcredemptionList = []
    allocbcredemptionList = Processing.processallocbcredemption(session['user'], session["cardno"])
    return render_template('allocbcredemption.html', allocbcredemptions=allocbcredemptionList)


@app.route('/alldbsredemption')
def alldbsredemption():
    alldbsredemptionList = []
    alldbsredemptionList = Processing.processalldbsredemption(session['user'], session["cardno"])
    return render_template('alldbsredemption.html', alldbsredemptions=alldbsredemptionList)


    return render_template('alldbsredemption.html')

@app.route('/updateuobrewardretail')
def updateuobrewardretail():
    return render_template('updateuobrewardretail.html')

@app.route('/updateuobrewarddining')
def updateuobrewarddining():
    return render_template('updateuobrewarddining.html')

@app.route('/updatepart2uobdining')
def updatepart2uobdining():
    return render_template('updatepart2uobdining.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/catalogueuob',methods=['GET', 'POST'])
def catalogueuob():
    session["cart"]={}
    session['user']="Rubbish"
    session["cardno"]= "9888-6121-0824-1112"

    if request.method == 'POST':
        fullname = request.form["fullname"]
        itempoint = request.form["point"]
        currentpoint = request.form["currentpoint"]
        redeempoint = request.form["redeempoint"]
        quantity = request.form["quantity"]
        print(quantity )

        if quantity == "0":
            print("Enter a valid quantity!")
        else:
            Processing.cartdict(session['user'],session["cardno"],fullname, itempoint,currentpoint,redeempoint,quantity )
            print("You have successfully redeemed {} {}".format(quantity, fullname))
     #  listqty=Processing.list_qty(session['user'],session["cardno"])
    uob_redeempts = Processing.processredeemedpoints(session['user'],session["cardno"])
    uob_currentpts = Processing.processcurrentpoints(session['user'],session["cardno"])
    uob_preferreditems = Processing.processpreferreduob(session['user'],session["cardno"])
    uob_allitems = Processing.processallitems(session['user'],session["cardno"])
    uob_retialitems = Processing.processretailitems(session['user'],session["cardno"])
    uob_diningitems = Processing.processdiningitems(session['user'],session["cardno"])
    uob_leisureitems = Processing.processleisureitems(session['user'],session["cardno"])
    #user = session["user"], cardno = session["cardno"],



    return render_template('catalogueuob.html',uobcurrentpts=uob_currentpts, uobredeempts=uob_redeempts, uobpreferreditems = uob_preferreditems, uoballitems = uob_allitems,uobretialitems=uob_retialitems, uobdiningitems=uob_diningitems, uobleisureitems=uob_leisureitems)

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()
