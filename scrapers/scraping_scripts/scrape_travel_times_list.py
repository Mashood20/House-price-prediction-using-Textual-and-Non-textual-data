def run(soup):
    try:
        travel_times_list = []
        travel_times_ul = soup.find('ul', class_='x63et80').find_all('li')

        for li in travel_times_ul:
            if li.find('use', href='#school-small'):
                amenity = 'school'
            elif li.find('use', href='#national-rail-colour-small'):
                amenity = 'station'
            elif li.find('use', href='#london-underground-colour-small'):
                amenity = 'station'
            elif li.find('use', href='#london-dlr-colour-small'):
                amenity = 'station'
            elif li.find('use', href='#ferry-small'):
                amenity = 'ferry'
            else:
                amenity = None
            
            try:
                miles = li.find('span', class_='x63et83').text.strip()
            except:
                miles = None
                
            travel_times_list.append((amenity, miles))
    except:
        travel_times_list = None

    return travel_times_list