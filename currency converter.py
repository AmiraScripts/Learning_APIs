import requests

base = input("enter the source currency \n").strip().upper()
target = input("enter the target currency \n").strip().upper()
amount = input("enter the amount you want to convert \n").strip()

if not amount.replace('.', '', 1).isdigit():
    print("❌ Please enter a valid number for amount.")
    exit()

url = f"https://api.frankfurter.app/latest"
params = {
    "from":base,
    "to": target,
    "amount":amount
}

response = requests.get(url, params=params)
data = response.json()
print(data)

if response.status_code==200 and data.get("sucess",False):
    result = data["result"]
    print(f"\n {amount} {base}= {result:.2f} {target}")
else:
    print("conversion failed!")