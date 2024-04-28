def run(soup):
    try:
        price = soup.find('p', class_='_194zg6t4 _18cwln10', attrs={'data-testid': 'price'}).text.strip()
    except:
        price = None

    return price
