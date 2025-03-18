# Finance Tracker

This Python script automates the process of categorizing transactions from a CSV file (e.g., bank statements) and uploading the category totals to a Google Sheet.  It's designed to help you track your spending and income efficiently.

## Features

*   **CSV Parsing:** Reads transaction data from a CSV file.
*   **Transaction Categorization:**  Categorizes transactions into predefined categories (Subscription, Gas, Food/Shopping, Income).
*   **Ignore List:** Skips transactions based on keywords.
*   **Google Sheets Integration:**  Uploads category totals to a specified Google Sheet and worksheet.
*   **Batch Updates:** Uses Google Sheets API batch updates for faster performance.
*   **Error Handling:** Includes basic error handling for malformed rows and invalid amounts.

## Prerequisites

Before running this script, you'll need to:

1.  **Install Required Libraries:**

    ```
    pip install gspread csv
    ```

2.  **Set up Google Sheets API Credentials:**

    *   Enable the Google Sheets API: Go to the [Google Cloud Console](https://console.cloud.google.com/) and enable the Google Sheets API.
    *   Create a Service Account: Create a service account and download the credentials file (JSON).  Make sure to give the service account editor permissions.
    *   Share Your Spreadsheet: Share the Google Sheet with the service account's email address.

## Configuration

1.  **Set the `file` variable:**  Modify the `file` variable in the script to point to the correct path of your CSV file.

    ```
    file = r"C:\Users\sophi\Finances\chase_statements.csv"
    ```

2.  **Configure Categories:** Adjust the `SUBSCRIPTION`, `GAS`, `INCOME`, and `IGNORE` sets to match your specific needs.  Add or remove keywords as necessary.  Make sure all keywords are in lowercase for accurate matching.

    ```
    SUBSCRIPTION = {"amazon prime", "spotify", "max.com", "peacock"}
    GAS = {"fuel", "tom thumb fs", "tiger mart"}
    INCOME = {"zelle"}
    IGNORE = {"online transfer"}
    ```

3.  **Set the `YEAR` variable:**  Update the `YEAR` variable to the relevant year.  This determines which worksheet in your Google Sheet will be updated.

    ```
    YEAR = '2025'
    ```

4.  **Update Cell Mappings:**  Modify the `cell_mapping` dictionary to match the exact cells in your Google Sheet where you want the category totals to be written.  This is crucial for the script to update the correct cells.

    ```
    cell_mapping = {
        "SUBSCRIPTION": 'C23',
        "GAS": 'C21',
        "FOOD/SHOPPING": 'C22',
        "INCOME": 'A25'
    }
    ```

## Usage

1.  **Place Credentials File:** Make sure your Google Sheets API credentials file (the JSON file you downloaded) is in the same directory as the Python script, or specify the correct path when authenticating with `gspread`.

2.  **Run the Script:**  Execute the Python script.

    ```
    python your_script_name.py
    ```

3.  **Check Google Sheets:**  Verify that the category totals have been updated correctly in your Google Sheet.

## Troubleshooting

*   **Authentication Errors:** Double-check that you've correctly set up the Google Sheets API credentials and shared the spreadsheet with the service account.
*   **File Not Found Errors:** Ensure that the path to your CSV file is correct.
*   **Incorrect Totals:** Review your category keywords and the `cell_mapping` to make sure they are accurate.
*   **API Errors:** Check the Google Cloud Console for any API usage limits or errors.
*   **KeyError:** KeyError usually means that the category names are not matching the cell mappings. Review your defined categories and the cell mappings.
*   **Malformed CSV Rows:** Ensure your CSV file is properly formatted and doesn't contain any unexpected characters or missing fields.

## Improvements and Future Enhancements

*   **Date Range Filtering:**  Add the ability to filter transactions by date range.
*   **More Flexible Categorization:** Implement more sophisticated categorization logic, possibly using regular expressions or machine learning.
*   **Configuration File:** Use a configuration file (e.g., JSON or YAML) to store settings like file paths, category keywords, and cell mappings.
*   **Error Logging:** Implement more robust error logging to a file.
*   **Command-Line Arguments:**  Add command-line arguments to specify the year, CSV file, and other options.
*   **Automated Scheduling:**  Use a task scheduler (e.g., cron) to run the script automatically on a regular basis.
*   **GUI:** Develop a graphical user interface (GUI) for easier configuration and use.

