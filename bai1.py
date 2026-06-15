Balance = 0
import logging 

logging.basicConfig(
    filename='momo_transactions.log', 
    level=logging.INFO, 
    format='[%(asctime)s] - [%(levelname)s] - [%(message)s]'
    )

def deposit(amount):
    global Balance
    if "-" in amount:
        logging.error("Money can't be negative!")
        print("Không được nhập số âm!")
        return 
    try: 
        Balance += int(amount)
        logging.info(f"Deposit successful +{amount}VND. Current balance: {Balance:,}")
        print(f"Nạp tiền thành công! số dư mới {Balance:,} VND")
    except ValueError:
        logging.error("Wrong type of data!")

def transfer(amount):
    global Balance
    if "-" in amount:
        logging.error("Money can't be negative!")
        print("Không được nhập số âm!")
        return 
    try: 
        if int(amount) > Balance:
            logging.warning(f"Transfer failed! Not enough balance to transfer {amount}VND. Current balance: {Balance:,}")
            print("Số dư không đủ để chuyển tiền!")
            return 
        if int(amount) >= 10000000:
            logging.info(f"Large transfer detected! Attempting to transfer {amount}VND. Current balance: {Balance:,}")
        Balance -= int(amount)
        logging.info(f"Transfer successful -{amount}VND. Current balance: {Balance:,}")
        print(f"Chuyển tiền thành công! số dư mới {Balance:,} VND")
    except ValueError:
        logging.error("Wrong type of data!")

while True:
    print("VÍ MOMO GIẢ LẬP".center(50,"="))
    print("""
        1. Nạp tiền vào ví
        2. Chuyển tiền 
        3. Xem số dư hiện tại 
        4. Thoát  
    """)
    print("=" * 50)
    choice = input("nhập vào lựa chọn (1 - 4):")
    match choice:
        case '1':
            money_amount = input("Nhập vào số tiền muốn nạp: ")
            deposit(money_amount)
        case '2':
            money_amount = input("Nhập vào số tiền muốn chuyển: ")
            transfer(money_amount)
        case '3':
            logging.info(f"Checked balance: {Balance:,} VND")
            print(f"Số dư hiện tại: {Balance:,} VND")
        case '4':
            break