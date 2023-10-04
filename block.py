from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

w3 = Web3(Web3.HTTPProvider(ganache_url))


from_address="0x55b07d70f972aEFE09d100147a9888B46f535367"
to_address="0x9563D4931Ec8237D836CAe33D5b7371bBf7Ab447"
private_key="e58c2d65e064d33ae060b5ad789d4b4b7e8b5a85e058fb1784190595273967fa"
amount_ether=0.01

def send_ethereum(from_address, to_address, private_key, amount_ether):
    # Yuboruvchi manzilni tekshirish
    if not w3.is_address:
        print("Xatolik: Yuboruvchi manzil noto'g'ri formatda.")
        return
    
    # Qabul qiluvchi manzilni tekshirish
    if not w3.is_address(to_address):
        print("Xatolik: Qabul qiluvchi manzil noto'g'ri formatda.")
        return
    
    # Qabul qiluvchi manzilga jo'natilayotgan miqdorni wei (int) formatiga o'tkazish
    amount_wei = w3.to_wei(amount_ether, 'ether')
    
    # Yuboruvchi manzilning nonce'ini olish
    nonce = w3.eth.get_transaction_count(from_address)
    
    # Tranzaksiyani tuzish
    transaction = {
        'to': to_address,
        'value': amount_wei,
        'gas': 30000,
        'gasPrice': w3.to_wei('50', 'gwei'),  # O'zgartirishingiz mumkin
        'nonce': nonce,
    }
    
    # Tranzaksiyani yaratish va imzolash
    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
    
    # Tranzaksiyani yuborish
    transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    
    return transaction_hash

send_ethereum(from_address=from_address, to_address=to_address, private_key=private_key,amount_ether=amount_ether)

