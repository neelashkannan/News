from GoogleNews import GoogleNews
googlenews=GoogleNews()
googlenews=GoogleNews('en', 'd')
a = input()
googlenews.search(a)
googlenews.getpage(2)
for i in range (0,20):
    r = googlenews.result()[i]
    res = {key: r[key] for key in r.keys()
       & {'desc','title'}}
    print(str(res))
googlenews.gettext()
