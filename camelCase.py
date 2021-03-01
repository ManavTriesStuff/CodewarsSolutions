#Solution 1
# def to_camel_case(s):
#     return s[0] + s.title().translate(None, "-_")[1:] if s else s

 #Solution 2
 def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])