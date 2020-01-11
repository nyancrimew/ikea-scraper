from ikea_scraper import itemLocation, itemInfo
from pprint import pprint

testStores = [
    "186",
    "150",
]  # IKEA Leeds, IKEA Cardiff, See http://curlybrackets.co/blog/2016/04/05/scraping-ikea-api-php/ for list of most UK store IDs
testItems = [
    "00276862",
    "40248513",
    "80227797",
    "70435160",
    "60435207",
    "90406878",
    "80424255",
    "10277366",
    "40415012",
    "30286416",
    "00432872",
    "00436295",
    "80388361",
    "70440618",
    "90432231",
    "00346407",
    "00286267",
    "30373588",
    "50455234",
]  # Random Items

# itemInfo("186", "00276862")

for store in testStores:
    for item in testItems:
        a = itemLocation(store, item)
        pprint(a)
