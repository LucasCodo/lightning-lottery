import lnpay_py
from lnpay_py.wallet import LNPayWallet
import pyqrcode
import os

# init lnpay
lnpay_py.initialize(os.environ['lnpay_api_key'])

def get_invoice(num_satoshis=2,memo='{02,13,22,44,55,59}, ex@gmail.com'):
    my_wallet = LNPayWallet(os.environ['wallet_id'])
    invoice_params = {
        'num_satoshis': num_satoshis,
        'memo': memo
    }
    invoice = my_wallet.create_invoice(invoice_params)
    myqr = pyqrcode.create(str(invoice["payment_request"]))
    return invoice , myqr.png_as_base64_str(scale=6)

def get_transactions():
    my_wallet = LNPayWallet(os.environ['wallet_invoice'])
    transactions = my_wallet.get_transactions()
    return transactions
def get_info():
    my_wallet = LNPayWallet(os.environ['wallet_read'])
    info = my_wallet.get_info()
    return info

if __name__=="__main__":
    print(get_info())
