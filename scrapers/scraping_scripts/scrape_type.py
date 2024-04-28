def run(soup):
    try:
        type = soup.find('p', class_='_194zg6t7 _18cwln11', attrs={'data-testid': 'title-label'}).text.strip()
    except:
        type = None
    
    return type