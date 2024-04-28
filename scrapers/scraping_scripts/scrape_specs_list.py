def run(soup):
    try:
        specs_list = []
        specs_div = soup.find_all('div', class_='jc64990 jc64995 _194zg6t8')
        
        for i in specs_div:
            if i.find('use', href = '#bedroom-medium'):
                spec_name = 'beds'
            elif i.find('use', href = '#bathroom-medium'):
                spec_name = 'baths'
            elif i.find('use', href = '#living-room-medium'):
                spec_name = 'receptions'
            elif i.find('use', href = '#dimensions-medium'):
                spec_name = 'area'
            elif i.find('use', href = '#epc-medium'):
                spec_name = 'epc_rating'
            else:
                spec_name = None

            try:
                spec_value = i.find('div', class_= '_14bi3x30').text.strip()
            except:
                spec_value = None

            specs_list.append((spec_name, spec_value))
    except:
            specs_list = None
    
    return specs_list