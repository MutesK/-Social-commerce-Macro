import json

class COption(object):
	def __init__ (self, option_json) :
		option_file = open(option_json, "r")
		self.json = json.load(option_file)

	def get_Userid(self) :
		return self.json["UserId"]

	def get_Userpass(self) :
		return self.json["Password"]

	def get_PurchaseSrc(self) :
		return self.json["PurchaseSrc"]

	def get_SocialCommerceType(self) :
		return self.json["CommerceName"]
