from datetime import date
from bs4 import BeautifulSoup
import urllib.request, re, csv


def get_soup_obj(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_ISONE_prices():
    prices = []

    url = 'http://www.iso-ne.com/' \
              'transform/csv/hourlylmp/current?type=prelim&market=rt'

    zones = {'4001': '.Z.MAINE',
             '4002': '.Z.NEWHAMPSHIRE',
             '4003': '.Z.VERMONT',
             '4004': '.Z.CONNECTICUT',
             '4005': '.Z.RHODEISLAND',
             '4006': '.Z.SEMASS',
             '4007': '.Z.WCMASS',
             '4008': '.Z.NEMASSBOST'}

    try:
        with urllib.request.urlopen(url) as response:
            datareader = \
                csv.reader(response.read().decode('utf-8').splitlines())
    except:
        return prices

    data = []
    for row in datareader:
        if row[0] == 'D' and row[3] in zones.keys():
            data.append(row)

    for row in data:
        prices.append((zones[row[3]], row[-1]))

    return prices


def get_NYISO_prices():
    prices = []
    url = 'http://mis.nyiso.com/public/htm/rtlbmp/' + \
          str(date.today()).replace('-', '', 2) + 'rtlbmp_zone.htm'
    try:
        soup = get_soup_obj(url)
    except:
        return prices

    target_rows = soup.body.table.find_next('table')\
        .find_next('table').select('tr[valign="top"]')

    for row in target_rows:
        columns = row.select('td')
        first_column_contents = columns[0].font.contents
        last_column_contents = columns[-1].font.contents
        if re.match(r'[A-Z]+', first_column_contents[0]):
            prices.append((first_column_contents[0], last_column_contents[0]))

    return prices


def get_PJM_prices():
    prices = []
    try:
        soup = get_soup_obj('http://pjm.com/pub/account/lmpgen/lmppost.html')
    except:
        return prices

    target_rows = soup.find('table').find_next('table').find_all('tr')

    for child in target_rows:
        columns = child.find_all('td')
        if columns[1].string == 'ZONE':
            prices.append((columns[0].string, columns[3].string))

    return prices


def get_ERCOT_prices():
    headers = []
    lmps = []
    url = 'http://www.ercot.com/content/cdr/html/' + \
          str(date.today()).replace('-', '', 2) + '_real_time_spp'
    try:
        soup = get_soup_obj(url)
    except:
        return zip(headers, lmps)

    header_row = \
        soup.find('table', class_='tableStyle')\
            .find_all('th', class_="headerValueClass")

    for elem in header_row[-6:]:
        headers.append(elem.string)

    rows = soup.find('table', class_='tableStyle').find_all('tr')
    last_row = rows[-1].find_all('td')

    for elem in last_row[-6:]:
        lmps.append(elem.string)

    return zip(headers, lmps)
