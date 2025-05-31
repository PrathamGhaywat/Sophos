import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

def fetch_arxiv_articles(query, max_results=3):
    base_url = 'http://export.arxiv.org/api/query?'
    params = {
        'search_query': f'all:{query}',
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    url = base_url + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MyArxivClient/1.0 (email@example.com)"}
    )
    with urllib.request.urlopen(req) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    entries = root.findall('atom:entry', ns)

    articles = ""
    for idx, entry in enumerate(entries, 1):
        title = entry.find('atom:title', ns).text.strip()
        authors = [author.find('atom:name', ns).text.strip() for author in entry.findall('atom:author', ns)]
        summary = entry.find('atom:summary', ns).text.strip()
        articles += f"Article {idx}:\n"
        articles += f"Title: {title}\n"
        articles += f"Authors: {', '.join(authors)}\n"
        articles += f"Summary: {summary}\n"
        articles += "-" * 80 + "\n"

    return articles
