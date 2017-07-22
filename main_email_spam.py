import re

email=open("emailSample2.txt",'r').read()
print(email)

email=email.lower()
email=re.sub(r'<[^<>]+>',' ',email)
email=re.sub(r'[^\s]+@[^\s]+','emailaddr',email)
email=re.sub(r'(http|https)://[^\s]*','httpaddr',email)
email=re.sub(r'[^\s]+@[^\s]+','emailaddr',email)
email=re.sub(r'[\d]+','number',email)
print(email)

