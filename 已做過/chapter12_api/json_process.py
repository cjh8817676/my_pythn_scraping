import json

jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}' #讀取到json
jsonObj = json.loads(jsonString)

print(jsonObj.get('arrayOfNums'))

print(jsonObj.get('arrayOfNums')[1])

print(jsonObj.get('arrayOfNums')[1].get('number') + jsonObj.get('arrayOfNums')[2].get('number'))

print(jsonObj.get('arrayOfFruits')[2].get('fruit'))

'''
json處裡簡單例子
第一行是字典物件的清單
第二行是字典物件
第三行是整數(字典中整數的加總)
第四行是字串
'''