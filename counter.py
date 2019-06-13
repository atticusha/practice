import time
def counter():
    dayr=int(time.time()/86400)
    day=time.time()/86400
    hrsr=int((day-dayr)*24)
    hrs=(day-dayr)*24
    minzr=int((hrs-hrsr)*60)
    minz=(hrs-hrsr)*60
    secsr=int((minz-minzr)*60)
    print('It has been ' + str(dayr) + ' days ' + str(hrsr) + ' hours ' + str(minzr) + ' minutes and ' + str(secsr) + ' seconds since the epoch.')
