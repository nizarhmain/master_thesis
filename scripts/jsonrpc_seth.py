'''
curl -d '{"jsonrpc": "2.0", "method": "eth_sendTransaction", "id": 2, "params": [{"from": "0xbf90562eca5e1b0d725f0590a59b61dd47c7c1de", "data": "0x608060405234801561001057600080fd5b50610239806100206000396000f300608060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680631ab06ee514610067578063812600df1461009e5780639507d39a146100cb578063c20efb901461010c575b600080fd5b34801561007357600080fd5b5061009c6004803603810190808035906020019092919080359060200190929190505050610139565b005b3480156100aa57600080fd5b506100c960048036038101908080359060200190929190505050610193565b005b3480156100d757600080fd5b506100f6600480360381019080803590602001909291905050506101c2565b6040518082815260200191505060405180910390f35b34801561011857600080fd5b50610137600480360381019080803590602001909291905050506101de565b005b80600080848152602001908152602001600020819055507f545b620a3000f6303b158b321f06b4e95e28a27d70aecac8c6bdac4f48a9f6b38282604051808381526020018281526020019250505060405180910390a15050565b600160008083815260200190815260200160002054016000808381526020019081526020016000208190555050565b6000806000838152602001908152602001600020549050919050565b6001600080838152602001908152602001600020540360008083815260200190815260200160002081905550505600a165627a7a72305820db9e778e020441599ea5a4c88fbc38a17f36647f87712224f92815ad23c3d6a00029"}]}' -H "Content-Type: application/json" http://localhost:3030
'''


import requests
import json


def main():
    url = "http://localhost:3030"


    # Example echo method
    payload = {
        "method": "eth_sendTransaction",
        "params": [ { "from": '0xadeba846153e9d956be969fe98f8980361699fc9', "data": "0x608060405234801561001057600080fd5b50610239806100206000396000f300608060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680631ab06ee514610067578063812600df1461009e5780639507d39a146100cb578063c20efb901461010c575b600080fd5b34801561007357600080fd5b5061009c6004803603810190808035906020019092919080359060200190929190505050610139565b005b3480156100aa57600080fd5b506100c960048036038101908080359060200190929190505050610193565b005b3480156100d757600080fd5b506100f6600480360381019080803590602001909291905050506101c2565b6040518082815260200191505060405180910390f35b34801561011857600080fd5b50610137600480360381019080803590602001909291905050506101de565b005b80600080848152602001908152602001600020819055507f545b620a3000f6303b158b321f06b4e95e28a27d70aecac8c6bdac4f48a9f6b38282604051808381526020018281526020019250505060405180910390a15050565b600160008083815260200190815260200160002054016000808381526020019081526020016000208190555050565b6000806000838152602001908152602001600020549050919050565b6001600080838152602001908152602001600020540360008083815260200190815260200160002081905550505600a165627a7a72305820db9e778e020441599ea5a4c88fbc38a17f36647f87712224f92815ad23c3d6a00029" }],
        "jsonrpc": "2.0",
        "id": 5,
    }
    response = requests.post(url, json=payload).json()

    print(response)



if __name__ == "__main__":
    main()