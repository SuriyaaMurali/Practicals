import wikipedia


def wiki_search():
    page_or_phrase = input('Type page name or phrase here:')
    while page_or_phrase != '':
        page_or_phrase = input('Type page name or phrase here:')
        search_page = wikipedia.search(page_or_phrase)
        print(wikipedia.summary(search_page))


wiki_search()
