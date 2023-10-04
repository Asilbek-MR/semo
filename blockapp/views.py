from django.shortcuts import render
from web3 import Web3
from django.contrib import messages

# Create your views here.

ganache_url = "http://127.0.0.1:7545"

w3 = Web3(Web3.HTTPProvider(ganache_url))

def index(request):
    if request.method == 'POST':
        to_address = request.POST.get('toaddres')
        from_address = request.POST.get('fromaddres')
        private_key = request.POST.get('privatekey')
        amount_ether = request.POST.get('amount')
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
            messages.success(request, 'Form submission successful')
            transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
            
            return transaction_hash
        
        send_ethereum(from_address=from_address, to_address=to_address, private_key=private_key,amount_ether=amount_ether)
    return render(request, 'index.html')