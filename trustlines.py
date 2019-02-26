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

#Making everyone trust USD
builder = Builder(bob_secret , network='TESTNET').append_change_trust_op(
    asset_code='USD',asset_issuer=alice_public,limit=None, source=bob_public)
builder.sign()
resp = builder.submit()

builder = Builder(charlie_secret , network='TESTNET').append_change_trust_op(
    asset_code='USD',asset_issuer=alice_public,limit=None, source=charlie_public)
builder.sign()
resp = builder.submit()

builder = Builder(diana_secret , network='TESTNET').append_change_trust_op(
    asset_code='USD',asset_issuer=alice_public,limit=None, source=diana_public)
builder.sign()
resp = builder.submit()

#Making everyone trust INR
builder = Builder(bob_secret , network='TESTNET').append_change_trust_op(
    asset_code='INR',asset_issuer=charlie_public,limit=None, source=bob_public)
builder.sign()
resp = builder.submit()

builder = Builder(alice_secret , network='TESTNET').append_change_trust_op(
    asset_code='INR',asset_issuer=charlie_public,limit=None, source=alice_public)
builder.sign()
resp = builder.submit()

builder = Builder(diana_secret , network='TESTNET').append_change_trust_op(
    asset_code='INR',asset_issuer=charlie_public,limit=None, source=diana_public)
builder.sign()
resp = builder.submit()

#Making everyone trust YEN
builder = Builder(alice_secret , network='TESTNET').append_change_trust_op(
    asset_code='YEN',asset_issuer=bob_public,limit=None, source=alice_public)
builder.sign()
resp = builder.submit()

builder = Builder(charlie_secret , network='TESTNET').append_change_trust_op(
    asset_code='YEN',asset_issuer=bob_public,limit=None, source=charlie_public)
builder.sign()
resp = builder.submit()

builder = Builder(diana_secret , network='TESTNET').append_change_trust_op(
    asset_code='YEN',asset_issuer=bob_public,limit=None, source=diana_public)
builder.sign()
resp = builder.submit()


#Alice sends 1000 USD to Bob
builder = Builder(
    alice_secret, network='TESTNET').append_payment_op(
        destination=bob_public,
        amount='1000',
        asset_code='USD',
        asset_issuer=alice_public)
builder.sign()
resp = builder.submit()
print(resp)

#Charlie sends 1000 INR to Diana
builder = Builder(
    charlie_secret, network='TESTNET').append_payment_op(
        destination=diana_public,
        amount='1000',
        asset_code='INR',
        asset_issuer=charlie_public)
builder.sign()
resp = builder.submit()
print(resp)

#Bob sends 1000 Yen to Alice
builder = Builder(
    bob_secret, network='TESTNET').append_payment_op(
        destination=alice_public,
        amount='1000',
        asset_code='YEN',
        asset_issuer=bob_public)
builder.sign()
resp = builder.submit()
print(resp)