# Monthly Expense Calculator

A simple web application that helps you track and analyze your monthly expenses. The application calculates total expenses, average daily expenses, and identifies your top 3 largest expenses.

## Features

- Add and remove expense entries
- Calculate total monthly expenses
- Calculate average daily expenses (based on 30 days)
- Display top 3 largest expenses
- Simple and intuitive user interface
- No installation required - runs directly in your web browser

## How to Use

1. **Open the Application**
   - Open the `index.html` file in any modern web browser (Chrome, Firefox, Safari, Edge, etc.)

2. **Enter Your Expenses**
   - The application starts with one empty row
   - Enter the expense category (e.g., "Rent", "Groceries", "Entertainment")
   - Enter the amount in dollars (e.g., 1000, 500.50)
   - Click "Add Expense" button to add more rows if needed
   - Use the "Delete" button to remove unwanted entries

3. **Calculate Results**
   - After entering all your expenses, click the "Calculate" button
   - The results will show:
     - Total amount of expenses
     - Average daily expense (total ÷ 30 days)
     - Top 3 largest expenses in descending order

## Example

If you enter the following expenses:
- Rent: $40,000
- Groceries: $15,000
- Entertainment: $10,000
- Utilities: $5,000
- Transportation: $5,000

The results will show:
- Total Expenses: $75,000
- Average Daily Expense: $2,500
- Top 3 Expenses:
  1. Rent: $40,000
  2. Groceries: $15,000
  3. Entertainment: $10,000

## Notes

- All amounts should be entered in dollars
- The application assumes a 30-day month for average daily calculations
- You must enter at least one valid expense to calculate results
- Invalid entries (empty categories or non-numeric amounts) will be ignored
- You can modify entries at any time and recalculate the results

## Technical Details

- Built with pure HTML, CSS, and JavaScript
- No external dependencies or libraries required
- Works offline
- Compatible with all modern web browsers 