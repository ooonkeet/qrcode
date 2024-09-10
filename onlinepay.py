import qrcode
upi_id=input("Enter your upi id:- ")
# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('googlr_pay_qr.png')
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()