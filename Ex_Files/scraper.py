import requests
from bs4 import BeautifulSoup
import datetime

url = "https://pixelford.com/blog/"
response = requests.get(url)
html = (response.content)
soup = BeautifulSoup(html, 'html.parser')
#a_tags = soup.find_all('a', class_="entry-title-link")
blogs = soup.find_all('article', class_="type-post")

for blog in blogs:
    title = blog.find('a', class_="entry-title-link").get_text()
  #  print(title)

    blog_datetime_string = blog.find(
        'time', class_="entry-time").get('datetime')
  #  print(blog_datetime_string)

    blog_datetime = datetime.datetime.fromisoformat(blog_datetime_string)
    pretty_date = blog_datetime.strftime("%A %m %B %H:%M:%S")
    print(f"{pretty_date} - {title}")

# for a_tag in a_tags:
#  print(a_tag.get_text())

#titles = list(map(lambda a_tag: a_tag.get_text(), a_tags))
# print(titles)
