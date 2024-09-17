import requests

def get_exchange_rate(from_currency, to_currency):
  """Fetches the exchange rate between two currencies."""
  url = f"https://api.exchangeratesapi.io/v1/latest?access_key=7d5026d685ff143d88b350e2f8371cbb&base={from_currency}&symbols={to_currency}"
  response = requests.get(url)
  data = response.json()
  return data['rates'][to_currency]

def convert_currency(amount, from_currency, to_currency):
  """Converts an amount from one currency to another."""
  exchange_rate = get_exchange_rate(from_currency, to_currency)
  converted_amount = amount * exchange_rate
  return converted_amount

def main():
  """Main function to handle user input and output."""
  amount = float(input("Enter the amount: "))
  from_currency = input("Enter the currency to convert from: ").upper()
  to_currency = input("Enter the currency to convert to: ").upper()

  converted_amount = convert_currency(amount, from_currency, to_currency)
  print(f"{amount} {from_currency} is equivalent to {converted_amount} {to_currency}")

if __name__ == "__main__":

  main()