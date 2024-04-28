def run(link):
    field = link.find('div', class_='_14bi3x30', text='Shared ownership')
    if field is None:
        shared_ownership = 0
    else:
        shared_ownership = 1

    return shared_ownership