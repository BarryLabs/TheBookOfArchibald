import random

# The Tome
quotes = [
    "This right here is right here.",
    "I swear i'll piss on his grandmama's grave.",
    "No Sir.",
    "I've been trying to tell you!",
]

def read_quote():
  quote = quotes[random.randint(0, len(quotes)-1)]
  print(quote)

def add_quote(new_quote):
  # Add the new quote to the tome
  quotes.append(new_quote)
  print("Quote added:", new_quote)

# Function
def main():
  # Print a welcome message
  print("Welcome to The Book of Archibald!")

  # Prompt the user for their choice
  choice = input("Would you like to (R)ead a quote or (A)dd a quote? ")

  # If the user wants to read a quote, call the read_quote function
  if choice.lower() == "r":
    read_quote()

  # If the user wants to add a quote, prompt for the quote and call the add_quote function
  elif choice.lower() == "a":
    new_quote = input("Enter the quote: ")
    add_quote(new_quote)
  else:
    print("Invalid choice. Please try again.")

main()
