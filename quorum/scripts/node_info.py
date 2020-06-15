# https://github.com/ethereum/wiki/wiki/JSON-RPC#json-rpc-api-reference

# the methods are all defined here, check em out if you forget

import requests
import json

from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider



# change the node port to something else later

NODE_PORT = 22001 

PRIVATE_ABI = '[{"constant":true,"inputs":[],"name":"storedData","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"x","type":"uint256"}],"name":"set","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"get","outputs":[{"name":"retVal","type":"uint256"}],"payable":false,"type":"function"},{"inputs":[{"name":"initVal","type":"uint256"}],"payable":false,"type":"constructor"}]'

FIRST_TX = '0x58d58bf5b1bfc3ce5270953d4ff3c1067177390d86ac8ba974a1f6f286859473'

w3 = Web3(HTTPProvider(f'http://localhost:{NODE_PORT}'))


tx = w3.geth.admin.peers()[0]['enode']
print(tx)


# print([json.dumps(w3.geth.admin.peers()], indent=4, sort_keys=True))


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# convert from hex to int
def hexdec(hex): 
	return int(hex, 16)

# the name of the rpc method in a string
# the port is the rpc port. just the ending not the full url
def rpc_method(method, params, port, cleanhex=False, pretty_json=False):

	url = f'http://localhost:{port}'

	payload = {
		"method": method,
		"params" : params,
		"id": 67,
		"jsonrpc": "2.0"
	}


	response = requests.post(url, json=payload).json()

	try:

		result = response['result']

		if cleanhex == True:
			dec = hexdec(result) 
			print(f'{bcolors.OKGREEN}{method} {bcolors.ENDC} :  {dec}')

		elif pretty_json == True:
			print(f'{bcolors.OKGREEN}{method} {bcolors.ENDC} : ')
			print(json.dumps(result, indent=4, sort_keys=True))

		else: 
			print(f'{bcolors.OKGREEN}{method} {bcolors.ENDC} :  {result}')

		return result 
	except:
		print(f'{bcolors.FAIL}{response}{bcolors.ENDC}')


rpc_method('web3_clientVersion', [], NODE_PORT)
rpc_method('eth_syncing', [], NODE_PORT)
rpc_method('net_version', [], NODE_PORT)
rpc_method('net_listening', [], NODE_PORT)
rpc_method('net_peerCount', [], NODE_PORT, True)
rpc_method('eth_protocolVersion', [], NODE_PORT, True)
rpc_method('eth_coinbase', [], NODE_PORT)
rpc_method('eth_mining', [], NODE_PORT)
rpc_method('eth_hashrate', [], NODE_PORT)
rpc_method('eth_gasPrice', [], NODE_PORT)

first_acc = rpc_method('eth_accounts', [], NODE_PORT)
rpc_method('eth_blockNumber', [], NODE_PORT)
rpc_method('eth_getBalance', [first_acc[0], 'latest'], NODE_PORT, True)
rpc_method('eth_getTransactionCount', [first_acc[0], 'latest'], NODE_PORT, True)

rpc_method('eth_getTransactionByHash', [FIRST_TX], NODE_PORT, False, True)
contract_addr = rpc_method('eth_getTransactionReceipt', [FIRST_TX], NODE_PORT, False, True)['contractAddress']

# needed for the thing, otherwise it complains
checksum_contract_addr = Web3.toChecksumAddress(contract_addr)

print(f'{bcolors.WARNING}contract address is : {contract_addr} {bcolors.ENDC}')

# Let's try to call the Get on the contract

# print(Web3.isChecksumAddress(checksum_contract_addr))

private_contract = w3.eth.contract(address=checksum_contract_addr, abi=PRIVATE_ABI)

try:
	final_value = private_contract.functions.get().call()
	print(f'{bcolors.WARNING}private value is : {final_value} {bcolors.ENDC}')
except Exception as e:
	print(f'{bcolors.FAIL} {e} {bcolors.ENDC}')




# private contract address
# 0x58d58bf5b1bfc3ce5270953d4ff3c1067177390d86ac8ba974a1f6f286859473








