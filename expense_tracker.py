import pandas as pd
import matplotlib.pyplot as plt
import os

if os.path.exists('trackss.csv'):
    df = pd.read_csv('trackss.csv')
else:
    tracker = {'Date': [],
               'Month': [],
               'Category': [],
               'Amount': [],
               'Description': []}
    df = pd.DataFrame(tracker)

while True:
    menu = input('''
 1. Add Expense
 2. View Expenses
 3. Show Summary
 4. Show Charts
 5. Delete Expenses
 6. Exit
 Enter choice: ''')

    if menu == '1':
        date = input('Enter date and month (e.g. 9 march): ')
        month = date.split(' ')[1]
        category = input('Enter category: ')
        try:
            amt = int(input('Enter amount spent: '))
        except ValueError:
            print('Invalid amount, please enter a number')
            continue
        des = input('Enter description: ')

        new_row = pd.DataFrame({'Date': [date], 'Month': [month],
                                'Category': [category], 'Amount': [amt],
                                'Description': [des]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv('trackss.csv', index=False)
        print('Expense saved!')

    elif menu == '2':
        print('\n--- All Expenses ---')
        print(df.to_string(index=False))
        print(f'\nTotal Spent: ₹{df["Amount"].sum()}')

    elif menu == '3':
        grp = input('''Summarize by:
 1. Date
 2. Month
 Enter choice: ''')
        if grp == '1':
            print('\n--- Spending by Date ---')
            print(df.groupby('Date')['Amount'].sum())
        elif grp == '2':
            print('\n--- Spending by Month ---')
            print(df.groupby('Month')['Amount'].sum())

    elif menu == '4':
        print('Generating charts...')

        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        fig.suptitle('Expense Analysis', fontsize=16)

        # Chart 1 — Bar chart by category
        cat_data = df.groupby('Category')['Amount'].sum()
        axes[0].bar(cat_data.index, cat_data.values, color='steelblue')
        axes[0].set_title('Spending by Category')
        axes[0].set_xlabel('Category')
        axes[0].set_ylabel('Amount (₹)')
        axes[0].tick_params(axis='x', rotation=45)

        # Chart 2 — Pie chart
        axes[1].pie(cat_data.values, labels=cat_data.index, autopct='%1.1f%%')
        axes[1].set_title('Expense Breakdown')

        # Chart 3 — Line chart by month
        month_data = df.groupby('Month')['Amount'].sum()
        axes[2].plot(month_data.index, month_data.values,
                     marker='o', color='green', linewidth=2)
        axes[2].set_title('Spending by Month')
        axes[2].set_xlabel('Month')
        axes[2].set_ylabel('Amount (₹)')

        plt.tight_layout()
        plt.show()

    elif menu == '5':
        sure=input('Are you sure you want to drop all the entries ?(yes/no)')
        if sure.lower() == 'yes':
            df=df.iloc[0:0]
            df.to_csv('trackss.csv',index=False)
            print('All expenses deleted')
        else:
            print('cancelled')    


    elif menu == '6':
        print('Goodbye!')
        break

    else:
        print('Invalid choice, please enter 1-6')


       
       
      
      
   
    

    