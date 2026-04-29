import urllib.request
from urllib.parse import urljoin, urlparse, unquote, urldefrag
from html.parser import HTMLParser


class LinkParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value:
                    self.links.append(value)


def clean_url(url):
    decoded = unquote(url)
    without_fragment = urldefrag(decoded)[0]
    return without_fragment


def get_links(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "MobileCyberLab/1.0"
    })

    response = urllib.request.urlopen(req, timeout=5)
    html = response.read().decode(errors="ignore")

    parser = LinkParser()
    parser.feed(html)

    links = []

    for link in parser.links:
        full_url = urljoin(url, link)
        cleaned = clean_url(full_url)
        links.append(cleaned)

    return links


def crawl(start_url, max_depth=1):
    visited = set()
    base_domain = urlparse(start_url).netloc

    def visit(url, depth):
        if depth > max_depth:
            return

        url = clean_url(url)

        if url in visited:
            return

        parsed = urlparse(url)

        if parsed.netloc != base_domain:
            return

        if parsed.scheme not in ["http", "https"]:
            return

        visited.add(url)
        print("[URL]", url)

        try:
            links = get_links(url)

            for link in links:
                visit(link, depth + 1)

        except Exception as e:
            print("[ERROR]", url, e)

    visit(start_url, 0)


if __name__ == "__main__":
    start = input("Start URL: ")
    depth = int(input("Max depth: "))

    crawl(start, depth)