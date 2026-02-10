distance_mi = 20
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = True
if has_car or has_ride_share_app:
    if is_raining:
        print ('user took a car or booked a ride')
    else:
        print ('user took a car or a ride by choice')
elif has_bike and not is_raining:
    print('user took his bike')
if not distance_mi:
    print (False)
if distance_mi < 5:
    print('short distance covered')
elif distance_mi >=5 and distance_mi <=15:
    print('medium distance covered')
elif distance_mi >=15 and distance_mi <=19 :
    print('long distance covered')
else:
    print('Maximum distance covered')
if not is_raining:
    distance_mi < 1
    print(True)
if has_bike and not is_raining:
    distance_mi >1 and  distance_mi >= 6
    print (True)
if has_car or has_ride_share_app:
    distance_mi > 6 
    print(True)
else:
    print(False)