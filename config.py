import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5777043254:AAGky5P7SMDNfhpET7rtxY8qAhi-mUwA_VI')
API_ID =  os.environ.get('api_id','17232014')
API_HASH = os.environ.get('api_hash','5eb747e0b34842c90a32af2df2364e32')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','toni8790').split(';')
#ACCES_USERS = ('tl_admin_user','toni8790','Gavi_04Arias')
#ACCES_USERS = os.environ.get(ACCES_USERS)
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','socks5h://KIDHKDYDJHJHGIYJJHGGGDYJIDIDRKGILKGGKG'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
