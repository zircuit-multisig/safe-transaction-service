import json

import requests
from eth_abi import encode_single, encode_abi, decode_single
from gnosis.eth import EthereumClient
import time

from gnosis.eth.multicall import Multicall
from hexbytes import HexBytes

node_url = 'https://staging-openethereum.mainnet.gnosisdev.com/'
ethereum_client = EthereumClient(node_url)
safe_address = '0xE41d2489571d322189246DaFA5ebDe1F4699F498'

token_addresses = [
    '0xE41d2489571d322189246DaFA5ebDe1F4699F498',
    '0x08130635368AA28b217a4dfb68E1bF8dC525621C',
    '0x9c5c3395B9B791d2Edd472592045fB341E115c3b',
    '0x4DC3643DbC642b72C158E7F3d2ff232df61cb6CE',
    '0x1985365e9f78359a9B6AD760e32412f4a445E862',
    '0xe71cEbd38cE2186E01eb6c8a232eC16E8906Ed69',
    '0x1C3BB10dE15C31D5DBE48fbB7B87735d1B7d8c32',
    '0x5732046A883704404F284Ce41FfADd5b007FD668',
    '0x5C406D99E04B8494dc253FCc52943Ef82bcA7D75',
    '0x0F5D2fB29fb7d3CFeE444a200298f468908cC942',
    '0x0AbdAce70D3790235af448C88547603b945604ea',
    '0xBDDab785b306BCD9fB056Da189615Cc8eCE1D823',
    '0x2F141Ce366a2462f02cEA3D12CF93E4DCa49e4Fd',
    '0x419D0d8BdD9aF5e606Ae2232ed285Aff190E711b',
    '0x6810e776880C02933D47DB1b9fc05908e5386b96',
    '0x12B19D3e2ccc14Da04FAe33e63652ce469b3F2FD',
    '0x6c6EE5e31d828De241282B9606C8e98Ea48526E2',
    '0x2630997aAB62fA1030a8b975e1AA2dC573b18a13',
    '0x0f8b6440A1F7BE3354fe072638a5C0F500b044bE',
    '0xC12D1c73eE7DC3615BA4e37E4ABFdbDDFA38907E',
    '0x514910771AF9Ca656af840dff83E8264EcF986CA',
    '0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84',
    '0xA4e8C3Ec456107eA67d3075bF9e3DF3A75823DB0',
    '0xBBbbCA6A901c926F240b89EacB641d8Aec7AEafD',
    '0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2',
    '0xd084944d3c05CD115C09d072B9F44bA3E0E45921',
    '0xe2f2a5C287993345a840Db3B0845fbC70f5935a5',
    '0xE1Ac9Eb7cDDAbfd9e5CA49c23bd521aFcDF8BE49',
    '0x1A5F9352Af8aF974bFC03399e3767DF6370d82e4',
    '0x8E870D67F660D95d5be530380D0eC0bd388289E1',
    '0x70F823ed7643Fd7A26FDf8753827d31C16374FDE',
    '0x9992eC3cF6A55b00978cdDF2b27BC6882d88D1eC',
    '0x255Aa6DF07540Cb5d3d297f0D0D4D84cb52bc8e6',
    '0x53Ad8c733a4338e2B8C235ECfDbed0Ef8f79C7Bd',
    '0x5807CA447851C98569c567963B25B1C83D41BeBc',
    '0xfC89f1b932079b462Ef9C8757dE5A28E387b847b',
    '0x22CaBb38295eaeccFedE4e99AF508052e3B74cA0',
    '0x395C47a421C254AE42253764A7f56e0Ee0CDDac5',
    '0x74d2cb65B1158300c3e6BeA149d68509C7B2425d',
    '0xE9eace1313913888C364D8504ffC3b8d991C67C6',
    '0x6Fd016CCc4611F7BAB1DD3267334cB0216Ef47f9',
    '0xa9E8A9d9729e766A72763253f2aFd1b1cF9053a0',
    '0x43688910273f199B8AE2cA018c13918fb3D37B58',
    '0x22C8ECF727C23422f47093b562EC53c139805301',
    '0xE5f7ef61443Fc36AE040650aa585B0395AEf77c8',
    '0xeD42CeDcADbFbCAA3E6F411B09567C2C0b5AD28F',
    '0xDbb13D3f745A64995CA76069F2cebF9a2d7B18c0',
    '0xac1682ad8893eD96E7ec3379f3a212Dc50f06d23',
    '0xC4CB613947890EA300FEDc509AC19f8efa0cDd14',
    '0xd4203d4F0f2c3aE21ce93f04aB00517262f65aa9',
    '0x53993d04758Ee89BBE190E15A81C411688543AbA',
    '0x94Fa7F8cb8453AD57cd133363b3012044647078C',
    '0x434E3a92C43a98fF508ab44E023ea7638952Ad21',
    '0xba0d050BBB662c190Bf99C61708B42Ff9d8750e0',
    '0x6F442Da588232DC57Bf0096E8dE48D6961D5CC83',
    '0x4475Ad655d6FA73Db81CC52a5Cf4585fAa34A1Dd',
    '0x315699f1BA88383CFF2F2f30FcaD187aDb2E4D72',
    '0x41599149f1B52035392402F9e311b1edb0C9f699',
    '0x7E95b310724334FF74537dc08bfD3377d25E65Ce',
    '0x9FEF44FC4C571010BCCD5b63e1Cdc807D3b347bF',
    '0xFe17C3C0B6F38cF3bD8bA872bEE7a18Ab16b43fB',
    '0x1105c20aC6F4DE989fAF05d17ab3f950963B75Ad',
    '0x438f9De51f51692A4B83696413062a040cC5cBD5',
    '0xB3D3C1bBcEf737204AADb4fA6D90e974bc262197',
    '0x499A6c19F5537dd6005E2B5c6E1263103f558Ba4',
    '0x9856C5CA15A4Ac9C65AAC090c38a9f39EB3b5eeC',
    '0xbfF3a3d79d0f9165CFcC1B369eE41f3C5C9Ae398',
    '0x9A99f283e1F6c3b7F24901995624Ef7b78E94471',
    '0x75f06B482adbFb04b877D8ee683E2FCDf18AD153',
    '0x4Cc53Ee5ef306a95d407321d4B4acc30814C04ee',
    '0x830B0e9a5ecf36D0A886D21e1C20043cD2d16515',
    '0x8a9F904B4EaD6a97F3aB304d0D2196f5c602c807',
    '0x419f97e6dcfBf89A70EA898b7F44472F75bF6137',
    '0xd9e89bFebAe447B42C1Fa85C590716eC8820f737',
    '0xee9a08Fc54bF53353398f946db4Cb2447276f850',
    '0x96700Ffae33c651bC329c3f3fbFE56e1f291f117',
    '0xeFe82D6baF0dB71f92889eB9d00721bD49121316',
    '0x8a41B6b6177f35Bfa6D677447D3Fe0d5a0ceC45E',
    '0x2830209f6573F10c481D946Ba18B446429F30360',
    '0xec069EaA5c83763F288106506FeCBd5dBE74d047',
    '0x73BdE888664DF8DDfD156B52e6999EEaBAB57C94',
    '0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359',
    '0x5e74C9036fb86BD7eCdcb084a0673EFc32eA31cb',
    '0x1Fc31488f28ac846588FFA201cDe0669168471bD',
    '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984',
    '0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599'
]

balance_of_data = HexBytes('0x70a08231' + '{:0>64}'.format(safe_address.replace('0x', '').lower()))

start = time.time()
queries = [
    {'jsonrpc': '2.0',
     'method': 'eth_call',
     'params': [{'to': erc20_address,
                 'data': balance_of_data.hex(),
                 }, 'latest'],
     'id': i + 1} for i, erc20_address in enumerate(token_addresses)]
response = requests.post(ethereum_client.ethereum_node_url, json=queries).json()
ethereum_client.erc20.get_balances(safe_address, token_addresses)
print(f'Batch Call {time.time() - start:.4f} seconds elapsed')

# Test multicall
data = encode_single('(address,bytes)[]', [[token_addresses[1], balance_of_data]])

print(
    decode_single(
        'int',
        ethereum_client.w3.eth.call({
            'to': token_addresses[0],
            'data': balance_of_data
        })
    )
)

multicall = Multicall(ethereum_client)
aggregate_parameters = [(token, balance_of_data) for token in token_addresses]

start = time.time()
blocknumber, result = multicall.aggregate(aggregate_parameters)
print(f'Multicall {time.time() - start:.4f} seconds elapsed')

start = time.time()
results = multicall.try_aggregate(aggregate_parameters)
print(f'Multicall try {time.time() - start:.4f} seconds elapsed')
