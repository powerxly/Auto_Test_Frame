# # -*- coding: utf8 -*-
# import base64
# import hashlib
# import hmac
# import time
#
# import requests
#

import base64
import hashlib
import hmac
import time

import requests

#secret_id = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE"
#secret_key = "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE"
secret_id = "AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE"
secret_key = "Gu5t9xGARNpq86cd98joQYCN3EXAMPLE"
def get_string_to_sign(method, endpoint, params):
    s = method + endpoint + "/?"
    query_str = "&".join("%s=%s" % (k, params[k]) for k in sorted(params))
    return s + query_str

def sign_str(key, s, method):
    hmac_str = hmac.new(key.encode("utf8"), s.encode("utf8"), method).digest()
    return base64.b64encode(hmac_str)

if __name__ == '__main__':
    endpoint = "ocr.tencentcloudapi.com"
    data = {
        'Action' : 'EnglishOCR',
        'InstanceIds.0' : 'ins-09dx96dg',
        'Limit' : 20,
        'Nonce' : 11886,
        'Offset' : 0,
        'Region' : 'ap-beijing',
        'SecretId' : secret_id,
        'Timestamp' : int(time.time()), # int(time.time())
        'Version': '2018-11-19'
    }
    s = get_string_to_sign("GET", endpoint, data)
    data["Signature"] = sign_str(secret_key, s, hashlib.sha1)
    print(data["Signature"])
    # 此处会实际调用，成功后可能产生计费
    # resp = requests.get("https://" + endpoint, params=data)
    # print(resp.url)