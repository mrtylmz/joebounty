1)Install python and pip3
2)pip3 install web3   #web3 library for python
3)py BrowseUnderWaterAndLiquidateBorrow.py

Python code browse under water accounts  and retrieves all subgraph informations on trader joe dex.
After getting those values we should call liquidateBorrow method. But this wasn't succesfully implemented due to smart contract deploy problem. (deployment-error.png)
I shared smart contract class on this repo as well (see JWrappedNative.sol) You are able to compile with Remix but Remix could not deploy the class. 
