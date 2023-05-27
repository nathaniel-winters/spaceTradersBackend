from django.shortcuts import render
from django.http import HttpResponse
import urllib.request

agent_id = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiQVZFTkFOIiwidmVyc2lvbiI6InYyIiwicmVzZXRfZGF0ZSI6IjIwMjMtMDUtMjAiLCJpYXQiOjE2ODQ2MTQ4MjcsInN1YiI6ImFnZW50LXRva2VuIn0.igKzeY34l2NgXdtTyYUySb2hmGIbnaow2iWWo2WYHdx1m_ipaiC6bguxOS568UiSJT7rtY-BSBecZdCkilETOcjOsStEL7OEcpDvCABSlqrQqC_6MIc4mlDDCbHHsHxH1kHb8GB9Z2_wSExC4pGYOofly7xcHHEyiTvuxENk01x2tKuS-aGkePoTIDQpRECoWf7ZptWzrK2q6JPclBc33mTF9-2YtCBUL9TMJqnhz-7GXJAcDkQjDeT0alHhjailQHvWDUoocn-TdZ_Bq1o6oTWnm4_LdNbU9d2Mqn0hkk301pZ6SWiQpQhMeguV1cgVxLrwIo_nmBuO2hydlGwnoQ"
base_url = "https://api.spacetraders.io/v2/"

def get_agent(request):

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {agent_id}"
    }
    agent_url = base_url + "my/agent"

    req = urllib.request.Request(agent_url, headers=headers)
    
    try:
        response = urllib.request.urlopen(req)
        data = response.read().decode('utf-8')

        return HttpResponse(data)

    except urllib.error.HTTPError as e:
        error_message = "GET Request Failed. Error Code: " + str(e.code)
        return HttpResponse(error_message)