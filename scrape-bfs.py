html = """
<html>
<head> <title> Beautiful Soup Example </title> </head>
<div id="test"><p>Sample Text inside div</p></div>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
print(soup.div.p)
