from Corona_Tracker import CoronaTracker


Corona =CoronaTracker('Bangladesh')
Corona.loadData()
CountryInfo = Corona.countryInfo()
print(CountryInfo)
