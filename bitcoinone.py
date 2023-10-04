from blockcypher import get_address_overview

def get_bitcoin_balance(address):
    try:
        address_overview = get_address_overview(address)
        balance = address_overview['final_balance'] / 10**8  # Satoshidan Bitcoin ga o'tkazish
        return balance
    except Exception as e:
        print(f"Manzil malumotlarini olishda xatolik yuz berdi: {e}")
        return None

def main():
    bitcoin_address = input("Bitcoin manzilni kiriting: ")
    balance = get_bitcoin_balance(bitcoin_address)

    if balance is not None:
        print(f"{bitcoin_address} manzilingizning balansi: {balance} BTC")

if __name__ == "__main__":
    main()


