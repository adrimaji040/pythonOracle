import json

with open('list_employees.json') as f:
    datadict = json.load(f)

# lambda function to sort the dictionary
datadict.sort(key=lambda person: person["status"])
print(datadict)
print("**********************************")

    # Make a second list where key="status" val="out"
    # using filter() with lambda
key = "status"
val = "out"
#emp = next(filter(lambda emp: emp.get(key) == val, data), None)
#emp = dict((key,value) for key, value in data.status if value == "out")
filtered_dictionary = {}
list_dictionaries = []

size = len(datadict)
for i in range(size):
    for (key, value) in datadict[i].items():
        if (key == 'status' and value == "out"):
            filtered_dictionary = datadict[i]
            list_dictionaries.append(filtered_dictionary)
print(list_dictionaries)
    


