from load_data import load_data


def top_countries(shipping_data, number):
  """Print the top countries based on the number of shipments.

  Args:
    shipping_data: A list of shipment dictionaries containing country data.
    number: The number of top countries to print.
  """
  list_of_countries = []
  dict_of_countries = {}
  for ship in shipping_data:
    list_of_countries.append(ship["COUNTRY"])
  for country in list_of_countries:
    if country in dict_of_countries:
      dict_of_countries[country] += 1
    else:
      dict_of_countries[country] = 1

  sorted_countries = {k:v for k,v in sorted(dict_of_countries.items(), key = lambda item:item[1], reverse = True)} 
  for country in list(sorted_countries.keys())[:number]:
    print(country)


def show_countries(shipping_data):
  """Print all unique countries found in the shipping data.

  Args:
    shipping_data: A list of shipment dictionaries containing country data.
  """
  list_of_countries = []
  for ship in shipping_data:
    list_of_countries.append(ship["COUNTRY"])
  unique_countries = set(list_of_countries) 
  for country in unique_countries:
    print(country)


def menu():
  """Display the available commands for the user."""
  print("help") 
  print("show_countries")
  print("top_countries <num_countries>")


def main():
  """Load the shipping data and run the interactive program menu."""
  all_data = load_data()
  data = all_data["data"] 
  menu()
  while True: 
    user_choice = input("Enter your choice: ")
    if user_choice == "help":
      menu()
    elif user_choice == "show_countries":
      show_countries(data)
    else:
      number = int(user_choice.split(" ")[1])
      top_countries(data, number)


if __name__ ==  "__main__":
  main()