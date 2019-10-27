import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test"]
col = db['test']
col.drop()

docs=[
    {'name':{'first':'wang','last':'ming'},'age':15,'score':[{'chi':60,'eng':70,'num':1},{'chi':80,'eng':65,'num':2}],'reward':[3,2,4]},
    {'name':{'first':'wei','last':'hong'},'age':17,'score':[{'chi':66,'eng':90,'num':1},{'chi':40,'eng':55,'num':2}],'reward':[1,6,4]},
    {'name':{'first':'li','last':'ben'},'age':14,'score':[{'chi':50,'eng':78,'num':1},{'chi':50,'eng':45,'num':2}],'reward':[5,2,4]},
]

col.insert_many(docs)

# 获取col,并对内部的列表排序
# 方法1:先更新,再获取
col.update_one({'age':15},{'$push': {'reward': {'$each': [],'$sort':-1}}})
col.find_one({'name.first':'wang'},{'name':1,'_id':0})

# 方法2:方法1的综合
col.find_one_and_update({'age':15},{'$push': {'reward': {'$each': [],'$sort':1}}},return_document=True)

# 方法3:使用聚合函数
res = col.aggregate([
    {'$match' : { "age" : 15 }},
    {'$unwind' : "$reward"},
    {'$sort': { "TestArr" : 1 }},
    {'$group':{'_id' : "$age",'reward' : {'$push':"$reward"}}}
])

list(res)
