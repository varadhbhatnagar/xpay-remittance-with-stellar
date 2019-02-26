from stellar_base.keypair import Keypair
from stellar_base.utils import StellarMnemonic
from stellar_base.address import Address
import requests

for i in range(1,5):
    sm = StellarMnemonic()
    secret_phrase = sm.generate()
    kp = Keypair.deterministic(secret_phrase)
    publickey = kp.address().decode()
    seed = kp.seed().decode()
    url = 'https://friendbot.stellar.org'
    r = requests.get(url, params={'addr': publickey})

    print('Account Created ')
    print('Public Key' , publickey)
    print('Seed' , seed)
