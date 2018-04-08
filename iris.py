# Darren Keenan 2018-03-04
# Exercise 5 - Iris Data Set
# https://en.wikipedia.org/wiki/Iris_flower_data_set

columnname = "petal length", "petal width", "sepal length", "sepal width", "name"
print(columnname)

with open("data/iris.csv") as iris:
    for cmandname in iris:
        i = cmandname.split(",")
        print(i[0],i[1],i[2],i[3],i[4])
