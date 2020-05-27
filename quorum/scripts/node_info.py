# https://github.com/ethereum/wiki/wiki/JSON-RPC#json-rpc-api-reference

# the methods are all defined here, check em out if you forget

import requests
import json


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


rpc_method('web3_clientVersion', [], 22000)
rpc_method('eth_syncing', [], 22000)
rpc_method('net_version', [], 22000)
rpc_method('net_listening', [], 22000)
rpc_method('net_peerCount', [], 22000, True)
rpc_method('eth_protocolVersion', [], 22000, True)
rpc_method('eth_coinbase', [], 22000)
rpc_method('eth_mining', [], 22000)
rpc_method('eth_hashrate', [], 22000)
rpc_method('eth_gasPrice', [], 22000)
first_acc = rpc_method('eth_accounts', [], 22000)
rpc_method('eth_blockNumber', [], 22000)
rpc_method('eth_getBalance', [first_acc[0], 'latest'], 22000, True)
rpc_method('eth_getTransactionCount', [first_acc[0], 'latest'], 22000, True)
rpc_method('eth_getTransactionByHash', ['0x58d58bf5b1bfc3ce5270953d4ff3c1067177390d86ac8ba974a1f6f286859473'], 22000, False, True)
rpc_method('eth_getTransactionReceipt', ['0x58d58bf5b1bfc3ce5270953d4ff3c1067177390d86ac8ba974a1f6f286859473'], 22000, False, True)


# private contract address
# 0x58d58bf5b1bfc3ce5270953d4ff3c1067177390d86ac8ba974a1f6f286859473








