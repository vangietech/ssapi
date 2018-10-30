from sssdk import ShadowsocksSDK

ss = ShadowsocksSDK('127.0.0.1', 62000)
print(ss.ping())
print ss.add_user('9000', 'password')
print ss.remove_user('8381')

