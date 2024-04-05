import json

from enkanetwork.model.base import EnkaNetworkResponse

UID = "843715177"

with open(f"./{UID}.json" , "r", encoding="utf-8") as f:
    response = EnkaNetworkResponse.model_validate(json.load(f))
    print(response)