visitors = [
    {
        "name":"Jitesh",
        "flat":"A-101",
        "status":"Pending"
    },
    {
        "name":"Amit",
        "flat":"B-202",
        "status":"Approved"  
    },
    {
        "name":"Rakesh",
        "flat":"B-404",
        "status":"Pending"
    }
]

# for visitor in visitors:
#     if visitor["name"] == "Jitesh":
#         print(visitor)

# approved = []
# for visitor in visitors:
#     if visitor["status"] == "Approved":
#         approved.append(visitor)  
#         print(approved)      

for visitor in visitors:
    if visitor["name"] == "Jitesh":
        visitor["name"] = "Nitesh"
        print(visitor)
