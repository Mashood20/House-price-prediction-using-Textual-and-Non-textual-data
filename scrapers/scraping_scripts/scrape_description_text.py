def run(soup):    
    try:
        description_text = ' '.join(soup.find('div', class_='ckazh53').stripped_strings).split('<br>')[0]
    except:
        description_text = None
    
    return description_text