print("choose between 1 to 6 which action you want")
print("1 for Add visitor")
print("2 for Show visitors")
print("3 for Search visitor")
print("4 for Filter visitor")
print("5 for Update visitor status")
print("6 for Delete visitor")

visitors = [
    {"name": "Rahul", "flat": 101, "status": "Approved"},
    {"name": "Amit", "flat": 202, "status": "Pending"},
    {"name": "Raj", "flat": 303, "status": "Rejected"}
]

# def add_visitor():
#     name = input("Enter name:")
#     flat = int(input("Enter flat no:"))
#     status = input("Enter Status:")

#     visitor = {
#         "name": name,
#         "flat": flat,
#         "status": status
#     }

#     visitors.append(visitor)
#     print("Visitor Created Successfully.")
    

# def show_visitors():
#     if not visitors:
#         print("Visitors not registered yet...")
#     for index, visitor in enumerate(visitors, start=1):
#         print(f"\nVisitor {index}")
#         print("Name:", visitor["name"])
#         print("Flat:", visitor["flat"])
#         print("Status:", visitor["status"])
#         print("-----------------------")


# show_visitors() 

# def search_visitor():
#     search_name = input("Enter visitor name:")
#     for visitor in visitors:
#         if visitor["name"].lower() == search_name.lower():
#             print("Visitor found!")
#             print("Name:", visitor["name"])
#             print("Flat:", visitor["flat"])
#             print("Status:", visitor["status"])
#             return
#     print("Visitor not found!")

# search_visitor()

def filter_visitor():
    status = input("Enter status between Accepted/Pending/Rejected:")
    filtered_visitors = []

    for visitor in visitors:
        if visitor["status"].lower() == status.lower():
            filtered_visitors.append(visitor)

    if not filtered_visitors:
        print("No visitor found with this status")        
        return

    print(f"\n{status.title()} Visitors:")

    for index, visitor in enumerate(filtered_visitors, start=1):
        print(f"\nVisitor {index}")
        print("Name:", visitor["name"])
        print("Flat:", visitor["flat"])
        print("Status:", visitor["status"])

    print("Total visitors:", len(filtered_visitors))

filter_visitor()    



    



