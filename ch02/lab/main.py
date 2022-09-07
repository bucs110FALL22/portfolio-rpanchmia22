import random
#Part A
print("---------------------------------------------")
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = (classes * 7)
print("Classes per week:", classes_per_week)
cost_per_class = (cost_per_week // classes_per_week)
print("Cost per class:", cost_per_class)

print("---------------------")
print(weeks,type(weeks))
print(classes,type(classes))
print(tuition,type(tuition))
print(cost_per_week,type(cost_per_week))
print(classes_per_week,type(classes_per_week))
print(cost_per_class,type(cost_per_class))

#Part B
print("---------------------------------------------")
myList = []
myList.append("laptop")
myList.append("10")
myList.append("football")
myList.append("22")
myList.append("snow")
print(myList)
print(random.choice(myList))