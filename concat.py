import os
import re

import sys


class Contract:
    name = ""
    parents = []
    text = """"""

    def __init__(self, name, text, parents):
        self.name = name
        self.text = text
        self.parent = parents

    def __str__(self):
        return self.text

    @staticmethod
    def parse(text):
        res = re.search("contract ([a-zA-Z0-9]+)", text)
        if not res:
            return
        name = res.group(1)
        return Contract(name, text, [])

if __name__ == '__main__':
    if sys.argv:
        contracts = dict()
        for subdir, dir, files in os.walk(sys.argv[1]):
            concat_name = "../Gid.sol"
            for file_name in files:
                with open(subdir + file_name) as file:
                    text = file.read()
                    text = text.replace("pragma solidity ^0.4.4;\n", "")
                    text = re.sub("import.*\n", "", text)
                    contract = Contract.parse(text)
                    if contract:
                        contracts[contract.name] = contract
                    else:
                        contracts['Structures'] = Contract('Structures', text, [])

            with open(subdir + concat_name, 'w') as concat:
                concat.write("pragma solidity ^0.4.4;\n")
                concat.write(contracts['Structures'].text)
                concat.write(contracts['ERC20'].text)
                concat.write(contracts['Master'].text)
                concat.write(contracts['GidCoin'].text)
                concat.write(contracts['CrowdFunding'].text)
                concat.write(contracts['MigrationMaster'].text)
                concat.write(contracts['Administrator'].text)
                concat.write(contracts['Verifier'].text)
                concat.write(contracts['Person'].text)
                concat.write(contracts['Document'].text)
                concat.write(contracts['Gid'].text)

