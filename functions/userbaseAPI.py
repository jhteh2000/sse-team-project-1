import requests
import json


# Replace with your Supabase URL and API key
supabase_url = "https://yydcqovanzimrbpfmfue.supabase.co"
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl5ZGNxb3ZhbnppbXJicGZtZnVlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDEyNjI5OTcsImV4cCI6MjAxNjgzODk5N30.UDzFMe3qANp8-PwUoS4f2bCC3g3KiTk5ieZWgrDzjC8"
auth_api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl5ZGNxb3ZhbnppbXJicGZtZnVlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMTI2Mjk5NywiZXhwIjoyMDE2ODM4OTk3fQ.WTHLhx4Djm9jf5c5JuNhRc915ZX_BIg1xdittVKB_sI'

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

# Example usage
data = get_data_from_table(tableName)
print(data)
