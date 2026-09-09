import boto3

# Connect to AWS DynamoDB
dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-south-1"
)

# Connect to table
table = dynamodb.Table("Internship")

print("Successfully connected to AWS DynamoDB!")

# Insert a new intern record
new_intern = {
    "Name": "Aman Kumar",
    "Role": "Python Intern",
    "Email": "aman.kumar@gmail.com"
}

table.put_item(Item=new_intern)

print("\nNew intern added successfully!")
print("Name :", new_intern["Name"])
print("Role :", new_intern["Role"])
print("Email:", new_intern["Email"])

# Read all records
response = table.scan()

print("\nAll Intern Records:")
print("-" * 45)

for item in response["Items"]:
    print("Name :", item.get("Name"))
    print("Role :", item.get("Role"))
    print("Email:", item.get("Email"))
    print("-" * 45)