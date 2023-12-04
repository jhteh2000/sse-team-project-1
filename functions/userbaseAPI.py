import requests
import json
import supabase


# Replace with your Supabase URL and API key
supabase_url = "https://yydcqovanzimrbpfmfue.supabase.co"
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl5ZGNxb3ZhbnppbXJicGZtZnVlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDEyNjI5OTcsImV4cCI6MjAxNjgzODk5N30.UDzFMe3qANp8-PwUoS4f2bCC3g3KiTk5ieZWgrDzjC8"
auth_api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl5ZGNxb3ZhbnppbXJicGZtZnVlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMTI2Mjk5NywiZXhwIjoyMDE2ODM4OTk3fQ.WTHLhx4Djm9jf5c5JuNhRc915ZX_BIg1xdittVKB_sI'

#Initialise the Supabase Client
supabase_client = supabase.create_client(supabase_url,auth_api_key)

headers = {
    "apikey": auth_api_key,
    "Authorization": "Bearer " + auth_api_key,
    "Content-Type": "application/json"
}

tableName = "LoginInfo"

# Example: GET request to fetch data from a table
def get_data_from_table(table_name):
    
    response = requests.get(f"{supabase_url}/rest/v1/{table_name}", headers=headers)
    if response.status_code == 200:
        print("Request success!")
        return response.json()
    else:
        return "Error: " + response.text

Data_to_insert = {
    "first_name": "Test_name2",
    "last_name": "Test_lastname2",
    "username (email)": "Test_email2",
    "password": "Test_password2"
}

def add_details_to_table(table_name, Data_to_insert):
    #response = supabase_client.table(table_name).insert([Data_to_insert]).execute()
    data, count = supabase_client.table(table_name).insert([Data_to_insert]).execute()

def return_user_info(table_name, username):
    data, count = supabase_client.table(table_name).select('*').eq('username (email)', username).execute()
    return data
    
# Example usage
#add_details_to_table(tableName, Data_to_insert)
data = get_data_from_table(tableName)
print("This is the original data: ")
print(data)
info_data = return_user_info(tableName, "Test_email2")
print("\n")
print("The data requested is:")
#Somehow I have to put in [1][0] before
#print(info_data)
print(info_data[1][0]['first_name'])