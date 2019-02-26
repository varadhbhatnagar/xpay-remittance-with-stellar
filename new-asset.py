from stellar_base.keypair import Keypair
from stellar_base.asset import Asset
from stellar_base.builder import Builder

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

#Create new asset USD issued by Alice
my_asset1 = Asset('USD',alice_public)

#Create new asset INR issued by Charlie
my_asset2 = Asset('INR',charlie_public)

#Create new asset YEN issued by Diana
my_asset3 = Asset('YEN',bob_public)

