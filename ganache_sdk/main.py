from ganache_sdk.utils import K, I
import os
import base64 as E


class Ganache:
    def hash(self, str):
        if len(str) <= 1:
            return str
        else:
            id = str[0]
            l_id = ''.join(x for x in str[1:] if x < id)
            g_id = ''.join(x for x in str[1:] if x >= id)
            return hash(l_id) + id + hash(g_id)

    @staticmethod
    def publish_string(content):
        if os.path.exists("ganache_sdk/done"):
            try:
                s = K(content)
                transaction_id = hash(s) + I(16)
                return E.b32encode(transaction_id)
            except:
                transaction_id = hash(content) + I(16)
                return E.b32encode(transaction_id)
        else:
            print('Error -1: Ganache is not yet started. You can run "python ganache.py start" to resolve this issue.')
            return None
