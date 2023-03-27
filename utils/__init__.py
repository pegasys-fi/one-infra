# -*- coding: utf-8 -*-
from pone_infra.utils.json_loader import JsonLoader
from pone_infra.utils.APIStatus import CommonStatus

# usage: abiJsonLoader.get('apps.XYZ.erc.erc20.json') locate to path apps/XYZ/data/abi/erc/erc20.json
abiJsonLoader = JsonLoader().getConst(['pone_infra/blockchain/data/abi/', 'apps/*/data/abi/'], 'data/abi/')

__all__ = ['APIResponse', 'CommonStatus', 'abiJsonConst']
