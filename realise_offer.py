from stellar_base.builder import Builder
from stellar_base.keypair import Keypair

#Alice
alice_secret =   'SDL4KWT5OLLDGX6PE5P2PRPFUFMANXRRABJ6HVBAY2YCNYOECIMRQYN2'
alice_public = Keypair.from_seed(alice_secret).address().decode()

#Bob
bob_secret = 'SCICYKDGHKKXG24T654QO6HU2MI6WNY2W5MSAZV6LIDHJ2V6XZIT66OF'
bob_public = Keypair.from_seed(bob_secret).address().decode()

#Charlie
charlie_secret = 'SCC757FBKA7C6MOIY4MR677R5L7NOXCQKNA6OOCKMPXPG7EZADWUGQ2M'
charlie_public = Keypair.from_seed(charlie_secret).address().decode()

#Diana
diana_secret = 'SAJ3WR4BWQPLLCBQKVVMMHBIKXUOOJ6MSCAZ6GCWDHVSWOESAMSZTLKT'
diana_public = Keypair.from_seed(diana_secret).address().decode()

#Offer 3 : Alice wants to buy 10 INR for 25 YEN per INR
selling_code = 'YEN'
selling_issuer = bob_public

buying_code = 'INR'
buying_issuer = charlie_public

price = '.04'
amount = '250'

builder = Builder(secret=alice_secret , horizon_uri='https://horizon-testnet.stellar.org').append_manage_offer_op(selling_code,selling_issuer,buying_code,buying_issuer,amount,price)
builder.sign()
builder.submit()


#Offer 4 : Charlie wants to buy 50 USD for 10 XLM per USD
selling_code = 'XLM'
selling_issuer = None

buying_code = 'USD'
buying_issuer = alice_public

price = '.1'
amount = '500'

builder = Builder(secret=charlie_secret , horizon_uri='https://horizon-testnet.stellar.org').append_manage_offer_op(selling_code,selling_issuer,buying_code,buying_issuer,amount,price)
builder.sign()
builder.submit()
