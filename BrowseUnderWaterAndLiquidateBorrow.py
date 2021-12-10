import requests
import json
from web3 import Web3



# function to use requests.post to make an API call to the subgraph url
def runQuery(query):

    # endpoint where you are making the request
    request = requests.post('https://api.thegraph.com/subgraphs/name/traderjoe-xyz/lending'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))

def liquidateBorrow(borrower,amount,collateral):
    # add avalanche fuji testnet
    web3 = Web3(Web3.HTTPProvider('https://api.avax-test.network/ext/bc/C/rpc'))

    # I am unable to deploy smart contract. therefore below values just for example. 
    liquidateBorrowSmartContract = ''
    liquidateBorrowSmartContractABI = ''

    #smart contract interaction starts with this value
    contract = web3.eth.contract(address=liquidateBorrowSmartContract, abi=liquidateBorrowSmartContractABI)
    contract.functions.liquidateBorrow(w3.toChecksumAddress(borrower),w3.toWei(amount, 'ether'),w3.toChecksumAddress(collateral))
      

def main():
    queryUnderWater = """

{
  accounts(where: {health_gt: 0, health_lt: 1, totalBorrowValueInUSD_gt: 0}) {
    id
    health
    totalBorrowValueInUSD
    totalCollateralValueInUSD
    tokens {
      id
    }
  }
  
}
"""
    resultUnderWater = runQuery(queryUnderWater)
    accounts = resultUnderWater['data']
    
    for account in accounts['accounts']:
        print('Account Address ' + account['id'])
        borrowList = []
        supplyList = []
        for token in account['tokens']:
            #print('Account Token ID ' + str(token['id']))
            tokenAddress = token['id'] . split('-')
            print('Token Address ' + tokenAddress[0])
            queryAccountJToken = '{accountJToken(id:"' +token['id']+ '"){enteredMarket borrowBalanceUnderlying  supplyBalanceUnderlying  symbol jTokenBalance }}'
            positionResult = runQuery(queryAccountJToken)
            #print(positionResult)
            if (float(positionResult['data']['accountJToken']['borrowBalanceUnderlying'])>0):
                borrowList.append(positionResult['data']['accountJToken'])
            if (float(positionResult['data']['accountJToken']['supplyBalanceUnderlying'])>0 and positionResult['data']['accountJToken']['enteredMarket'] is True):
                supplyList.append(positionResult['data']['accountJToken'])   
        print(*borrowList, sep = "\n")
        print(*supplyList, sep = "\n") 
        #call smart contract to liquidate borrow for every account    
        #liquidateBorrow( account['id'] , borrowlist[i]['data']['accountJToken']['borrowBalanceUnderlying'], borrowlist[i]['data']['accountJToken']['supplyBalanceUnderlying'] )    
if __name__ == "__main__":
    main()      