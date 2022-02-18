from flask import Flask, render_template, request
from replit import db
import sys
sys.path.append(".")
from Class import *
from attractions import storedAttr, attr

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
provinceListChecked = ['', '', '', '', '', '', '', '', '', '']

def remove_attr_to_list(attr):
  global returnList
  if db[attr] in returnList:
    returnList.remove(db[attr])

def remove_filter_from_list(val, actualVal):
  global provinceList
  global filters
  global checkList
  if val == "on":
    checkList[filters.index(actualVal)] = "checked"
    #print(filters.index(actualVal))
    for i in storedAttr:
      arr = i.get_data()
      if actualVal not in arr[2]:
        if arr in returnList:
          returnList.remove(arr)
    

def remove_prov_from_list(val, actualVal):
  global provinceList
  global filters
  global checkList
  if val == actualVal:
    checkList[provinceList.index(actualVal) + len(filters)] = "checked"
    for i in storedAttr:
      data = i.get_data()
      prov = data[0].split(", ")
      if data[0] != "" and actualVal not in prov[1]:
        if data in returnList:
          returnList.remove(data)

def clear_checkList():
  global checkList
  global filters
  global provinceList
  checkList = []
  for i in range(len(filters) + len(provinceList)):
    checkList.append('')

def add_attr_to_list(attr):
  global returnList
  if db[attr] in returnList:
    returnList.append(db[attr])


def add_records_to_list():
  global returnList
  returnList = []
  for i in storedAttr:
    rec = i.get_data()
    returnList.append(rec)

def remove_keys():
  keys = db.keys()
  for rec in keys:
    del db[rec]
#remove_keys()


def get_based_on_tags(park, amusement, museum, cave, historical, outdoor, scienceCenter, art, breakfast, province):
  
  keys = db.keys()
  global returnList
  global checkList
  checkList = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
  for record in keys:
    #print(record) 
    value = db[record]
    
    if (province == "norfolk"):
      checkList[0] = "checked"
      if ("Norfolk" not in value[0]):
        remove_attr_to_list(record)
    elif (province == "virginiabeach"):
      checkList[1] = "checked"
      if ("Virginia Beach" not in value[0]):
        remove_attr_to_list(record)
    elif (province == "richmond"):
      checkList[2] = "checked"
      if ("Richmond" not in value[0]):
        remove_attr_to_list(record)
    elif (province == "front royale"):
      checkList[3] = "checked"
      if ("Front Royal" not in value[0]):
        remove_attr_to_list(record)
    elif (province == "danville"):
      checkList[4] = "checked"
      if ("Danville" not in value[0]):
        remove_attr_to_list(record)
    elif (province == "luray"):
      checkList[5] = "checked"
      if ("Luray" not in value[0]):
        remove_attr_to_list(record)
    elif (province == "williamsburg"):
      checkList[13] = "checked"
      if ("Williamsburg" not in value[0]):
        remove_attr_to_list(record)
    elif (province == "natural bridge"):
      checkList[14] = "checked"
      if ("Natural Bridge" not in value[0]):
        remove_attr_to_list(record)
    elif (province == "charlottesville"):
      checkList[16] = "checked"
      if ("Charlottesville" not in value[0]):
        remove_attr_to_list(record)
    elif (province == "chesterfield"):
      checkList[17] = "checked"
      if ("Chesterfield" not in value[0]):
        remove_attr_to_list(record)
    

    if (park == "on"):
      checkList[6] = "checked"
      if ("Park" not in value[2]):
        remove_attr_to_list(record)

    if (park == "on"):
      checkList[6] = "checked"
      if ("Park" not in value[2]):
        remove_attr_to_list(record)
        
    if (amusement == "on"):
      checkList[7] = "checked"
      if ("Amusement" not in value[2]):
        remove_attr_to_list(record)

    if (museum == "on"):
      checkList[8] = "checked"
      if ("Museum" not in value[2]):
        remove_attr_to_list(record)

    if (cave == "on"):
      checkList[9] = "checked"
      if ("Cave" not in value[2]):
        remove_attr_to_list(record)

    if (historical == "on"):
      checkList[10] = "checked"
      if ("Historical" not in value[2]):
        remove_attr_to_list(record)

    if (outdoor == "on"):
      checkList[11] = "checked"
      if ("Outdoor" not in value[2]):
        remove_attr_to_list(record)

    if (scienceCenter == "on"):
      checkList[12] = "checked"
      if ("Science Center" not in value[2]):
        remove_attr_to_list(record)

    if (art == "on"):
      checkList[13] = "checked"
      if ("Art" not in value[2]):
        remove_attr_to_list(record)

    if (breakfast == "on"):
      checkList[15] = "checked"
      if ("Breakfast" not in value[2]):
        remove_attr_to_list(record)    

#print(storedAttr)
#print(storedAttr[1].get_data())

@app.route("/", methods=["POST", "GET"])
def main():
  global checkList
  global returnList
  add_records_to_list()
  #print(returnList)
  if request.method == "POST":
    clear_checkList()
    if (request.form['button'] == 'search'):

      for f in filters:
        remove_filter_from_list(request.form.get(f), f)
      for p in provinceList:
        #print(p)
        remove_prov_from_list(request.form.get("provinceSelector"), p)
      '''
      park = request.form.get("Park")
      amusement = request.form.get("Amusement")
      museum = request.form.get("Museum")
      cave = request.form.get("Cave")
      historical = request.form.get("Historical")
      outdoor = request.form.get("Outdoor")
      scienceCenter = request.form.get("ScienceCenter")
      art = request.form.get("Art")
      breakfast = request.form.get("Breakfast")
      province = request.form.get("provinceSelector")
      get_based_on_tags(park, amusement, museum, cave, historical, outdoor, scienceCenter, art, breakfast, province)'''
      print(checkList)
      return render_template("index.html", attraction = returnList, provinceList = provinceList, filters = filters, checkBoxes = checkList)
      
  elif request.method == "GET":
    clear_checkList()
    return render_template("index.html", attraction = attr, provinceList = provinceList, filters = filters, checkBoxes = checkList)

for i in range(0, len(storedAttr)):
  indvAttr = storedAttr[i].get_data()
  if "" != indvAttr[0]:
    split = indvAttr[0].split(", ")
    if split[1] not in provinceList:
      provinceList.append(split[1])
  if "" != indvAttr[2]:
    split = indvAttr[2].split(", ")
    for n in split:
      if (n not in filters) and ("Breakfast" not in n) and ("Lodging" not in n):
        filters.append(n)
  
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
