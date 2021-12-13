from web3 import Web3

import web3
from web3 import Web3


web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/8c996291ab3145a7aff040085ad34366'))

print(web3.isConnected())



balance = web3.eth.getBalance('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')
print(web3.fromWei(balance,"ether"))

