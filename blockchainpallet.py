import json
import re
import urllib.request

print("start")


""" get block height """
req = urllib.request.Request('https://blockchain.info/ja/q/getblockcount')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   

target_bloack_height = str(the_page.decode(encoding='utf-8'))



url = "https://blockchain.info/ja/block-height/" + target_bloack_height + "?format=json"

print(url)
req2 = urllib.request.Request(url)
with urllib.request.urlopen(req2) as response2:
   the_page2 = response2.read()

   
"""
print(the_page2.decode(encoding='utf-8'))
"""

r1 = re.compile(r'"hash":"[a-zA-Z0-9]+"')
hash_code = r1.search(the_page2.decode(encoding='utf-8'))
print(hash_code.group(0))

r2 = re.compile(r'[a-zA-Z0-9]{64}')
hash_value = r2.search(hash_code.group(0))
print(hash_value.group(0))





print("end")	
