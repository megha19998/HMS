import datetime
from hotel.models import room, booking

def check_availability(room, check_in, check_out):
    avail_list=[]
    booking_list = booking.objects.filter(room=room)
    for bookingg in booking_list:
        if bookingg.check_in>check_out or bookingg.check_out<check_in :  #check_in check_out is our and booking.check_in booking.check_out is in the database for that room
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list) #return true if all are true else false..... any everything true return false else true
