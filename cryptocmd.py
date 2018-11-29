from cryptocmd import CmcScraper

# initialise scraper
scraper = CmcScraper('XRP', '01-01-2015', '30-10-2018')

# get data as list of list
headers, data = scraper.get_data()

# export the data to csv
scraper.export_csv()

# get dataframe for the data
df = scraper.get_dataframe()