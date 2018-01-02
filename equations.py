from requests import get
URL = 'http://latex.codecogs.com/png.latex'

def equation_to_png(code, f):
    data = get(f"{URL}?{code}")
    f.write(data.content)
