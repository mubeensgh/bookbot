def count_words(text):
    res = len(text.split())
    return res

def count_characters(text):
    ltext = text.lower()
    res={}
    for i in ltext:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    return res

def sort_on(dict):
    return dict["num"]

def sorted_dicts(dict):
    res=[]
    for i in dict:
        res.append({"char" : i,"num":dict[i]})
    res.sort(reverse=True, key=sort_on)    
    return res
