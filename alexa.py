import requests

headers = {'Pragma': 'no-cache',
           'csrf': 'XXXXXXXXXX',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': ':en-US,en;q=0.8,fr;q=0.6,mk;q=0.4,sr;q=0.2,cs;q=0.2,ru;q=0.2,it;q=0.2,es;q=0.2,pt;q=0.2,hr;q=0.2,bg;q=0.2',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Cache-Control': 'no-cache',
           'Referer': 'http://alexa.amazon.com/spa/index.html',
           'Cookie': 'XXXXXXXXXX',
           'Connection': 'keep-alive',
           'Content-Length': '0',
           'Origin': 'http://alexa.amazon.com'
           }


def set_tunein_station(station):
    url = 'https://pitangui.amazon.com/api/tunein/queue-and-play?deviceSerialNumber=XXXXXXXXXX&deviceType=AB72C64C86AW2&guideId=' + \
          station + \
          '&contentType=station&callSign=&mediaOwnerCustomerId=XXXXXXXXXX'

    headers_tunein = {'Content-Type': 'application/json; charset=UTF-8',
                      'Content-Length': '0',
                      }
    headers_tunein.update(headers)

    return requests.post(url, headers=headers_tunein)


def set_volume(volume):
    url2 = 'https://pitangui.amazon.com/api/np/command?deviceSerialNumber=XXXXXXXXXX&deviceType=AB72C64C86AW2'

    headers_volume = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', }
    headers_volume.update(headers)

    return requests.post(url2, headers=headers_volume, data='{"type":"VolumeLevelCommand","volumeLevel":' + str(volume) + '}')

if __name__ == "__main__":
    set_volume(25)
    set_tunein_station('s25814')  # Cannes Radio
