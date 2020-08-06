#! python3
# multidownloadX.py - Downloads every single XKCD comic threaded

import requests, os, threading
import bs4

url = 'http://xkcd.com' #starting url
os.makedirs('xkcd_m', exist_ok = True) # store comics in ./xkcd_m

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

       #Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        url = 'http://xkcd.com' #starting url
        res = requests.get(url + comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd_m', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

# TODO: Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')



# Create and start the Thread objects
downloadThreads = []  # a list of all the thread objects

for i in range(0, 1400, 100):   # loops 14 times , creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(1, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()


# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')



    

    