import Lnpay
import pyqrcode
import os

Public = Lnpay.Public()
Public.importkey(os.environ['public_lnpay_api_key'])
Wallet = Lnpay.Wallet()
keys = {'wallet_read':str(os.environ['wallet_read']),
        'wallet_id':str(os.environ['wallet_id']),
        'wallet_invoice':str(os.environ['wallet_invoice']),
        'wallet_admin':str(os.environ['wallet_admin'])}

Wallet.importkeys(keys)

def get_invoice(num_satoshis=2,passthru={},memo='{02,13,22,44,55,59}, ex@gmail.com',expiry=600):
    # init lnpay
    invoice = Wallet.newinvoice(num_satoshis,passthru,memo,expiry)
    myqr = pyqrcode.create(str(invoice["payment_request"]))
    return {"invoice": invoice , "QRBASE64": myqr.png_as_base64_str(scale=6)}

def get_transactions():
    return Wallet.transactions()
def get_info():
    return Wallet.balance()

if __name__=="__main__":
    print(Wallet.balance())
    print(Wallet.transactions())
    invoice = Wallet.newinvoice(2,memo="teste,asdfasd@asdf.com",expiry=600)
    myqr = pyqrcode.create(str(invoice["payment_request"]))
    print(invoice)
    print(myqr.png_as_base64_str(scale=6))
