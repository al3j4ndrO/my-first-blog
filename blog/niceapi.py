# Python 3
import http.client

yourId = "mH5rXGP2ykuXUuHtxj1YaWFsam5kcm9fZG90X29fZG90X2dfYXRfZ21haWxfZG90X2NvbQ=="
yourMobile = "+50361000171"
yourMessage = "Alguien quiere accesar"

user_enter = ""
pass_enter = ""

if user_enter and pass_enter != "":
	c = http.client.HTTPSConnection("NiceApi.net")
	c.request("POST", "/API", yourMessage, {"X-APIId": yourId, "X-APIMobile": yourMobile})
	response = c.getresponse()
	data = response.read()
	print (data)