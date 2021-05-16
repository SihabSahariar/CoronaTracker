'''
Programmer - Sihab Sahariar 
Website : https://sihabsahariar.github.io/
Corona Tracker is an opensource python library to get information of a particular country about Corona Virus.
Using webscrapping technology I implemented it to use in various project. There are 24 methods to get information.
The methods are listed here -
-updated
-country 
-countryInfo 
-cases 
-todayCases 
-deaths 
-todayDeaths 
-recovered 
-todayRecovered
-active 
-critical 
-casesPerOneMillion 
-deathsPerOneMillion 
-tests 
-testsPerOneMillion 
-population 
-continent 
-oneCasePerPeople 
-oneDeathPerPeople 
-oneTestPerPeople 
-undefined 
-activePerOneMillion 
-recoveredPerOneMillion 
-criticalPerOneMillion 
'''

from urllib.request import Request, urlopen
import json
class CoronaTracker:
	def __init__(self,countryName):
		self.loadedSuccessfully = False 
		self.data_json = None
		if countryName == "":
			return None
		else:
			self.countryName= countryName
	def loadData(self):
		try:
			req = Request('https://corona.lmao.ninja/v2/countries/'+self.countryName, headers={'User-Agent': 'Mozilla/5.0'})
			webpage = urlopen(req).read()
			self.data_json = json.loads(webpage)
			self.loadedSuccessfully = True
		except:
			None 

	def errorMessage(self):
		return ('Check Internet Connection and loadData function call')
	def updated(self):
		return self.data_json['updated'] if self.loadedSuccessfully ==True else self.errorMessage()
	def country(self):
		return self.data_json['country'] if self.loadedSuccessfully ==True else self.errorMessage()
	def countryInfo (self):
		return self.data_json['countryInfo'] if self.loadedSuccessfully ==True else self.errorMessage()	
	def cases (self):
		return self.data_json['cases'] if self.loadedSuccessfully ==True else self.errorMessage()
	def todayCases(self):
		return self.data_json['todayCases'] if self.loadedSuccessfully ==True else self.errorMessage()
	def deaths(self):
		return self.data_json['deaths'] if self.loadedSuccessfully ==True else self.errorMessage()
	def todayDeaths(self):
		return self.data_json['todayDeaths'] if self.loadedSuccessfully ==True else self.errorMessage()
	def recovered (self):
		return self.data_json['recovered'] if self.loadedSuccessfully ==True else self.errorMessage()
	def todayRecovered(self):
		return self.data_json['todayRecovered'] if self.loadedSuccessfully ==True else self.errorMessage()
	def active(self):
		return self.data_json['active'] if self.loadedSuccessfully ==True else self.errorMessage()
	def critical(self):
		return self.data_json['critical'] if self.loadedSuccessfully ==True else self.errorMessage()
	def casesPerOneMillion(self):
		return self.data_json['casesPerOneMillion'] if self.loadedSuccessfully ==True else self.errorMessage()
	def deathsPerOneMillion(self):
		return self.data_json['deathsPerOneMillion'] if self.loadedSuccessfully ==True else self.errorMessage()
	def tests(self):
		return self.data_json['tests'] if self.loadedSuccessfully ==True else self.errorMessage()
	def testsPerOneMillion(self):
		return self.data_json['testsPerOneMillion'] if self.loadedSuccessfully ==True else self.errorMessage()
	def population(self):
		return self.data_json['population'] if self.loadedSuccessfully ==True else self.errorMessage()
	def continent(self):
		return self.data_json['continent'] if self.loadedSuccessfully ==True else self.errorMessage()
	def oneCasePerPeople(self):
		return self.data_json['oneCasePerPeople'] if self.loadedSuccessfully ==True else self.errorMessage()
	def oneDeathPerPeople(self):
		return self.data_json['oneDeathPerPeople'] if self.loadedSuccessfully ==True else self.errorMessage()
	def oneTestPerPeople (self):
		return self.data_json['oneTestPerPeople'] if self.loadedSuccessfully ==True else self.errorMessage()
	def undefined(self):
		return self.data_json['undefined'] if self.loadedSuccessfully ==True else self.errorMessage()
	def activePerOneMillion(self):
		return self.data_json['activePerOneMillion'] if self.loadedSuccessfully ==True else self.errorMessage()
	def recoveredPerOneMillion(self):
		return self.data_json['recoveredPerOneMillion'] if self.loadedSuccessfully ==True else self.errorMessage()
	def criticalPerOneMillion(self):
		return self.data_json['criticalPerOneMillion'] if self.loadedSuccessfully ==True else self.errorMessage()

