#  [city A]   [city B]   [city C]   [City D]   [city E]
#        0          10        110        150        200 

#  volume  = 10L
#  consume = 2.5L/100km
#
city_A = 0
city_B = 400
city_C = 110
city_D = 150
city_E = 200

volume = 100      #L
consume = 11/100  #L/km

########### first destination ########
distance_1 = city_B - city_A
consume_1 = distance_1 * consume
if consume_1 <= volume:
    volume    = volume - consume_1
    print("The distance till first city B:", distance_1, "km")
    print(" The car will consume:",consume_1, "L", "remaing fuel:  ", volume, "L" )
else :
    print("Not enough fuel!!!")
########### second destination ########
distance_2 = city_C - city_B
consume_2 = distance_2 * consume
if consume_2 <= volume:
    volume    = volume - consume_2
    print("The distance till first city C:", distance_2, "km")
    print(" The car will consume:",consume_2, "L", "remaing fuel:  ", volume, "L" )
else :
    print("Not enough fuel for city C!!!")    
    ########### third destination ########
distance_3 = city_D - city_C
consume_3 = distance_3 * consume
if consume_3 <= volume:
    volume    = volume - consume_3
    print("The distance till first city D:", distance_3, "km")
    print(" The car will consume:",consume_3, "L", "remaing fuel:  ", volume, "L" )
else :
    print("Not enough fuel for city D!!!")    
    ########### fourth destination ########
distance_4 = city_E - city_D
consume_4 = distance_4 * consume
if consume_4 <= volume:
    volume    = volume - consume_4
    print("The distance till first city E:", distance_4, "km")
    print(" The car will consume:",consume_4, "L", "remaing fuel:  ", volume, "L" )
else :
    print("Not enough fuel for city E!!!")    

     
