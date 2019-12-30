from bs4 import BeautifulSoup

soup = BeautifulSoup(open("python_knowledge/metaclass.html"), "html.parser")


# print(soup.find("body"))
# for h3 in soup.find_all("h3"):
#     print(h3, end=f"\n{'='*30}\n\n")
