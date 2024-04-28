def run(soup):
    try:
        description_list = [li.text.strip() for li in soup.find('ul', class_='_15py5em0').find_all('li')]
    except:
        description_list = None

    return description_list