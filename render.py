from collections import defaultdict
import os.path
import glob
import jinja2
import codecs

def read_source(filename):
    r = defaultdict(str)
    r["filename"] = filename
    r["file_base"] = os.path.basename(filename.replace(".idx", "") if ".idx" in filename 
                                      else filename.replace(".article", ""))
    field = "body"
    with codecs.open(filename, encoding="utf-8") as f:
        for l in f.readlines():
            if l[:2] == "@@":
                field = l[2:l.find(" ")]
                if l.find(" ") > 0:
                    r[field] += l[l.find(" ")+1:]
            else:
                r[field] += l
    return r

def get_news(folder):
    newsletters = []
    for idx in glob.glob(os.path.join(folder, "*.idx")):
        index = read_source(idx)
        index["articles"] = [read_source(x) for x in 
                             glob.glob(os.path.join(folder, index["file_base"]+"*.article"))]
        newsletters.append(index)
    return newsletters

def render_news(news):
    print news
    news.sort(key=lambda k: k["date"], reverse=True)
    tl = jinja2.FileSystemLoader(searchpath="templates/")
    tEnv = jinja2.Environment(loader=tl)
    articlet = tEnv.get_template("article.php")
    indext = tEnv.get_template("news.php")
    nlt = tEnv.get_template("nl.php")
    index_page = indext.render({"news": news})
    with codecs.open("output/news.php", mode="w", encoding="utf-8") as outf:
        outf.write(index_page)
    for letter in news:
        page = nlt.render({"letter": letter})
        with codecs.open(os.path.join("output", letter["file_base"]+".php"), 
                         mode="w", encoding="utf-8") as outf:
            outf.write(page)
        print letter["articles"]
        for article in letter["articles"]:
            page = articlet.render({"article": article})
            with codecs.open(os.path.join("output", article["file_base"]+".php"), 
                             mode="w", encoding="utf-8") as outf:
                outf.write(page)
        
if __name__ == "__main__":
    render_news(get_news("source/"))
    
