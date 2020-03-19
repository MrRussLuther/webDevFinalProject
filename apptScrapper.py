import mysql.connector

from craigslist import CraigslistHousing

bostonAreas = ['gbs', 'nwb', 'bmw', 'nos', 'sob']

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "Budgeting App"
)

cursor = mydb.cursor()

sql = ("""INSERT INTO `Apartments` (`ID`, `Name`, `URL`, `Price`, `Location`, `Geotag`) VALUES ('{}','{}','{}','{}','{}','{}');""")


for areas in bostonAreas:
    cl_h = CraigslistHousing(site='boston', area=areas, category='roo',
                      filters={'max_price': 2000, 'private_room': True})

    for result in cl_h.get_results(sort_by='newest', geotagged=True):
        id = result["id"]
        name = result["name"]
        url = result["url"]
        price = result["price"]
        location = result["where"]
        if result["geotag"]:
            geotag = '{} {}'.format(result["geotag"][0], result["geotag"][1] )
        else:
            geotag = "NULL"

        
        try:
            cursor.execute(sql.format(id, name, url, price, location, geotag), )
            mydb.commit()
            print(id)
        except:
            print("FAILED TO WRITE " +id +" TO DATABASE")
        



