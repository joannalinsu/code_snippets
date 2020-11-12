import urllib.request
import http.cookiejar

#set up cookike opener
cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders=[('User-agent', 'Mozilla/5.0')]

weburl = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.atom'
infile = opener.open(weburl)
newpage = infile.read().decode('utf-8', errors ='ignore')
outfile = open('earthquake.txt','w', encoding ='utf-8', errors ='ignore')  
header = 'magnitude|location|time|latitude|longitude'
print(header, file = outfile)

keyword = '<entry><id>urn:earthquake-usgs-gov'
findentry = newpage.find(keyword)

#basic
while findentry > -1:
    index1 = newpage.find('<title>M',findentry)
    index2 = newpage.find('</title>',index1)
    index3 = newpage.find('<updated>',index2)
    index4 = newpage.find('</updated>',index3)
    index5 = newpage.find('<dt>Location</dt>',index4)
    index6 = newpage.find('&deg;',index5)
    index7 = newpage.find('&deg;',index6)
    index8 = newpage.find('</dd><dt>Depth',index7)
    index9 = newpage.find('km', index8)

    magnitude = float(newpage[index1+9:index1+12])
    location = newpage[index1+15:index2]
    if magnitude >= 4.0:
        print("magnitude:", magnitude,'location:',location)

    time = newpage[index3+9:index4]
    
    lat = newpage[index5+21:index6]
    lat_1 = newpage[index6+5:index6+7]  
    lon = newpage[index7+7:index8-6]
    lon_1 =newpage[index7+5:index7+7]  ## cant really parse this part. not sure why. but wont hurt the result
    
    depth = int(float(newpage[index8+23:index9])*1000)

    print(magnitude,"|",location,"|",time,"|",lat,"|",lon,"|", depth, file =outfile)

    findentry = newpage.find(keyword,index3)
    



