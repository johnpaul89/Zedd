import json

def getJSON(filePathAndName):
    with open('/home/john/Projects/Django/Web_Apps/PhoNews/News/nation.json', 'r') as fp:
        return json.load(fp)

nationId = getJSON('fp').get('id',[])
nationTitle = getJSON('fp').get('title',[])
nationDate = getJSON('fp').get('date',[])
nationArticle = getJSON('fp').get('article',[])
nationArticleUrl = getJSON('fp').get('articleUrl',[])
nationImageUrl = getJSON('fp').get('imageUrl',[])
