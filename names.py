def process_names():
  """Prompts user for names, sorts them, removes duplicates, and displays results."""
  names = ["Nyagol", "Eunice", "Wairimu", "Sizler", "Elvis","Wairimu", "Hamati", "Nyagol"]
  while True:
    name = input("Enter a name (or leave blank to finish): ")
    if not name:
      break
    names.append(name)

  # Remove duplicates and sort names
  unique_names = list(set(names))
  unique_names.sort()

  # Print results
  print("Total names entered:", len(names))
  print("Unique names (sorted):")
  for name in unique_names:
    print(name)

# Execute the function
process_names()
