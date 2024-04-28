def run(soup):
    try:
        map_picture = soup.find('picture', attrs={'data-testid':'static-google-image'})
        srcset = map_picture.find('source', attrs={'media':True}).get('srcset')
        location = srcset.split('&')[3].replace('center=','').split(',')
    except:
        location = None
    
    return location
