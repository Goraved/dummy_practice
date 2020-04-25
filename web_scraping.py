import requests
import json
from bs4 import BeautifulSoup


def get_articles_with_needed_count_of_votes(soup, min_count, articles, page_index):
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    for ind, link in enumerate(links):
        votes = subtext[ind].select('.score')
        vote_count = 0 if not votes else int(votes[0].getText().replace(' points', ''))
        if vote_count >= min_count:
            title = link.getText()
            href = link.get('href', None)
            articles.append({'title': title, 'link': href, 'votes': vote_count, 'page': page_index})


def get_articles_for_pages(pages, min_votes):
    articles = []
    for page in range(1, pages + 1):
        res = requests.get(f'https://news.ycombinator.com/news?p={page}')
        soup = BeautifulSoup(res.text, 'html.parser')
        get_articles_with_needed_count_of_votes(soup, min_votes, articles, page)
    return articles


arts = get_articles_for_pages(2, 100)
print(json.dumps(arts, indent=4))
