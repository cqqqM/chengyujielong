import json

with open('C://Users/machunqi/Desktop/cy.json','r') as f:
	text = f.read()

parse = json.loads(text)

cy = {}

for i in range(len(parse)):
    cy[parse[i]["word"]] = parse[i]["explanation"]

print('成语词典长度：{:d}'.format(len(cy)))

def jielong(cy1):
    word = cy1[-1]
    for key in cy:
        if word == key[0]:
            print(key)
            print(cy[key])
            break
            
def chaci(cy1):
    print(cy[cy1])
