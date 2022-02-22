from Class import attractions




attr = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

storedAttr = []

attr[0] = ['6700 Azalea Garden Rd, Norfolk, VA 23518', 'https://norfolkbotanicalgarden.org/', 'Park, Outdoor', 'https://norfolkbotanicalgarden.org/wp-content/uploads/2017/04/13-perennial-b-hr.jpg', 'The Norfolk Botanical Gardens', '', '']
attr[1] = ['3500 Granby St, Norfolk, VA 23504', 'https://virginiazoo.org/', 'Park, Outdoor', 'https://virginiazoo.org/wp-content/themes/vazoo/template-parts/header/Virginia-Zoo-logo-300p.png', 'Norfolk Zoo', '', '']
attr[2] = ['21073 Skyline Drive, Front Royal, Virginia 22630', 'https://www.nps.gov/shen/index.htm', 'Park, Cave, Outdoor', 'https://www.nps.gov/shen/planyourvisit/images/20180807_SwiftRunEntrance_SNP5236_mo_3.jpg?maxwidth=1200&maxheight=1200&autorotate=false', 'Shenandoah National Park', '', '']
attr[3] =  ['3200 Mount Vernon Memorial Hwy, Mt Vernon, VA 22121', 'https://www.mountvernon.org/', 'Historical, Museum', 'https://mtv-main-assets.mountvernon.org/files/callout/card-full/image/dsc00033.jpg', 'Mount Vernon', '', '']
attr[4] =  ['1 Busch Gardens Blvd, Williamsburg, VA 23185', 'https://buschgardens.com/williamsburg/', 'Amusement, Park, Outdoor', 'https://seaworld.com/williamsburg/-/media/busch-gardens-williamsburg/images/logos/busch-gardens-williamsburg-logo-outlined.ashx?version=1_202012235536&la=en&hash=355C60FEF829D5ED5EA0B1394C7F54880FCA6F6C', 'Busch Gardens', '', '']
attr[5] =  ['101 Visitor Center Dr, Williamsburg, VA 23185', 'https://www.colonialwilliamsburg.org/', 'Historical, Outdoor', 'https://www.dailypress.com/resizer/hyeXiK6hZeyUsCSXBC4zMt__MN0=/1200x0/top/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/CKYPR45675GYHJ2X4DO4MDLXHM.jpg', 'Colonial Williamsburg', '', '']
attr[6] =  ['931 Thomas Jefferson Pkwy, Charlottesville, VA 22902', 'https://www.monticello.org/', 'Historical, Museum', 'https://monticello-www.s3.amazonaws.com/images/footer-lg.jpg', 'Monticello', '', '']
attr[7] = ['101 Cave Hill Rd, Luray, VA 22835', 'https://luraycaverns.com/', 'Cave, Museum', 'https://luraycaverns.com/wp-content/uploads/2018/07/luray-caverns-giants.jpg', 'Luray Caverns', '', '']
attr[8] = ['200 N Arthur Ashe Blvd, Richmond, VA 23220', 'http://www.vmfa.museum/', 'Museum', 'https://assets.simpleviewinc.com/simpleview/image/fetch/c_limit,q_75,w_1200/https://assets.simpleviewinc.com/simpleview/image/upload/crm/virginia/E201410_0402_1b8e0fd6-5056-a36a-0714fcaef4db8f57.jpg', 'Virginia Museum of Fine Arts', '', '']
attr[9] = ['1368 Colonial Parkway, Jamestown, Virginia', 'https://historicjamestowne.org/', 'Outdoor, Historical, Park', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/1639_Jamestown_Church_%282883847775%29.jpg/250px-1639_Jamestown_Church_%282883847775%29.jpg', 'Jamestown', '', '']
attr[10] = ['301 Main Street, Yorktown, VA 23690', 'https://www.visityorktown.org/', 'Museum, Outdoor', 'https://www.visityorktown.org/ImageRepository/Document?documentID=816', 'Yorktown', '', '']
attr[11] = ['15 Appledore Lane, Natural Bridge, VA 24578', 'https://www.dcr.virginia.gov/state-parks/natural-bridge', 'Park, Outdoor', 'https://www.dcr.virginia.gov/state-parks/image/data/nb-image-01.jpg', 'Natural Bridge of Virginia', '', '']
attr[12] = ['717 General Booth Blvd, Virginia Beach, VA 23451', 'https://www.virginiaaquarium.com/', 'Museum, Outdoor', 'https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,h_907,q_75,w_1100/v1/clients/virginiabeachva/RED_SEA05_f9b991e2-61d9-4293-bd54-437651ff1a30.jpg', 'Virginia Aquarium & Marine Science Center', '', '']
attr[13] = ['801 General Booth Blvd, Virginia Beach, VA 23451', 'https://myadventurepark.com/location/virginia-beach-va/', 'Outdoor, Amusement', 'https://30zhnx2odhzl2kels211p0eu-wpengine.netdna-ssl.com/wp-content/uploads/2019/08/virginia-logo-200x58.png', 'Adventure Park', '', '']
attr[14] = ['2500 W Broad St, Richmond, VA 23220', 'https://smv.org/', 'Museum, Science Center', 'https://smv.org/static/images/logo.png', 'Richmond Science Center', '', '']
attr[15] = ['677 Craghead St, Danville, VA 24541', 'https://dsc.smv.org/', 'Science Center', 'https://dsc.smv.org/static/images/logo.png', 'Danville Science Center', '', '']
attr[16] = ['2200 Parks Ave, Virginia Beach, VA 23451', 'https://virginiamoca.org/', 'Museum, Art', 'https://images.ctfassets.net/mcewm80m4225/3VozPM0ZQa14xh4EAUEZup/3fb09606252fb0be70071ce56f9d69b7/55Agnes_Grochulska_ARCHETYPES_3_20x26_inches_oil_on_canvas.jpg?w=1499&h=2008&q=50&fm=webp', 'Virginia Museum of Contemperary Art', '', '']
attr[17] = ['1822 Resort Drive, McGaheysville, VA 22840', 'https://www.massresort.com/', 'Outdoor, Park, Amusement', 'https://www.massresort.com/upload/cache/home_gallery.image/xs/homegallery_water_park-observation-web__1.jpg', 'Massanutten Resort', '', '']
attr[18] = ['9826 Midlothian Turnpike, North Chesterfield, 23235 ', 'https://www.bestwestern.com/en_US/book/hotels-in-north-chesterfield/best-western-plus-governor-s-inn/propertyCode.47077.html', 'Lodging', 'https://d2nuhorlnps36p.cloudfront.net/hotels/47077/47077_040_Exterior.jpg', 'Best Western Plus Governors Inn', '', '']
attr[19] = ['2000 Morton Dr, Charlottesville, VA 22903', 'https://englishinncharlottesville.com/', 'Lodging', 'https://englishinncharlottesville.com/assets/images/header_images/English-Inn-Header.jpg', 'English Inn', '', '']
attr[20] = ['229 Safari Ln, Natural Bridge, VA 24578', 'https://www.virginiasafaripark.com/', 'Outdoor, Park, Amusement', 'https://www.virginiasafaripark.com/resources/themes/gbzoo/assets/images/vsp-logo.png', 'Virginia Safari Park', '', '']
attr[21] = ['1113 Atlantic Ave, Virginia Beach, VA 23451', 'https://awhm.org/', 'Museum', 'http://awhm.org/wp-content/uploads/thegem-logos/logo_505e641b3b7aa720850fbc71486e86fe_1x.png', 'Atlantic Windfowl Heritage Museum', '', '']
attr[22] = ['Arlington National Cemetery, Arlington, VA 22211', 'https://www.arlingtoncemetery.mil', 'Outdoor, Park', 'https://www.arlingtoncemetery.mil/portals/0/ANC_logo_new.png', 'Arlington National Cemetery', '', '']
attr[23] = ['1290 Richmond Ave, Staunton', 'http://www.frontiermuseum.org/', 'Museum, Park, Outdoor', 'https://fblacompetition2022.danieltomov.repl.co/static/FCM.png', 'Frontier Culture Museum', '', '']
attr[24] = ['1341 Princess Anne Rd, Virginia Beach, VA 23457', 'https://militaryaviationmuseum.org/', 'Museum', 'https://militaryaviationmuseum.org/wp-content/uploads/2018/04/MAM-HeaderLogosmall.png', 'Military Aviation Museum', '', '']
attr[25] = ['780 University Blvd, Harrisonburg, VA 22807', 'https://www.jmu.edu/arboretum/index.shtml', 'Park, Outdoor', 'https://fblacompetition2022.danieltomov.repl.co/static/Arboretum.png', 'Edith J. Carrier Arboretum', '', '']
attr[26] = ['', '', '', '', '', '', '']
attr[27] = ['', '', '', '', '', '', '']
attr[28] = ['', '', '', '', '', '', '']
attr[29] = ['', '', '', '', '', '', '']
attr[30] = ['', '', '', '', '', '', '']
attr[31] = ['', '', '', '', '', '', '']
attr[32] = ['', '', '', '', '', '', '']
attr[33] = ['', '', '', '', '', '', '']
attr[34] = ['', '', '', '', '', '', '']
attr[35] = ['', '', '', '', '', '', '']
attr[36] = ['', '', '', '', '', '', '']
attr[37] = ['', '', '', '', '', '', '']
attr[38] = ['', '', '', '', '', '', '']
attr[39] = ['', '', '', '', '', '', '']
attr[40] = ['', '', '', '', '', '', '']
attr[41] = ['', '', '', '', '', '', '']
attr[42] = ['', '', '', '', '', '', '']
attr[43] = ['', '', '', '', '', '', '']
attr[44] = ['', '', '', '', '', '', '']
attr[45] = ['', '', '', '', '', '', '']
attr[46] = ['', '', '', '', '', '', '']
attr[47] = ['', '', '', '', '', '', '']
attr[48] = ['', '', '', '', '', '', '']
attr[49] = ['', '', '', '', '', '', '']
attr[50] = ['', '', '', '', '', '', '']
attr[51] = ['', '', '', '', '', '', '']

for a in attr:
  storedAttr.append(attractions(a[0], a[1], a[2], a[3], a[4], a[5], a[6]))