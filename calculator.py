import time

def display_menu():
    print('\n1. Check Balance')
    print('2. Withdraw')
    print('3. Deposit')
    print('4. Transaction History')
    print('5. Transfer')
    print('6. Quit')

def check_balance(balance):
    print(f'Your current balance is {balance}.')

def withdraw(balance, transaction_history):
    withdraw_amt = get_numeric_input('Please enter withdraw amount: ')
    if withdraw_amt is None:
        return balance

    if withdraw_amt > balance:
        print('Insufficient balance.')
    else:
        balance -= withdraw_amt
        transaction_history.append(f'Withdrawn: {withdraw_amt}')
        print(f'{withdraw_amt} is debited from your account.')
        print(f'Your updated balance is {balance}.')
    return balance

def deposit(balance, transaction_history):
    deposit_amt = get_numeric_input('Please enter deposit amount: ')
    if deposit_amt is None:
        return balance

    balance += deposit_amt
    transaction_history.append(f'Deposited: {deposit_amt}')
    print(f'{deposit_amt} is credited to your account.')
    print(f'Your updated balance is {balance}.')
    return balance

def show_transaction_history(transaction_history):
    print('Transaction History:')
    if not transaction_history:
        print('No transactions yet.')
    else:
        for transaction in transaction_history:
            print(transaction)

def transfer(balance, transaction_history):
    transfer_amt = get_numeric_input('Please enter transfer amount: ')
    if transfer_amt is None:
        return balance

    transfer_acc = input('Please enter account number to transfer to: ')
    if transfer_amt > balance:
        print('Insufficient balance.')
    else:
        balance -= transfer_amt
        transaction_history.append(f'Transferred: {transfer_amt} to account {transfer_acc}')
        print(f'{transfer_amt} is transferred to account {transfer_acc}.')
        print(f'Your updated balance is {balance}.')
    return balance

def get_numeric_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print('Invalid input. Please enter a numeric value.')
        return None

def main():
    print('Please insert your card')
    time.sleep(1)

    password = 2622
    balance = 5000
    transaction_history = []

    pin = get_numeric_input('Enter your PIN: ')
    if pin is None:
        return

    if pin == password:
        while True:
            display_menu()
            option = get_numeric_input('Please enter your choice: ')
            if option is None:
                continue

            if option == 1:
                check_balance(balance)
            elif option == 2:
                balance = withdraw(balance, transaction_history)
            elif option == 3:
                balance = deposit(balance, transaction_history)
            elif option == 4:
                show_transaction_history(transaction_history)
            elif option == 5:
                balance = transfer(balance, transaction_history)
            elif option == 6:
                print('Thank you for using our service.')
                break
            else:
                print('Invalid option. Please try again.')
    else:
        print('You entered the wrong PIN.')

if __name__ == "__main__":
    main()