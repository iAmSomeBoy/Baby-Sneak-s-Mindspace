print("Enter weight in Earth")
weight= float(input())
print("Enter planet's number")
nth=int(input())

if nth== 1:
  desWeight= weight* 0.38
elif nth==2:
  desWeight= weight* 0.91
elif nth==3:
  desWeight= weight* 0.38
elif nth==4:
  desWeight= weight* 2.53
elif nth==5:
  desWeight= weight* 1.07
elif nth==6:
  desWeight= weight* 0.89
elif nth==7:
  desWeight= weight* 0.89

if nth>= 1 and nth<=7:
  print(desWeight)
else:
    print("Invalid planet number")


# Number	Planet	Relative Gravity
# 1	Mercury	0.38
# 2	Venus	0.91
# 3	Mars	0.38
# 4	Jupiter	2.53
# 5	Saturn	1.07
# 6	Uranus	0.89
# 7	Neptune	1.14