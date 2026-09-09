import boto3

# Connect to AWS DynamoDB
dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-south-1"
)

# Connect to the DynamoDB table
table = dynamodb.Table("Internship")

print("Successfully connected to AWS DynamoDB!")
print("Connected to table: Internship")

# Read all records from the table
response = table.scan()

print("\nIntern Records:")
print("-" * 40)

for item in response["Items"]:
    print("Name :", item.get("Name"))
    print("Role :", item.get("Role"))
    print("Email:", item.get("Email"))
    print("-" * 40)