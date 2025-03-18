import csv
import gspread
import time

YEAR = '2025'

file = r"C:\Users\sophi\Finances\chase_statements.csv"

SUBSCRIPTION = {"amazon prime", "spotify", "max.com", "peacock"}
GAS = {"fuel", "tom thumb fs", "tiger mart"}
INCOME = {"zelle"}
IGNORE = {"online transfer"}

def hsbcFin(file, SUBSCRIPTION, GAS, INCOME, IGNORE):
    """
    Reads a CSV file, categorizes transactions, ignores certain transactions,
    and calculates the sum of expenses for each category.
    """

    category_totals = {
        "SUBSCRIPTION": 0,
        "GAS": 0,
        "FOOD/SHOPPING": 0,
        "INCOME": 0
    }
    transactions = []

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            if not row:
                continue

            try:
                details = row[0]
                date = row[1]
                name = row[2].strip().lower()
                amount = float(row[3])

                if any(ignore_term in name for ignore_term in IGNORE):
                    print(f"Skipping transaction: {name}")
                    continue

                category = 'FOOD/SHOPPING'
                if any(sub in name for sub in SUBSCRIPTION):
                    category = "SUBSCRIPTION"
                elif any(gas_item in name for gas_item in GAS):
                    category = "GAS"
                elif any(income_term in name for income_term in INCOME):
                    category = "INCOME"

                category_totals[category] += abs(amount)
                

            except IndexError:
                print(f"Skipping malformed row: {row}")
            except ValueError:
                print(f"Skipping row with invalid amount: {row}")

    # Print category totals for debugging (optional)
    print("\n--- Category Totals ---")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")
    print("-----")

    return category_totals  # Returns the category totals dictionary

# Authenticate with Google Sheets
sa = gspread.service_account()
sh = sa.open("Personal Finances")
wks = sh.worksheet(f"{YEAR}")

# Get category totals
category_totals = hsbcFin(file, SUBSCRIPTION, GAS, INCOME, IGNORE)

# Define the cells for each category as per request looking at Sheet3.jpg
cell_mapping = {
    "SUBSCRIPTION": 'C23',  # +8 for next month cell
    "GAS": 'C21',          # +8
    "FOOD/SHOPPING": 'C22',  # +8
    "INCOME": 'A25' # +8
}

# Prepare list of cells to update in Batch
cells_to_update = []

# Iterate over defined cells and add them with respective totals to the Update List
for category, cell in cell_mapping.items():
    if category in category_totals:
        total = category_totals[category]
        cells_to_update.append({'range': cell, 'values': [[total]]}) #Batch Write with Total
        print(f"Will update {category} total to cell: {cell} with value: {total}") #Log to ensure it all functions
    else:
        print(f"Warning: No total for category: {category}") #Catch errors

# Batch update to speed it up.
wks.batch_update(cells_to_update)
print("Category Totals updated in Google Sheets!")
