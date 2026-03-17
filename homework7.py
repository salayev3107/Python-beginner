import json
data = {'model' : 'Malibu', 'Rang' : 'Qora', 'Yil' : 2020, 'Narx' : 40000}
data_json = json.dumps(data)
print(data_json)

# 

talaba_json = """{"ism": "Hasan","familiya":"Husanov","tyil":2000}"""
talaba_json1 = json.loads(talaba_json)
print(talaba_json1["ism"])
print(talaba_json1["familiya"])

#

with open('hwork.json','w') as file:
    json.dump(data,file)
with open('hwork2.json','w') as file:
    json.dump(talaba_json1,file)

#

filename = 'students.json'
with open(filename) as f:
    data1 = json.load(f)
for student1 in data1['student']:
    print(f'{student1['name']},{student1['lastname']},{student1['year']}')

#

fayl = 'api-result.json'
with open(fayl) as f2:
    data2 = json.load(f2)
    
print(data2['query']['pages']['13801']['title'])
print(data2['query']['pages']['13801']['extract'])
