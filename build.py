"""Rebuild index.html after editing wedding.json or template.html:  python3 build.py"""
import json
t=open('template.html',encoding='utf-8').read()
data=json.dumps(json.load(open('wedding.json',encoding='utf-8')),ensure_ascii=False).replace('</','<\\/')
frag=t.replace('__WEDDING_JSON__',data)
head,body=frag.split('</style>',1)
open('index.html','w',encoding='utf-8').write('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'+head+'</style>\n</head>\n<body>\n'+body+'\n</body>\n</html>\n')
print("index.html rebuilt")
