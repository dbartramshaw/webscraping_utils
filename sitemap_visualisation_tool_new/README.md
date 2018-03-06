# Visualising BT's sitemap using Python

Initial visualisation. Needs to be updated into a dynamic tool that allows you to select metrics and level of depth.
Exploration of graph devs to be explored, includng the size of nodes and vertices.


## Dependencies

The code can run in Python 2 or 3 and the external library dependencies are as follows:

 - Requests and BeautifulSoup4 for `extract_urls.py`
 - Pandas for `categorize_urls.py`
 - Graphviz for `visualize_urls.py`

Once you have Python, these libraries can most likely be installed on any operating system with the following terminal commands:

```
pip install requests   
pip install beautifulsoup4   
pip install pandas   
```

The Graphviz library is more difficult to install. On Mac it can be done with the help of homebrew:

```
brew install graphviz   
pip install graphviz   
```

For other operating systems or alternate methods, check out the [installation instructions in the Graphviz documentation](http://graphviz.readthedocs.io/en/latest/manual.html).

