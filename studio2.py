MPG = 108
e = True

GPY = 14032/MPG
kWh = GPY*33.7

if e:
    costCOR = kWh*0.1116
    costCS = kWh*0.3
    print("E-gallons/year: "+ str(GPY))
    print("cost/year corvallis: "+str(costCOR))
    print("cost/year charger: "+str(costCS))

else:
    costOR = 4.72*GPY
    costCAL = 5.92*GPY
    print("gallons/year: "+ str(GPY))
    print("cost/year OR: "+str(costOR))
    print("cost/year CA: "+str(costCAL))

test

