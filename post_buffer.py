import requests
cid='53e728db62aca5c57ff21d11'
csec='2d21bf504042bfce2e8b65889e2b7790'
access_token='1/a1e7c460602310a498a8998d24775726'
from buffpy.models.update import Update
from buffpy.managers.profiles import Profiles
from buffpy.managers.updates import Updates
from buffpy.api import API
import json
def send_tweet(text,link,img_url):
    '''
    rdict={}
    rdict['client_id']=cid
    rdict['client_secret']=cid
    rdict['code']=access_token
    rdict['redirect_uri']='http://www.kwantm.com'
    rdict['grant_type']='authorization_code'
    resp=requests.post('https://api.bufferapp.com/1/oauth2/token.json',data=rdict)
    print resp
    
    rdict={'access_token':access_token}
    resp=requests.get('https://api.bufferapp.com/1/user.json',data=rdict)
    print resp.text
    print resp
    '''
    api = API(client_id=cid,
          client_secret=csec,
          access_token=access_token)
    #print api
    profiles = Profiles(api=api).all()
    profile_id=profiles[1].id
    #print profile_id
    media={}
    media['link']=link
    media['picture']=img_url

    updates=Updates(api,profile_id)
    updates.new(text=text,shorten=True,now=True,media=media)
    profile_id=profiles[1].id
    updates=Updates(api,profile_id)
    updates.new(text=text,shorten=True,now=True,media=media)
    
#send_tweet()

send_tweet('How Your Face Shapes Your Economic Chances ','http://www.theatlantic.com/business/archive/2014/08/the-economics-of-your-face/375450/','http://static.kwantm.com/imgs/20909014da03ffad2ba88b71eff60958')