from math import *

def parse_relation(relation):
    parsed_relation = (None,None,None)
    possible_exp = ["=","!=",">","<",">=","<="]
    for exp in possible_exp:
        if exp in relation:
            a,b = extract_relation(relation,exp)
            if exp == "=":
                exp = "=="
            parsed_relation = (a,b,exp)
    return parsed_relation

def extract_relation(exp,sign):
    a,b = exp.replace("^","**").split(sign)
    for e in a.split("+"):
        r = e
        for f in range(len(e)):
            if e[f].isalpha() and e[f-1].isdigit():
                r = e.replace(e[f],f"*{e[f]}")
        r = r.removeprefix("*")
        a = a.replace(e,r)

        
    for e in b.split("+"):
        for f in range(len(e)):
            r = e
            if e[f].isalpha() and e[f-1].isdigit():
                r = e.replace(e[f],f"*{e[f]}")
        r = r.removeprefix("*")
        b = b.replace(e,r)
            
    return a.strip(),b.strip()

def calculate_relation(relation,X,Y):
    rel = set()
    for x in X:
        for y in Y:
            a,b,exp = parse_relation(relation)
            a = a.replace("x",str(x)).replace("y",str(y))
            b = b.replace("x",str(x)).replace("y",str(y))
            if eval(a+exp+b):
                rel.add((x,y))
    return rel
        
    for e in b.split("+"):
        for f in range(len(e)):
            r = e
            if e[f].isalpha() and e[f-1].isdigit():
                r = e.replace(e[f],f"*{e[f]}")
        r = r.removeprefix("*")
        b = b.replace(e,r)
            
    return a.strip(),b.strip()

def calculate_domain(relation,X,Y):
    domain = set()

    rel = calculate_relation(relation,X,Y)
    for x,y in rel:
        domain.add(x)
    return domain
            
def calculate_range(relation,X,Y):
    range_ = set()

    rel = calculate_relation(relation,X,Y)
    for x,y in rel:
        range_.add(y)
    return range_

def calculate_cartesian_product(X,Y):
    return calculate_relation("1=1",X,Y)

def is_function(relation,X,Y):
    rel = calculate_relation(relation,X,Y)
    for x in X:
        count = 0
        for y in Y:
            if (x,y) in rel:
                count += 1
        if count != 1:
            return False
    return True
