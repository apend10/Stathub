import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd

#Step1: create a variable called headers to tell the website that we are a browser and not a scraping tool
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

#Step 2: assigns the address of the page we need to scrape to a string
default = "https://www.transfermarkt.us/arsenal-fc/kadernaechstesaison/verein/11/plus/0/galerie/0?anschluss=1"
page = input("Enter a URL: ")
if(page == "" or page == " "):
    page = default

try:
    #Step 3: uses the requests library to grab the code of a page and assign it to 'PageTree'
    pageTree = requests.get(page, headers=headers)

    #Step 4: parses the website code into html and we will be able to search through this for the data we want to extract
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    #Step 5: Extracting player names
    Players = pageSoup.find_all("td", {"class" : "hauptlink"})

    #Step 6: values are not a link, they are a player in a cell so we need to find a new feature to identify them by
    Transfer_Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})
    Positions = pageSoup.find_all("table", {"class": "inline-table"})
    #have to do this to get just the position: Positions[0].text[len(Players[0].text):]


    #create clean lists
    arrPlayers = []
    counter = 0
    for i in range(len(Players)):
        if(i % 2 == 0):
            counter += 1
            arrPlayers.append(Players[i].text)
            if(counter == len(Transfer_Values)):
                break

    arrValues = []
    for i in range(len(Transfer_Values)):
        arrValues.append(Transfer_Values[i].text[0:len(Transfer_Values[i].text)-1])

    arrPositions = []
    for i in range(len(Positions)):
        arrPositions.append(Positions[i].text[len(arrPlayers[i]):])




    #table using tabulate
    big_table = {'Name ' : arrPlayers, 'Position ': arrPositions, 'Market Value' : arrValues}
    print(tabulate(big_table, headers = 'keys', tablefmt='fancy_grid'))

    #INCOMPLETE: CREATING DATAFRAME
    # DataFrame creation
    # Players List = arrNames
    # Values List = arrValues
    # Positions List = arrPositions


    #df = pd.DataFrame({"Players": arrPlayers, "Values": arrValues, "Positions": arrPositions})

    #Writing the lists[arrPlayers, arrValues, arrPositions, arrNumbers] into a text file
    textfile = open("arsenalWindowTransfermarkt.txt", "w")
    for element in arrPlayers:
        textfile.write(element + " ")
    textfile.write("\n")

    for element in arrValues:
        textfile.write(element + " ")
    textfile.write("\n")

    for element in arrPositions:
        textfile.write(element + " ")
    textfile.write("\n")

    textfile.close()
except:
    print("Improper URL entered!")