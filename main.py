from flask import Flask, render_template, request
from replit import db

app = Flask(__name__)
#Creating Database
#Format is Address, Website, Tags, image address, name
#Tags made: Park, Amusement, Outdoor, Historical, Cave, Museum, Science Center, Lodging, Breakfast
#Provinces: Virginia Beach, Norfolk, Danville, Richmond, Front Royale, Luray
db["Botanical Garden"] = ['6700 Azalea Garden Rd, Norfolk, VA 23518', 'https://norfolkbotanicalgarden.org/', 'Park, Outdoor', 'https://norfolkbotanicalgarden.org/wp-content/uploads/2017/04/13-perennial-b-hr.jpg', 'The Norfolk Botanical Gardens']
db["Norfolk Zoo"] = ['3500 Granby St, Norfolk, VA 23504', 'https://virginiazoo.org/', 'Park, Outdoor', 'https://virginiazoo.org/wp-content/themes/vazoo/template-parts/header/Virginia-Zoo-logo-300p.png', 'Norfolk Zoo']
db["Shenandoah National Park"] =  ['21073 Skyline Drive, Front Royal, Virginia 22630', 'https://www.nps.gov/shen/index.htm', 'Park, Cave', 'https://www.nps.gov/shen/planyourvisit/images/20180807_SwiftRunEntrance_SNP5236_mo_3.jpg?maxwidth=1200&maxheight=1200&autorotate=false', 'Shenandoah National Park']
db["Mount Vernon"] =  ['3200 Mount Vernon Memorial Hwy, Mt Vernon, VA 22121', 'https://www.mountvernon.org/', 'Historical, Museum', 'https://mtv-main-assets.mountvernon.org/files/callout/card-full/image/dsc00033.jpg', 'Mount Vernon']
db["Busch Gardens"] =  ['1 Busch Gardens Blvd, Williamsburg, VA 23185', 'https://buschgardens.com/williamsburg/', 'Amusement, Park, Outdoor', 'https://seaworld.com/williamsburg/-/media/busch-gardens-williamsburg/images/logos/busch-gardens-williamsburg-logo-outlined.ashx?version=1_202012235536&la=en&hash=355C60FEF829D5ED5EA0B1394C7F54880FCA6F6C', 'Busch Gardens']
db["Colonial Williamsburg"] =  ['101 Visitor Center Dr, Williamsburg, VA 23185', 'https://www.colonialwilliamsburg.org/', 'Historical, Outdoor', 'https://www.dailypress.com/resizer/hyeXiK6hZeyUsCSXBC4zMt__MN0=/1200x0/top/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/CKYPR45675GYHJ2X4DO4MDLXHM.jpg', 'Colonial Williamsburg']
db["Monticello"] =  ['931 Thomas Jefferson Pkwy, Charlottesville, VA 22902', 'https://www.monticello.org/', 'Historical, Museum', 'https://monticello-www.s3.amazonaws.com/images/footer-lg.jpg', 'Monticello']
db["Luray Caverns"] = ['101 Cave Hill Rd, Luray, VA 22835', 'https://luraycaverns.com/', 'Cave, Museum', 'https://luraycaverns.com/wp-content/uploads/2018/07/luray-caverns-giants.jpg', 'Luray Caverns']
db["Virginia Museum of Fine Arts"] = ['200 N Arthur Ashe Blvd, Richmond, VA 23220', 'http://www.vmfa.museum/', 'Museum', 'https://assets.simpleviewinc.com/simpleview/image/fetch/c_limit,q_75,w_1200/https://assets.simpleviewinc.com/simpleview/image/upload/crm/virginia/E201410_0402_1b8e0fd6-5056-a36a-0714fcaef4db8f57.jpg', 'Virginia Museum of Fine Arts']
db["Jamestown"] = ['1368 Colonial Parkway, Jamestown, Virginia', 'https://historicjamestowne.org/', 'Outdoor, Historical, Park', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/1639_Jamestown_Church_%282883847775%29.jpg/250px-1639_Jamestown_Church_%282883847775%29.jpg', 'Jamestown']
db["Yorktown"] = ['301 Main Street, Yorktown, VA 23690', 'https://www.visityorktown.org/', 'Museum, Outdoor', 'https://www.visityorktown.org/ImageRepository/Document?documentID=816', 'Yorktown']
db["Natural Bridge of Virginia"] = ['15 Appledore Lane, Natural Bridge, VA 24578', 'https://www.dcr.virginia.gov/state-parks/natural-bridge', 'Park, Outdoor', 'https://www.dcr.virginia.gov/state-parks/image/data/nb-image-01.jpg', 'Natural Bridge of Virginia']
db["Virginia Aquarium"] = ['717 General Booth Blvd, Virginia Beach, VA 23451', 'https://www.virginiaaquarium.com/', 'Museum, Outdoor', 'https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_907,q_75,w_1100/v1/clients/virginiabeachva/RED_SEA05_f9b991e2-61d9-4293-bd54-437651ff1a30.jpg', 'Virginia Aquarium & Marine Science Center']
db["Adventure Park"] = ['801 General Booth Blvd, Virginia Beach, VA 23451', 'https://myadventurepark.com/location/virginia-beach-va/', 'Outdoor, Amusement', 'https://30zhnx2odhzl2kels211p0eu-wpengine.netdna-ssl.com/wp-content/uploads/2019/08/virginia-logo-200x58.png', 'Adventure Park']
db["Richmond Science Center"] = ['2500 W Broad St, Richmond, VA 23220', 'https://smv.org/', 'Museum, Science Center', 'https://smv.org/static/images/logo.png', 'Richmond Science Center']
db["Danville Science Center"] = ['677 Craghead St, Danville, VA 24541', 'https://dsc.smv.org/', 'Science Center', 'https://dsc.smv.org/static/images/logo.png', 'Danville Science Center']
db["Moca"] = ['2200 Parks Ave, Virginia Beach, VA 23451', 'https://virginiamoca.org/', 'Museum, Art', 'https://images.ctfassets.net/mcewm80m4225/3VozPM0ZQa14xh4EAUEZup/3fb09606252fb0be70071ce56f9d69b7/55Agnes_Grochulska_ARCHETYPES_3_20x26_inches_oil_on_canvas.jpg?w=1499&h=2008&q=50&fm=webp', 'Virginia Museum of Contemperary Art']
db["Massanutten "] = ['', 'https://www.massresort.com/', 'Outdoor, Park, Amusement', 'https://www.massresort.com/upload/cache/home_gallery.image/xs/homegallery_water_park-observation-web__1.jpg', '']
db[""] = ['', '', '', '', '']
db["English Inn"] = ['2000 Morton Dr, Charlottesville, VA 22903', 'https://englishinncharlottesville.com/', 'Lodging, Breakfast', '', 'English Inn']
db["Safari Park"] = ['229 Safari Ln, Natural Bridge, VA 24578', 'https://www.virginiasafaripark.com/', 'Outdoor, Park, Amusement', 'https://www.virginiasafaripark.com/resources/themes/gbzoo/assets/images/vsp-logo.png', 'Virginia Safari Park']
db["Wildfowl Museum"] = ['1113 Atlantic Ave, Virginia Beach, VA 23451', 'https://awhm.org/', 'Museum', 'http://awhm.org/wp-content/uploads/thegem-logos/logo_505e641b3b7aa720850fbc71486e86fe_1x.png', 'Atlantic Windfowl Heritage Museum']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
db["Monticello"] = ['', '', '', '', '']
returnList = []

def remove_attr_to_list(attr):
  global returnList
  if db[attr] in returnList:
    returnList.remove(db[attr])

def add_attr_to_list(attr):
  global returnList
  if db[attr] in returnList:
    returnList.append(db[attr])


def add_records_to_list():
  global returnList
  returnList = []
  keys = db.keys()
  for rec in keys:
    returnList.append(db[rec])

def remove_keys():
  keys = db.keys()
  for rec in keys:
    del db[rec]
#remove_keys()

def get_based_on_tags(park, amusement, museum, cave, historical, outdoor, scienceCenter, art, breakfast, province):
  keys = db.keys()
  global returnList
  global checkList
  checkList = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
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
    

    if (park == "on"):
      checkList[6] = "checked"
      if ("Park" not in value[2]):
        #print("park")
        #print(value[4])
        remove_attr_to_list(record)

    if (park == "on"):
      checkList[6] = "checked"
      if ("Park" not in value[2]):
        #print("park")
        #print(value[4])
        remove_attr_to_list(record)
        
    if (amusement == "on"):
      checkList[7] = "checked"
      if ("Amusement" not in value[2]):
        #print("amusement")
        #print(value[4])
        remove_attr_to_list(record)

    if (museum == "on"):
      checkList[8] = "checked"
      if ("Museum" not in value[2]):
        #print("museum")
        #print(value[4])
        remove_attr_to_list(record)

    if (cave == "on"):
      checkList[9] = "checked"
      if ("Cave" not in value[2]):
        #print("cave")
        #print(value[4])
        remove_attr_to_list(record)

    if (historical == "on"):
      checkList[10] = "checked"
      if ("Historical" not in value[2]):
        #print("historical")
        #print(value[4])
        remove_attr_to_list(record)

    if (outdoor == "on"):
      checkList[11] = "checked"
      if ("Outdoor" not in value[2]):
        #print("outdoor")
        #print(value[4])
        remove_attr_to_list(record)

    if (scienceCenter == "on"):
      checkList[12] = "checked"
      if ("Science Center" not in value[2]):
        #print("Science Center")
        #print(value[4])
        remove_attr_to_list(record)
    if (art == "on"):
      checkList[13] = "checked"
      if ("Art" not in value[2]):
        #print("Science Center")
        #print(value[4])
        remove_attr_to_list(record)

    if (breakfast == "on"):
      checkList[15] = "checked"
      if ("Breakfast" not in value[2]):
        #print("Science Center")
        #print(value[4])
        remove_attr_to_list(record)    


@app.route("/", methods=["POST", "GET"])
def main():
  global checkList
  global returnList
  add_records_to_list()
  if request.method == "POST":
    if (request.form['button'] == 'search'):

      park = request.form.get("park")
      amusement = request.form.get("amusement")
      museum = request.form.get("museum")
      cave = request.form.get("cave")
      historical = request.form.get("historical")
      outdoor = request.form.get("outdoor")
      scienceCenter = request.form.get("scienceCenter")
      art = request.form.get("art")
      breakfast = request.form.get("breakfast")
      province = request.form.get("provinceSelector")
      get_based_on_tags(park, amusement, museum, cave, historical, outdoor, scienceCenter, art, breakfast, province)

      #print(returnList)
      #print(checkList)
      return render_template("index.html", attraction = returnList, checkBoxes = checkList)
      
  elif request.method == "GET":
    checkList = []
    checkList = ['', '', '', '', '', '', '', '', '', '', '', '', '']
    return render_template("index.html", attraction = returnList, checkBoxes = checkList)
  
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
