list = [1, 2, 3, 4, 5]
embedded_list = [[1,2,3],[4,5,6]]
dict = {1:{"name":"Bronson","money":"$5"},2:{"name":"Masha","money":"$6"}}

for data in embedded_list:
    for element in data:
        print(element)

for item in dict.values():
    print(item)
