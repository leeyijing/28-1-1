from uobitems import uobitems , checkoutuobitems
from allredemption import allredemption
import operator
import datetime


def processallitems(name,cardno):
    allitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            points = points.strip()
            usert =points.split(",")
            if usert[0] == name and usert[1] == cardno:
                point.append(int(usert[2]))

        points = point[-1]
        individual_items = a.split(",")

        if (points >= int(individual_items[3])):
            c = uobitems(individual_items[1], individual_items[2], individual_items[3],
                individual_items[4], individual_items[5], individual_items[6],individual_items[7])
            maxquantity = points // int(individual_items[3])
            c.set_maxquantity(maxquantity)
            allitems.append(c)
    avaliableuobpts_file.close()
    return allitems


def processretailitems(name,cardno):
    retailitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point=[]
        for points in avaliableuobpts_file:
            usert =points.split(",")
            if usert[0] == name and usert[1] == cardno:
                point.append(int(usert[2]))
        avaliableuobpts_file.close()
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Retail"):
            if (points >= int(individual_items[3])):
                c = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                maxquantity = points // int(individual_items[3])
                c.set_maxquantity(maxquantity)
                retailitems.append(c)
    uobitems_file.close()
    return retailitems

def processdiningitems(name,cardno):
    diningitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            usert =points.split(",")
            if usert[0] == name and usert[1] == cardno:
                point.append(int(usert[2]))
        avaliableuobpts_file.close()
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Dining"):
            if (points >= int(individual_items[3])):
                d = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                maxquantity = points // int(individual_items[3])
                d.set_maxquantity(maxquantity)
                diningitems.append(d)
    uobitems_file.close()
    return diningitems


def processleisureitems(name,cardno):
    leisureitems = []
    uobitems_file = open("file/uobitems.txt", "r")
    for a in uobitems_file:
        avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
        point = []
        for points in avaliableuobpts_file:
            usert =points.split(",")
            if usert[0] == name and usert[1] == cardno:
                point.append(int(usert[2]))
        avaliableuobpts_file.close()
        points = point[-1]
        individual_items = a.split(",")
        if (individual_items[0] == "Leisure"):
            if (points >= int(individual_items[3])):
                e = uobitems(individual_items[1], individual_items[2], individual_items[3],
                             individual_items[4], individual_items[5], individual_items[6],individual_items[7])
                maxquantity = points // int(individual_items[3])
                e.set_maxquantity(maxquantity)
                leisureitems.append(e)
    uobitems_file.close()
    return leisureitems

def processredeemedpoints(name, cardno):
    redeemedpoint = 0
    try:
        redeemuobpts_file = open("file/redeemuobpts.txt", "r")

        for points in redeemuobpts_file:
            transaction = points.split()
            if transaction[0] == name:
                if transaction[1] == cardno:
                    redeemedpoint = transaction[2]

        redeemuobpts_file.close()
    finally:
        return redeemedpoint

def processcurrentpoints(name,cardno):
    #uob_allpoints =[]
    uob_currentpts = 0
    avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
    for j in avaliableuobpts_file:
        transaction = j.split(",")
        if transaction[0] == name and transaction[1] == cardno:
            uob_currentpts = transaction[2]
     #           uob_allpoints.append(int(transaction[2]))
    #uob_currentpts = uob_allpoints[-1]
    avaliableuobpts_file.close()
    return uob_currentpts


# in transaction history of redemption
def processallredemption(name,cardno):
    allredemptionList =[]
    allredemption_file = open("file/allredemption.txt", "r")
    for i in  allredemption_file:
        list = i.split(',')
        if list[0] == name:
            s = allredemption(list[1], list[2], list[3], list[4], int(list[5]),list[6])
            allredemptionList.append(s)
    allredemption_file.close()
    return allredemptionList

def processalluobredemption(name, cardno):
    alluobredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            bank = list[2].split(" ")
            if bank[0] == "UOB":
                y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                alluobredemptionList.append(y)
    allredemption_file.close()
    return alluobredemptionList

def processallocbcredemption(name, cardno):
    allocbcredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            bank = list[2].split(" ")
            if bank[0] == "OCBC":
                y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                allocbcredemptionList.append(y)
    allredemption_file.close()
    return allocbcredemptionList

def processalldbsredemption(name, cardno):
    alldbsredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            bank = list[2].split(" ")
            if bank[0] == "DBS":
                y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                alldbsredemptionList.append(y)
    allredemption_file.close()
    return alldbsredemptionList

def processsallnovredemption(name, cardno):
    allnovredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1]== "11" and individual[2]=="2017":
                z = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                allnovredemptionList.append(z)
    allredemption_file.close()
    return allnovredemptionList

def processuobnovredemption(name, cardno):
    uobnovredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "11" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "UOB":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    uobnovredemptionList.append(y)
    allredemption_file.close()
    return uobnovredemptionList

def processocbcnovredemption(name, cardno):
    ocbcnovredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "11" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "OCBC":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    ocbcnovredemptionList.append(y)
    allredemption_file.close()
    return ocbcnovredemptionList

def processdbsnovredemption(name, cardno):
    dbsnovredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "11" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "DBS":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    dbsnovredemptionList.append(y)
    allredemption_file.close()
    return dbsnovredemptionList

def processsalldecredemption(name, cardno):
    alldecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                z = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                alldecredemptionList.append(z)
    allredemption_file.close()
    return alldecredemptionList

def processuobdecredemption(name, cardno):
    uobdecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "UOB":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    uobdecredemptionList.append(y)
    allredemption_file.close()
    return uobdecredemptionList

def processocbcdecredemption(name, cardno):
    ocbcdecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "OCBC":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    ocbcdecredemptionList.append(y)
    allredemption_file.close()
    return ocbcdecredemptionList

def processdbsdecredemption(name, cardno):
    dbsdecredemptionList = []
    allredemption_file = open("file/allredemption.txt", "r")
    for i in allredemption_file:
        list = i.split(",")
        if list[0] == name:
            individual = list[1].split("/")
            if individual[1] == "12" and individual[2]=="2017":
                bank = list[2].split(" ")
                if bank[0] == "DBS":
                    y = allredemption(list[1], list[2], list[3], list[4], int(list[5]), list[6])
                    dbsdecredemptionList.append(y)
    allredemption_file.close()
    return dbsdecredemptionList




def processpreferreduob(name, cardno):
    uobpreferredList=[]
    qtyanditemdictionary = processget_quantityuob(name, cardno)  # returns a dictionary; {user:[[item1,qty1] , [] , [] ]
    qtyanditem = qtyanditemdictionary[name]

    avaliableuobpts_file = open("file/avaliableuobpts.txt", "r")
    point = []
    for currentpoints in avaliableuobpts_file:
        currentpoints = currentpoints.strip()
        usert = currentpoints.split(",")
        if usert[0] == name and usert[1] == cardno:
            point.append(int(usert[2]))
    avaliableuobpts_file.close()
    points = point[-1]

    alluobitems = open("file/uobitems.txt", "r")
    for individual in alluobitems:
        individual= individual.strip()
        individual=individual.split(",")
        b = individual[7]
        for i in qtyanditem:
            itemname=i[0]
            qty = i[1]
            if str(itemname) == str(b):
                if (points >= int(individual[3])):
                    preferreditems = uobitems(individual[1], individual[2], individual[3], individual[4],
                                            individual[5],individual[6], individual[7])
                    preferreditems.set_count(int(qty))
                    currentcount = preferreditems.get_count()
                    maxquantity = points // int(individual[3])
                    preferreditems.set_maxquantity(maxquantity)
                    uobpreferredList.append(preferreditems)
    avaliableuobpts_file.close()
    return uobpreferredList

def processget_quantityuob(name, cardno): #based on the quantity of your redemptionhistory
    dictionary={}
    dictvalue = []
    allredemption_file = open("file/allredemption.txt", "r")
    for redeemed in allredemption_file:
        lists = redeemed.split(",")
        bank = lists[2].split(" ")
        if lists[0] == name and lists[3]== cardno:
            if bank[0] == "UOB":
                individualitemandqty = []
                individualitemandqty.append(lists[4])
                individualitemandqty.append(int(lists[5]))
                dictvalue.append(individualitemandqty)
    allredemption_file.close()
    totals = {}
    for k, v in dictvalue:
        totals[k] = totals.get(k, 0) + v
    dictvalue = sorted(map(list, totals.items()))
    dictvalue = sorted(dictvalue, key=operator.itemgetter(1), reverse=True)


    if (len(dictvalue))> 3:
        empty = []
        for i in range(3):
            value = dictvalue[i]
            empty.append(value)
        dictionary[name] = empty

    else:
        dictionary[name] = dictvalue
    return dictionary

def Addtocart(firstname, lastname, age):
    userdata = firstname + ',' + lastname +',' + age +'\n'
    user_file = open('file/users.txt', 'a')
    user_file.write(userdata)

cart=[]
def cartdict(user, cardno, fullname, itempoint, currentpoint, redeempoint,quantity):
    totalitempt = int(itempoint) * int(quantity)
    pointsleft = int(currentpoint) - int(totalitempt)
    redeempoint = int(redeempoint) + int(totalitempt)
#current point left after redemption
    avaliablepointsdata = user + ',' + cardno + ',' + str(pointsleft) + '\n'
    avaliableuobpts_file = open("file/avaliableuobpts.txt", "a")
    avaliableuobpts_file.write(avaliablepointsdata)
    avaliableuobpts_file.close()
    #redemption point after remdeem
    redeempointsdata = user + ',' + cardno + ',' + str(redeempoint) + '\n'
    redeemuobpts_file = open("file/redeemuobpts.txt", "a")
    redeemuobpts_file.write(redeempointsdata)
    redeemuobpts_file.close()
    item = [user,cardno,fullname, itempoint, quantity, totalitempt]
    cart.append(item)
    redeemuobpts_file = open("file/uobcheckout.txt", "w")
    for items in cart:
        checkoutdata = items[0] + ',' + str(items[1]) + ',' + items[2] + ',' + str(items[3]) + ',' + str(items[4]) + ',' + str(items[5]) + '\n'
        print(checkoutdata)
        redeemuobpts_file.write(checkoutdata)
    redeemuobpts_file.close()

def checkout(name,cardno):
    uobcheckout=[]
    redeemuobpts_file = open("file/uobcheckout.txt", "r")
    for items in redeemuobpts_file:
        items = items.split(",")

        if items[0] == name:

            if items[1] == cardno:
                uobitems_file = open("file/uobitems.txt", "r")
                for a in uobitems_file:

                    a = a.strip()
                    a = a.split(",")
                    if a[7] == items[2]:
                        item = checkoutuobitems(a[1], a[2], a[3],a[4], a[5], a[6], a[7], items[4], items[5])
                        print(items[4])
                        uobcheckout.append(item)
    print(uobcheckout)
    return uobcheckout

"""
def enternameof(user, cardno,current_point, redeem_point, points, quantity):
    amount = int(points) * int(quantity)
    avaliableuobpts_file = open("file/avaliableuobpts.txt", "a")
    avaliableuobpts_file.write(user, cardno,int(current_point) - amount)
    avaliableuobpts_file.close()
    currentpoint_file = open("file/currentuobpts.txt", "a")
    currentpoint_file.write(user, cardno,int(redeem_point) + amount)
    currentpoint_file.close()



#def removefromcart(self, user, cardno,current_point, redeem_point, points, quantity):
#    avaliableuobpts_file = open("file/avaliableuobpts.txt", "a")
#    avaliableuobpts_file.write(user, cardno,int(current_point) - amount)
#    avaliableuobpts_file.close()
#    currentpoint_file = open("file/currentuobpts.txt", "a")
#    currentpoint_file.write(user, cardno,int(redeem_point) + amount)
#    currentpoint_file.close()



def processredemptionpoints(name,cardno):
    redeemuobpts_file = open("file/redeemuobpts.txt", "r+")
    for i in redeemuobpts_file:
        if i == "":
            userredeemptdata = name + ',' + cardno + ',' + 0 + '\n'
            redeemuobpts_file.write(userredeemptdata)
            print(userredeemptdata)
    for i in redeemuobpts_file:
        redeemuobpts_file.read()
"""
