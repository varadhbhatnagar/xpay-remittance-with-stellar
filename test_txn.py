from stellar_base.builder import Builder
from stellar_base.keypair import Keypair

#Simple Transactions

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

# Bob transfers 500 YEN to Alice
builder = Builder(
    bob_secret, network='TESTNET').append_payment_op(
        destination=alice_public,
        amount='500',
        asset_code='YEN',
        asset_issuer=bob_public)
builder.sign()
resp = builder.submit()
print(resp)


