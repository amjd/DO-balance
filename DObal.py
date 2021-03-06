import mechanize
import cookielib
from bs4 import BeautifulSoup

br = mechanize.Browser()

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open('https://cloud.digitalocean.com/login')

br.select_form(nr=0)

#Specify your credentials here

br.form['user[email]'] = 'EMAIL_ID'
br.form['user[password]'] = 'PASSWORD'

br.submit()

r = br.open('https://cloud.digitalocean.com/billing')

html = r.read()

soup = BeautifulSoup(html)

elem = soup.find_all("h3",class_='credit')[0]

soup2 = BeautifulSoup(str(elem))

result = soup2.get_text().splitlines()[1]

print result
