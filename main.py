from flask import Flask, render_template, request
import sys

sys.path.append(".")
from Class import *
from attractions import storedAttr, attr, firstAttrs


app = Flask(__name__)
#Creating Database
#Format is Address, Website, Tags, image address, name
#Tags made: Park, Amusement, Outdoor, Historical, Cave, Museum, Science Center, Lodging, Food
#Provinces: Virginia Beach, Norfolk, Danville, Richmond, Front Royale, Luray
#['Virginia Beach', 'Norfolk', 'Danville', 'Richmond', 'Front Royal', 'Willamsburg', 'Luray', 'Natural Bridge', 'Charlottseville', 'Chesterfield']
#"Park", "Amusement", "Cave", "Historical", "Outdoor", "Science Center", "Art"

returnList = []
filters = []
provinceList = []

mode = 0 #Mode is "and" mode by default

def filter_from_list(val, actualVal):
    global provinceList
    global filters
    global checkList
    global returnList
    global mode
    #check if the filter was checked
    if val == "on":
        #set the same index as the filter in its list in the checked list
        checkList[filters.index(actualVal)] = "checked"
        for i in storedAttr:
            arr = i.get_data()
            if mode == 1:
            #add attractions that meet the filters
                if actualVal in arr[2]:
                  if arr not in returnList:
                    returnList.append(arr)
                    
            elif mode == 0:
            #remove attractions that do not meet the filter
                if actualVal not in arr[2]:
                    if arr in returnList:
                        returnList.remove(arr)


def prov_from_list(val, actualVal):
    global provinceList
    global filters
    global checkList
    global mode
    #check if the the user selected the province
    if (val == "All Provinces" and actualVal == "All Provinces"):
      checkList[provinceList.index(actualVal) + len(filters)] = "checked"
    elif val == actualVal:
        #set the same index as the province in its list in the checked list
        checkList[provinceList.index(actualVal) + len(filters)] = "checked"
        for i in storedAttr:
            data = i.get_data()
            #Splits the address into an array
            prov = data[0].split(", ")
            if mode == 0:
            #remove attractions that are not in the selected province
                if actualVal not in prov[1]:
                    if data in returnList:
                        returnList.remove(data)
                    
            elif mode == 1:
                if actualVal not in prov[1]:
            	    if data in returnList:
                        returnList.remove(data)

#
def clear_checkList():
    global checkList
    global filters
    global provinceList
    checkList = []
    for i in range(len(filters) + len(provinceList)):
        checkList.append('')


def add_records_to_list():
    global returnList
    returnList = []
    #adds attractions to the list so they can be removed later on
    for i in storedAttr:
        rec = i.get_data()
        returnList.append(rec)


@app.route("/map", methods=["POST", "GET"])
def map():
    return render_template("other.html",key='AIzaSyCztFq5Me_V6Neh2RF9G0s9qoSQz9w2AvE')


@app.route("/modePage", methods=["POST", "GET"])
def modePage():
  global mode
  if mode == 0:
    mode = 1
    return str(mode) + ' now doing "or" displaying'
  elif mode == 1:
    mode = 0  
    return str(mode) + ' now doing "and" displaying'
  return ''

@app.route("/", methods=["POST", "GET"])
def main():
  return render_template("index.html")

@app.route("/search", methods=["POST", "GET"])
def search():
  #import global variables
  global checkList
  global returnList

  #Run if the user is sending data back
  if request.method == "POST":
  #Add the attractions to the returnList so they can be removed for a POST request. The POST includes the filters the user selected
    if mode == 0:
        add_records_to_list()
    elif mode == 1:
        returnList = []
    #clears the checklist because we don't know what the user checked yet
    clear_checkList()
    #Perform the operations if the button with search was pressed
    if (request.form['button'] == 'search'):
      
      #remove attractions that don't fit the filters the user wanted
      for f in filters:
        filter_from_list(request.form.get(f), f)
        #remove provinces from the list that the user didn't want
      for p in provinceList:
        prov_from_list(request.form.get("provinceSelector"), p)
      return render_template(
            "search.html",
            attraction=returnList,
            provinceList=provinceList,
            filters=filters,
            checkBoxes=checkList)

  #Runs if the user is not sending data back
  elif request.method == "GET":
      #clears the checklist because the user does not have anything checked
      clear_checkList()
      return render_template("index.html",
                             attraction=firstAttrs,
                             provinceList=provinceList,
                             filters=filters,
                             checkBoxes=checkList)

    
#create the "fitler" and "ProvinceList" that will be passed to the html
for i in range(0, len(storedAttr)):
    indvAttr = storedAttr[i].get_data()
    if "" != indvAttr[0]:
        split = indvAttr[0].split(", ")
        #print(split)
        if split[1] not in provinceList:
            provinceList.append(split[1])
    if "" != indvAttr[2]:
        split = indvAttr[2].split(", ")
        for n in split:
            if n not in filters:
                filters.append(n)
#Sort the provinces in alphabetical order
provinceList.sort()
filters.sort()
provinceList.insert(0, 'All Provinces')

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=80)