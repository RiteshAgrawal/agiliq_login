from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
import urllib
import urllib2
import json
import requests
from form import Application 
client_id = 'yZuFGnC2azgd0zXm1YgZ2lRNkXUtDIMxV90UEqRSWbpEveCyG1'
client_secret = 'vonyUrjsyeToyfHbl0YtR7SWrDP3YxhpWnhXJuOcFixoutT1ZF' 
redirect_uri = 'http://127.0.0.1:8000/agiliq/'
auth_url = 'http://join.agiliq.com/oauth/authorize/'
access_url = 'http://join.agiliq.com/oauth/access_token/'


def agiliq(request):			
	code = request.GET.get('code','')
	access_token = request.GET.get('access_token','')
	state='application'
	if not code:							#This is for first when when authorizing the app 
		params = {'client_id':client_id,
			'redirect_uri':redirect_uri,
			'scope':'code',
			'state':'application'}
		return HttpResponseRedirect('%s?%s'%(auth_url,urllib.urlencode(params)))
	
	elif (not access_token and request.GET.get('state','')==state):	#This is for getting the access token after authorization
		params = {'client_id':client_id,
			'client_secret':client_secret,
			'code':code,
			'redirect_uri':redirect_uri}
		headers = {'Accept':'application/json','User-Agent': 'Mozilla/5.0',}
		respond = requests.post(access_url,data=params,headers=headers)
		access_token =  respond.json()['access_token']
		upload_url='http://join.agiliq.com/api/resume/upload/?access_token='+access_token
		a=Application()
		html = '<html><body>All the details are uploaded</body></html>'
		return render_to_response('submit.html',{'form':a,'url':upload_url})

			
	
