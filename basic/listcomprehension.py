cel=[39.0,50.3,37.8]
fahe=[((float(9)/5)*x+32)for x in cel]
print(fahe)



[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2+y**2==z**2]