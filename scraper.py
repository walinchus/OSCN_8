# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
#sudo service morph restart
import scraperwiki
import lxml
import urlparse
import urllib2
#import mechanize
import requests
import lxml.html
import sqlite3
import time

#counties = ['adair','alfalfa','appellate','atoka','beaver','beckham','blaine','bryan','caddo','canadian','carter','cherokee','choctaw','cimarron','cleveland','coal','comanche','cotton','craig','creek','bristow','drumright','custer','delaware','dewey','ellis','garfield','garvin','grady','grant','greer','harmon','harper','haskell','hughes','jackson','jefferson','johnston','kay','poncacity','kingfisher','kiowa','latimer','leflore','lincoln','logan','love','major','marshall','mayes','mcclain','mccurtain','mcintosh','murray','muskogee','noble','nowata','okfuskee','oklahoma','okmulgee','henryetta','osage','ottawa','payne','pawnee','pittsburg','pontotoc','pottawatomie','pushmataha','rogermills','rogers','seminole','sequoyah','stephens','texas','tillman','tulsa','wagoner','washington','washita','woods','woodward']
counties = ['oklahoma']
#next_link = 0
years = ['2011','2012','2013','2014','2015','2016','2017']
CrimeSeverity = ['CF','CM']

def CaseEndingNumbers():
    for x in range(1, 2):
        yield '%d' % x
        

def GetOklahomaStateCases():
    for county in counties:
        for CaseEndingNumber in ListOfCaseEndingNumbers:
            for year in years:
                for severity in CrimeSeverity:
                    yield 'http://www.oscn.net/dockets/GetCaseInformation.aspx?db=%s&number=%s-%s-%s' % (county, severity, year, CaseEndingNumber)

def scrape_table(root):
    #create a record to hold the data
    record = {}
    #grab all table rows <tr> in table class="tblSearchResults"
    rows = root.cssselect("table.caseStyle tr")
    #for each row, loop through this
    for row in rows:
        #create a list of all cells <td> in that row
        table_cells = row.cssselect("td")
        if table_cells: 
        #if there is a cell, record the contents in our dataset, the first cell [0] in 'recipient' and so on
            Case_Style = table_cells[0].text_content()
            #print Case_Style
            record['Case Style'] = table_cells[0].text_content()
            record['Date Filed and Judge'] = table_cells[1].text_content()
            record['URL'] = table_cellsurls[0].attrib.get('href')
            #record['Case Number'] = table_cells[0].strong.text_content()
            #this line adds 1 to the ID no. we set at 0 earlier
            #idno=idno+1
            #record['ID'] = idno 
            print record, '------------'
        counts = root.cssselect("div.CountsContainer")
        countstotal = len(counts)
        print "total number of counts:", countstotal
        #countsrange = range(0, countstotal+1)
        #for count in countsrange:
        id=0
        for count in counts:
            id+=1
            if counts: 
                record['Count'+str(id)] = count.text_content()
            '''rows = count.cssselect('div.CountsContainer tr')
            if rows:
                id = 0
                #rowstotal = len(rows)
                #rowsrange = range(0,rowstotal+1)
                #create a record to hold the data
                #record = {}
                #for each row, loop through this
                #for rownum in rowsrange:
                for row in rows:
                    id + 1 
                    record["'Count'+str(id)"] = row[1].text_content()
                    #record['Count'+str(id)+'as disposed:'] = row[2].text_content()
                    #print "scraping row", rownum
                    #create a list of all cells <td> in that row
                    table_cells = row.cssselect("td")
                    if table_cells:
                    #print table_cells
                        record['Charges'] = table_cells[0].text_content()
                        record['Count Description:'] = table_cells[1].text_content()
                        record['Outcome:'] = table_cells[-1].text_content()
                        print record, '------------'
                        # Save the record to the datastore - 'ID' is our unique key - '''
    print 'ALL DATA:', record
    scraperwiki.sqlite.save(unique_keys=['Date Filed and Judge'], data=record)
           
            

def scrape_and_look_for_next_link(url):
    #html = scraperwiki.scrape(url)
    headers = { 'User-Agent' : 'Lucia Walinchus, Lucia@ProfessionalNewsServices.com, 646-397-7761' }
    req = urllib2.Request(url, None, headers)
    html = urllib2.urlopen(req).read()
    #page = requests.get(url)
    #html = page.content
    print html
    root = lxml.html.fromstring(html)
    scrape_table(root)
    #CaseEndingNumber += 1
    global i
    i = (i + 1)
    if i < 450:
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if i == 451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 451 < i < 901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 901 < i < 1351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 1351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 1351 < i < 1801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 1801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 1801 < i < 2251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 2251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 2251 < i < 2701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 2701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 2701 < i < 3151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 3151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 3151 < i < 3601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 3601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 3601 < i < 4051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 4051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 4051 < i < 4501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 4501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 4501 < i < 4951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 4951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 4951 < i < 5401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 5401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 5401 < i < 5851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 5851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 5851 < i < 6301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 6301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 6301 < i < 6751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 6751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 6751 < i < 7201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 7201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 7201 < i < 7651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 7651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 7651 < i < 8101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 8101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 8101 < i < 8551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 8551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 8551 < i < 9001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 9001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 9001 < i < 9451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 9451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 9451 < i < 9901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 9901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 9901 < i < 10351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 10351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 10351 < i < 10801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 10801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 10801 < i < 11251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 11251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 11251 < i < 11701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 11701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 11701 < i < 12151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 12151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 12151 < i < 12601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 12601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 12601 < i < 13051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 13051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 13051 < i < 13501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 13501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 13501 < i < 13951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 13951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 13951 < i < 14401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 14401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 14401 < i < 14851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 14851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 14851 < i < 15301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 15301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 15301 < i < 15751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 15751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 15751 < i < 16201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 16201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 16201 < i < 16651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 16651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 16651 < i < 17101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 17101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 17101 < i < 17551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 17551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 17551 < i < 18001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 18001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 18001 < i < 18451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 18451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 18451 < i < 18901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 18901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 18901 < i < 19351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 19351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 19351 < i < 19801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 19801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 19801 < i < 20251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 20251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 20251 < i < 20701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 20701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 20701 < i < 21151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 21151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 21151 < i < 21601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 21601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 21601 < i < 22051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 22051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 22051 < i < 22501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 22501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 22501 < i < 22951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 22951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 22951 < i < 23401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 23401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 23401 < i < 23851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 23851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 23851 < i < 24301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 24301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 24301 < i < 24751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 24751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 24751 < i < 25201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 25201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 25201 < i < 25651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 25651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 25651 < i < 26101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 26101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 26101 < i < 26551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 26551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 26551 < i < 27001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 27001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 27001 < i < 27451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 27451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 27451 < i < 27901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 27901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 27901 < i < 28351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 28351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 28351 < i < 28801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 28801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 28801 < i < 29251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 29251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 29251 < i < 29701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 29701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 29701 < i < 30151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 30151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 30151 < i < 30601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 30601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 30601 < i < 31051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 31051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 31051 < i < 31501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 31501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 31501 < i < 31951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 31951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 31951 < i < 32401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 32401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 32401 < i < 32851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 32851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 32851 < i < 33301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 33301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 33301 < i < 33751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 33751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 33751 < i < 34201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 34201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 34201 < i < 34651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 34651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 34651 < i < 35101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 35101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 35101 < i < 35551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 35551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 35551 < i < 36001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 36001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 36001 < i < 36451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 36451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 36451 < i < 36901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 36901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 36901 < i < 37351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 37351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 37351 < i < 37801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 37801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 37801 < i < 38251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 38251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 38251 < i < 38701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 38701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 38701 < i < 39151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 39151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 39151 < i < 39601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 39601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 39601 < i < 40051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 40051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 40051 < i < 40501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 40501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 40501 < i < 40951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 40951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 40951 < i < 41401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 41401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 41401 < i < 41851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 41851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 41851 < i < 42301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 42301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 42301 < i < 42751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 42751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 42751 < i < 43201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 43201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 43201 < i < 43651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 43651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 43651 < i < 44101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 44101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 44101 < i < 44551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 44551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 44551 < i < 45001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 45001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 45001 < i < 45451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 45451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 45451 < i < 45901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 45901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 45901 < i < 46351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 46351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 46351 < i < 46801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 46801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 46801 < i < 47251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 47251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 47251 < i < 47701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 47701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 47701 < i < 48151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 48151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 48151 < i < 48601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 48601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 48601 < i < 49051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 49051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 49051 < i < 49501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 49501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 49501 < i < 49951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 49951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 49951 < i < 50401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 50401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 50401 < i < 50851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 50851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 50851 < i < 51301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 51301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 51301 < i < 51751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 51751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 51751 < i < 52201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 52201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 52201 < i < 52651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 52651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 52651 < i < 53101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 53101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 53101 < i < 53551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 53551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 53551 < i < 54001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 54001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 54001 < i < 54451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 54451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 54451 < i < 54901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 54901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 54901 < i < 55351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 55351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 55351 < i < 55801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 55801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 55801 < i < 56251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 56251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 56251 < i < 56701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 56701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 56701 < i < 57151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 57151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 57151 < i < 57601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 57601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 57601 < i < 58051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 58051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 58051 < i < 58501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 58501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 58501 < i < 58951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 58951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 58951 < i < 59401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 59401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 59401 < i < 59851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 59851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 59851 < i < 60301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 60301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 60301 < i < 60751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 60751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 60751 < i < 61201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 61201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 61201 < i < 61651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 61651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 61651 < i < 62101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 62101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 62101 < i < 62551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 62551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 62551 < i < 63001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 63001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 63001 < i < 63451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 63451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 63451 < i < 63901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 63901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 63901 < i < 64351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 64351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 64351 < i < 64801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 64801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 64801 < i < 65251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 65251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 65251 < i < 65701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 65701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 65701 < i < 66151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 66151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 66151 < i < 66601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 66601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 66601 < i < 67051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 67051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 67051 < i < 67501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 67501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 67501 < i < 67951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 67951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 67951 < i < 68401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 68401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 68401 < i < 68851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 68851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 68851 < i < 69301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 69301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 69301 < i < 69751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 69751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 69751 < i < 70201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 70201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 70201 < i < 70651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 70651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 70651 < i < 71101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 71101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 71101 < i < 71551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 71551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 71551 < i < 72001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 72001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 72001 < i < 72451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 72451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 72451 < i < 72901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 72901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 72901 < i < 73351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 73351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 73351 < i < 73801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 73801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 73801 < i < 74251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 74251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 74251 < i < 74701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 74701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 74701 < i < 75151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 75151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 75151 < i < 75601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 75601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 75601 < i < 76051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 76051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 76051 < i < 76501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 76501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 76501 < i < 76951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 76951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 76951 < i < 77401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 77401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 77401 < i < 77851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 77851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 77851 < i < 78301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 78301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 78301 < i < 78751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 78751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 78751 < i < 79201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 79201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 79201 < i < 79651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 79651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 79651 < i < 80101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 80101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 80101 < i < 80551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 80551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 80551 < i < 81001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 81001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 81001 < i < 81451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 81451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 81451 < i < 81901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 81901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 81901 < i < 82351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 82351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 82351 < i < 82801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 82801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 82801 < i < 83251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 83251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 83251 < i < 83701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 83701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 83701 < i < 84151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 84151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 84151 < i < 84601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 84601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 84601 < i < 85051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 85051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 85051 < i < 85501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 85501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 85501 < i < 85951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 85951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 85951 < i < 86401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 86401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 86401 < i < 86851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 86851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 86851 < i < 87301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 87301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 87301 < i < 87751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 87751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 87751 < i < 88201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 88201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 88201 < i < 88651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 88651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 88651 < i < 89101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 89101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 89101 < i < 89551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 89551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 89551 < i < 90001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 90001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 90001 < i < 90451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 90451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 90451 < i < 90901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 90901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 90901 < i < 91351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 91351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 91351 < i < 91801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 91801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 91801 < i < 92251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 92251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 92251 < i < 92701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 92701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 92701 < i < 93151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 93151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 93151 < i < 93601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 93601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 93601 < i < 94051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 94051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 94051 < i < 94501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 94501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 94501 < i < 94951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 94951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 94951 < i < 95401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 95401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 95401 < i < 95851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 95851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 95851 < i < 96301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 96301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 96301 < i < 96751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 96751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 96751 < i < 97201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 97201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 97201 < i < 97651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 97651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 97651 < i < 98101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 98101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 98101 < i < 98551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 98551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 98551 < i < 99001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 99001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 99001 < i < 99451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 99451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 99451 < i < 99901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 99901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 99901 < i < 100351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 100351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 100351 < i < 100801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 100801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 100801 < i < 101251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 101251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 101251 < i < 101701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 101701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 101701 < i < 102151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 102151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 102151 < i < 102601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 102601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 102601 < i < 103051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 103051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 103051 < i < 103501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 103501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 103501 < i < 103951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 103951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 103951 < i < 104401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 104401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 104401 < i < 104851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 104851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 104851 < i < 105301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 105301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 105301 < i < 105751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 105751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 105751 < i < 106201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 106201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 106201 < i < 106651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 106651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 106651 < i < 107101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 107101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 107101 < i < 107551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 107551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 107551 < i < 108001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 108001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 108001 < i < 108451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 108451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 108451 < i < 108901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 108901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 108901 < i < 109351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 109351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 109351 < i < 109801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 109801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 109801 < i < 110251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 110251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 110251 < i < 110701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 110701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 110701 < i < 111151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 111151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 111151 < i < 111601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 111601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 111601 < i < 112051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 112051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 112051 < i < 112501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 112501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 112501 < i < 112951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 112951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 112951 < i < 113401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 113401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 113401 < i < 113851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 113851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 113851 < i < 114301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 114301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 114301 < i < 114751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 114751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 114751 < i < 115201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 115201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 115201 < i < 115651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 115651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 115651 < i < 116101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 116101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 116101 < i < 116551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 116551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 116551 < i < 117001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 117001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 117001 < i < 117451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 117451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 117451 < i < 117901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 117901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 117901 < i < 118351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 118351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 118351 < i < 118801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 118801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 118801 < i < 119251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 119251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 119251 < i < 119701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 119701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 119701 < i < 120151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 120151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 120151 < i < 120601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 120601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 120601 < i < 121051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 121051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 121051 < i < 121501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 121501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 121501 < i < 121951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 121951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 121951 < i < 122401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 122401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 122401 < i < 122851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 122851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 122851 < i < 123301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 123301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 123301 < i < 123751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 123751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 123751 < i < 124201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 124201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 124201 < i < 124651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 124651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 124651 < i < 125101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 125101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 125101 < i < 125551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 125551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 125551 < i < 126001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 126001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 126001 < i < 126451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 126451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 126451 < i < 126901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 126901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 126901 < i < 127351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 127351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 127351 < i < 127801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 127801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 127801 < i < 128251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 128251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 128251 < i < 128701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 128701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 128701 < i < 129151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 129151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 129151 < i < 129601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 129601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 129601 < i < 130051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 130051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 130051 < i < 130501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 130501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 130501 < i < 130951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 130951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 130951 < i < 131401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 131401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 131401 < i < 131851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 131851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 131851 < i < 132301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 132301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 132301 < i < 132751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 132751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 132751 < i < 133201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 133201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 133201 < i < 133651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 133651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 133651 < i < 134101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 134101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 134101 < i < 134551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 134551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 134551 < i < 135001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 135001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 135001 < i < 135451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 135451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 135451 < i < 135901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 135901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 135901 < i < 136351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 136351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 136351 < i < 136801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 136801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 136801 < i < 137251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 137251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 137251 < i < 137701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 137701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 137701 < i < 138151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 138151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 138151 < i < 138601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 138601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 138601 < i < 139051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 139051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 139051 < i < 139501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 139501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 139501 < i < 139951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 139951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 139951 < i < 140401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 140401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 140401 < i < 140851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 140851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 140851 < i < 141301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 141301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 141301 < i < 141751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 141751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 141751 < i < 142201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 142201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 142201 < i < 142651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 142651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 142651 < i < 143101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 143101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 143101 < i < 143551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 143551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 143551 < i < 144001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 144001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 144001 < i < 144451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 144451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 144451 < i < 144901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 144901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 144901 < i < 145351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 145351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 145351 < i < 145801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 145801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 145801 < i < 146251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 146251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 146251 < i < 146701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 146701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 146701 < i < 147151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 147151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 147151 < i < 147601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 147601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 147601 < i < 148051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 148051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 148051 < i < 148501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 148501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 148501 < i < 148951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 148951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 148951 < i < 149401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 149401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 149401 < i < 149851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 149851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 149851 < i < 150301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 150301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 150301 < i < 150751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 150751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 150751 < i < 151201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 151201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 151201 < i < 151651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 151651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 151651 < i < 152101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 152101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 152101 < i < 152551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 152551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 152551 < i < 153001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 153001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 153001 < i < 153451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 153451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 153451 < i < 153901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 153901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 153901 < i < 154351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 154351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 154351 < i < 154801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 154801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 154801 < i < 155251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 155251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 155251 < i < 155701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 155701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 155701 < i < 156151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 156151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 156151 < i < 156601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 156601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 156601 < i < 157051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 157051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 157051 < i < 157501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 157501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 157501 < i < 157951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 157951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 157951 < i < 158401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 158401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 158401 < i < 158851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 158851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 158851 < i < 159301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 159301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 159301 < i < 159751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 159751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 159751 < i < 160201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 160201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 160201 < i < 160651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 160651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 160651 < i < 161101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 161101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 161101 < i < 161551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 161551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 161551 < i < 162001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 162001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 162001 < i < 162451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 162451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 162451 < i < 162901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 162901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 162901 < i < 163351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 163351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 163351 < i < 163801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 163801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 163801 < i < 164251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 164251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 164251 < i < 164701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 164701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 164701 < i < 165151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 165151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 165151 < i < 165601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 165601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 165601 < i < 166051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 166051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 166051 < i < 166501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 166501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 166501 < i < 166951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 166951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 166951 < i < 167401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 167401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 167401 < i < 167851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 167851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 167851 < i < 168301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 168301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 168301 < i < 168751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 168751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 168751 < i < 169201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 169201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 169201 < i < 169651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 169651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 169651 < i < 170101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 170101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 170101 < i < 170551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 170551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 170551 < i < 171001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 171001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 171001 < i < 171451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 171451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 171451 < i < 171901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 171901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 171901 < i < 172351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 172351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 172351 < i < 172801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 172801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 172801 < i < 173251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 173251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 173251 < i < 173701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 173701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 173701 < i < 174151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 174151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 174151 < i < 174601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 174601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 174601 < i < 175051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 175051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 175051 < i < 175501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 175501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 175501 < i < 175951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 175951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 175951 < i < 176401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 176401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 176401 < i < 176851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 176851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 176851 < i < 177301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 177301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 177301 < i < 177751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 177751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 177751 < i < 178201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 178201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 178201 < i < 178651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 178651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 178651 < i < 179101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 179101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 179101 < i < 179551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 179551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 179551 < i < 180001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 180001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 180001 < i < 180451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 180451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 180451 < i < 180901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 180901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 180901 < i < 181351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 181351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 181351 < i < 181801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 181801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 181801 < i < 182251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 182251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 182251 < i < 182701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 182701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 182701 < i < 183151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 183151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 183151 < i < 183601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 183601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 183601 < i < 184051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 184051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 184051 < i < 184501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 184501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 184501 < i < 184951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 184951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 184951 < i < 185401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 185401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 185401 < i < 185851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 185851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 185851 < i < 186301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 186301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 186301 < i < 186751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 186751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 186751 < i < 187201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 187201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 187201 < i < 187651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 187651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 187651 < i < 188101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 188101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 188101 < i < 188551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 188551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 188551 < i < 189001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 189001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 189001 < i < 189451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 189451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 189451 < i < 189901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 189901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 189901 < i < 190351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 190351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 190351 < i < 190801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 190801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 190801 < i < 191251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 191251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 191251 < i < 191701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 191701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 191701 < i < 192151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 192151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 192151 < i < 192601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 192601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 192601 < i < 193051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 193051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 193051 < i < 193501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 193501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 193501 < i < 193951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 193951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 193951 < i < 194401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 194401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 194401 < i < 194851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 194851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 194851 < i < 195301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 195301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 195301 < i < 195751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 195751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 195751 < i < 196201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 196201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 196201 < i < 196651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 196651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 196651 < i < 197101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 197101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 197101 < i < 197551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 197551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 197551 < i < 198001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 198001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 198001 < i < 198451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 198451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 198451 < i < 198901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 198901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 198901 < i < 199351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 199351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 199351 < i < 199801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 199801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 199801 < i < 200251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 200251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 200251 < i < 200701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 200701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 200701 < i < 201151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 201151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 201151 < i < 201601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 201601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 201601 < i < 202051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 202051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 202051 < i < 202501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 202501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 202501 < i < 202951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 202951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 202951 < i < 203401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 203401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 203401 < i < 203851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 203851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 203851 < i < 204301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 204301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 204301 < i < 204751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 204751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 204751 < i < 205201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 205201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 205201 < i < 205651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 205651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 205651 < i < 206101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 206101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 206101 < i < 206551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 206551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 206551 < i < 207001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 207001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 207001 < i < 207451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 207451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 207451 < i < 207901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 207901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 207901 < i < 208351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 208351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 208351 < i < 208801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 208801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 208801 < i < 209251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 209251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 209251 < i < 209701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 209701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 209701 < i < 210151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 210151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 210151 < i < 210601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 210601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 210601 < i < 211051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 211051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 211051 < i < 211501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 211501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 211501 < i < 211951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 211951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 211951 < i < 212401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 212401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 212401 < i < 212851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 212851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 212851 < i < 213301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 213301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 213301 < i < 213751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 213751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 213751 < i < 214201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 214201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 214201 < i < 214651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 214651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 214651 < i < 215101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 215101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 215101 < i < 215551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 215551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 215551 < i < 216001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 216001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 216001 < i < 216451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 216451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 216451 < i < 216901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 216901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 216901 < i < 217351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 217351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 217351 < i < 217801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 217801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 217801 < i < 218251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 218251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 218251 < i < 218701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 218701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 218701 < i < 219151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 219151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 219151 < i < 219601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 219601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 219601 < i < 220051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 220051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 220051 < i < 220501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 220501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 220501 < i < 220951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 220951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 220951 < i < 221401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 221401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 221401 < i < 221851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 221851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 221851 < i < 222301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 222301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 222301 < i < 222751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 222751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 222751 < i < 223201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 223201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 223201 < i < 223651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 223651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 223651 < i < 224101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 224101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 224101 < i < 224551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 224551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 224551 < i < 225001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 225001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 225001 < i < 225451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 225451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 225451 < i < 225901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 225901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 225901 < i < 226351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 226351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 226351 < i < 226801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 226801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 226801 < i < 227251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 227251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 227251 < i < 227701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 227701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 227701 < i < 228151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 228151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 228151 < i < 228601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 228601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 228601 < i < 229051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 229051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 229051 < i < 229501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 229501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 229501 < i < 229951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 229951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 229951 < i < 230401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 230401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 230401 < i < 230851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 230851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 230851 < i < 231301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 231301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 231301 < i < 231751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 231751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 231751 < i < 232201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 232201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 232201 < i < 232651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 232651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 232651 < i < 233101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 233101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 233101 < i < 233551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 233551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 233551 < i < 234001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 234001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 234001 < i < 234451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 234451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 234451 < i < 234901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 234901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 234901 < i < 235351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 235351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 235351 < i < 235801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 235801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 235801 < i < 236251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 236251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 236251 < i < 236701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 236701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 236701 < i < 237151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 237151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 237151 < i < 237601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 237601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 237601 < i < 238051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 238051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 238051 < i < 238501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 238501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 238501 < i < 238951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 238951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 238951 < i < 239401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 239401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 239401 < i < 239851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 239851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 239851 < i < 240301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 240301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 240301 < i < 240751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 240751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 240751 < i < 241201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 241201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 241201 < i < 241651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 241651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 241651 < i < 242101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 242101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 242101 < i < 242551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 242551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 242551 < i < 243001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 243001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 243001 < i < 243451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 243451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 243451 < i < 243901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 243901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 243901 < i < 244351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 244351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 244351 < i < 244801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 244801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 244801 < i < 245251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 245251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 245251 < i < 245701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 245701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 245701 < i < 246151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 246151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 246151 < i < 246601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 246601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 246601 < i < 247051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 247051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 247051 < i < 247501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 247501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 247501 < i < 247951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 247951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 247951 < i < 248401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 248401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 248401 < i < 248851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 248851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 248851 < i < 249301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 249301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 249301 < i < 249751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 249751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 249751 < i < 250201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 250201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 250201 < i < 250651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 250651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 250651 < i < 251101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 251101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 251101 < i < 251551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 251551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 251551 < i < 252001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 252001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 252001 < i < 252451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 252451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 252451 < i < 252901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 252901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 252901 < i < 253351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 253351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 253351 < i < 253801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 253801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 253801 < i < 254251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 254251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 254251 < i < 254701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 254701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 254701 < i < 255151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 255151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 255151 < i < 255601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 255601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 255601 < i < 256051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 256051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 256051 < i < 256501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 256501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 256501 < i < 256951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 256951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 256951 < i < 257401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 257401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 257401 < i < 257851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 257851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 257851 < i < 258301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 258301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 258301 < i < 258751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 258751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 258751 < i < 259201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 259201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 259201 < i < 259651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 259651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 259651 < i < 260101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 260101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 260101 < i < 260551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 260551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 260551 < i < 261001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 261001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 261001 < i < 261451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 261451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 261451 < i < 261901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 261901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 261901 < i < 262351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 262351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 262351 < i < 262801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 262801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 262801 < i < 263251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 263251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 263251 < i < 263701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 263701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 263701 < i < 264151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 264151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 264151 < i < 264601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 264601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 264601 < i < 265051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 265051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 265051 < i < 265501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 265501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 265501 < i < 265951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 265951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 265951 < i < 266401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 266401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 266401 < i < 266851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 266851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 266851 < i < 267301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 267301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 267301 < i < 267751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 267751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 267751 < i < 268201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 268201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 268201 < i < 268651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 268651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 268651 < i < 269101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 269101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 269101 < i < 269551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 269551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 269551 < i < 270001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 270001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 270001 < i < 270451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 270451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 270451 < i < 270901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 270901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 270901 < i < 271351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 271351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 271351 < i < 271801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 271801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 271801 < i < 272251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 272251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 272251 < i < 272701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 272701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 272701 < i < 273151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 273151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 273151 < i < 273601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 273601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 273601 < i < 274051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 274051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 274051 < i < 274501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 274501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 274501 < i < 274951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 274951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 274951 < i < 275401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 275401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 275401 < i < 275851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 275851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 275851 < i < 276301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 276301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 276301 < i < 276751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 276751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 276751 < i < 277201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 277201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 277201 < i < 277651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 277651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 277651 < i < 278101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 278101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 278101 < i < 278551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 278551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 278551 < i < 279001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 279001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 279001 < i < 279451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 279451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 279451 < i < 279901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 279901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 279901 < i < 280351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 280351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 280351 < i < 280801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 280801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 280801 < i < 281251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 281251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 281251 < i < 281701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 281701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 281701 < i < 282151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 282151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 282151 < i < 282601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 282601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 282601 < i < 283051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 283051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 283051 < i < 283501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 283501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 283501 < i < 283951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 283951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 283951 < i < 284401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 284401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 284401 < i < 284851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 284851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 284851 < i < 285301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 285301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 285301 < i < 285751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 285751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 285751 < i < 286201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 286201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 286201 < i < 286651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 286651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 286651 < i < 287101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 287101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 287101 < i < 287551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 287551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 287551 < i < 288001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 288001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 288001 < i < 288451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 288451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 288451 < i < 288901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 288901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 288901 < i < 289351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 289351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 289351 < i < 289801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 289801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 289801 < i < 290251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 290251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 290251 < i < 290701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 290701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 290701 < i < 291151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 291151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 291151 < i < 291601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 291601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 291601 < i < 292051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 292051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 292051 < i < 292501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 292501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 292501 < i < 292951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 292951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 292951 < i < 293401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 293401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 293401 < i < 293851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 293851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 293851 < i < 294301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 294301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 294301 < i < 294751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 294751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 294751 < i < 295201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 295201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 295201 < i < 295651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 295651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 295651 < i < 296101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 296101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 296101 < i < 296551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 296551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 296551 < i < 297001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 297001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 297001 < i < 297451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 297451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 297451 < i < 297901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 297901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 297901 < i < 298351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 298351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 298351 < i < 298801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 298801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 298801 < i < 299251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 299251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 299251 < i < 299701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 299701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 299701 < i < 300151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 300151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 300151 < i < 300601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 300601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 300601 < i < 301051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 301051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 301051 < i < 301501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 301501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 301501 < i < 301951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 301951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 301951 < i < 302401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 302401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 302401 < i < 302851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 302851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 302851 < i < 303301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 303301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 303301 < i < 303751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 303751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 303751 < i < 304201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 304201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 304201 < i < 304651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 304651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 304651 < i < 305101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 305101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 305101 < i < 305551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 305551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 305551 < i < 306001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 306001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 306001 < i < 306451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 306451:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 306451 < i < 306901:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 306901:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 306901 < i < 307351:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 307351:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 307351 < i < 307801:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 307801:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 307801 < i < 308251:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 308251:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 308251 < i < 308701:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 308701:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 308701 < i < 309151:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 309151:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 309151 < i < 309601:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 309601:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 309601 < i < 310051:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 310051:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 310051 < i < 310501:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 310501:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 310501 < i < 310951:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 310951:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 310951 < i < 311401:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 311401:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 311401 < i < 311851:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 311851:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 311851 < i < 312301:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 312301:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 312301 < i < 312751:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 312751:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 312751 < i < 313201:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 313201:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 313201 < i < 313651:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 313651:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 313651 < i < 314101:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 314101:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 314101 < i < 314551:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 314551:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 314551 < i < 315001:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if i == 315001:
      time.sleep(65)
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)
    if 315001 < i < 315451:
      next_url = ListofOKCases[i]
      print next_url
      record = {}
      record['URL'] = next_url
      scraperwiki.sqlite.save(['URL'], record)
      scrape_and_look_for_next_link(next_url)


    '
        
           
        
        
# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then 
# call a function to scrape the first page in the series.
# ---------------------------------------------------------------------------
base_url = 'http://www.oscn.net/dockets/'
starting_url = urlparse.urljoin(base_url, 'GetCaseInformation.aspx?db=garfield&number=CF-2011-1')
print starting_url
global i
i = 1
#for i in range(0,1):
    #There are 743 cases but 468 appears to be the server request limit
CaseEndingNumbers()
ListOfCaseEndingNumbers = list(CaseEndingNumbers())
GetOklahomaStateCases()
ListofOKCases = list(GetOklahomaStateCases())
scrape_and_look_for_next_link(starting_url)     
    
    
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
