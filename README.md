# Relation Function

An API made using python FastAPI library that calculates the relation set including the domain, range,  cartesian product, and also checking if a relation is a function

<img width="950" height="503" alt="image" src="https://github.com/user-attachments/assets/8c7531bc-bdb8-454a-ba89-ae1615e168a0" />


## Project architecture

- `algorithm.py` -> includes all helper functions to calculate the relations,domains, etc
- `main.py` -> contains all endpoints and manages the interface

## Endpoints

### docs

contains the docs page(built in UI interface for FastAPI) and can be used to access all endpoints and can be accessed using this link

https://relation-calculator-production.up.railway.app/docs

please use the this interface

### relation

this endpoint calculates the relation and takes these inputs:

- `relation` -> this is the relation written in form of X->Y i.e "2x>y"

- `X` -> this is the set X and is written in this form "1,2,3,4,5,6" and can be written as a range i.e "1:5" this produces the set "1,2,3,4,5"

- `Y` -> this is the set X and is written in this form "1,2,3,4,5,6" and can be written as a range i.e "1:5" this produces the set "1,2,3,4,5"

this endpoint can be accessed using this link:

https://relation-calculator-production.up.railway.app/relation?relation=r&X=x&Y=y

for example:

https://relation-calculator-production.up.railway.app/relation?relation=2x>y&X=1,2,3,4,5,6&Y=1:4

and replacing the r with your relation and the x with your X set and the y with your Y set

### domain

this endpoint calculates the domain of the relation and takes the same inputs as the relation endpoint and can be accessed using this link:

https://relation-calculator-production.up.railway.app/domain?relation=r&X=x&Y=y

and replacing the r with your relation and the x with your X set and the y with your Y set i.e

https://relation-calculator-production.up.railway.app/domain?relation=2x>y&X=1,2,3,4,5,6&Y=1:4

### range

this endpoint calculates the range of the relation and takes the same inputs as the relation endpoint and can be accessed using this link:

https://relation-calculator-production.up.railway.app/range?relation=r&X=x&Y=y

and replacing the r with your relation and the x with your X set and the y with your Y set i.e

https://relation-calculator-production.up.railway.app/range?relation=2x>y&X=1,2,3,4,5,6&Y=1:4

### cartesian product

this endpoint calculates the cartesian product of X and Y and takes these inputs:

- `X` -> this is the set X and is written in this form "1,2,3,4,5,6" and can be written as a range i.e "1:5" this produces the set "1,2,3,4,5"

- `Y` -> this is the set Y and is written in this form "1,2,3,4,5,6" and can be written as a range i.e "1:5" this produces the set "1,2,3,4,5"

this endpoint can be accessed using this link:

https://relation-calculator-production.up.railway.app/cartesian_product?X=x&Y=y

and replacing the x with your X set and the y with your Y set i.e

https://relation-calculator-production.up.railway.app/cartesian_product?X=1,2,3,4,5,6&Y=1:4

### is function

this endpoint checks if a relation is a function or not

a function is a relation where every element in X is mapped to only 1 element

this enpoint can be accessed using this link:

https://relation-calculator-production.up.railway.app/is_function?relation=r&X=x&Y=y

and replacing the r with your relation and the x with your X set and the y with your Y set i.e

https://relation-calculator-production.up.railway.app/is_function?relation=2x>y&X=1,2,3,4,5,6&Y=1:4

# Math
## basics
an ordered pair is expressed as this (x,y) i.e (1,2) such that when entering x as the input of a function you get output y( f(x) = y )

a set is a list where elements do not repeat i.e {1,2,3,4}

## Relations

a relation set is the product of taking every x value in the set X and every y value in the set Y and checking if a condition is true
i.e 

X = {1,2,3}, Y = {2,3,4,5} where x + y = 5

this means that we take every element in the X set and pair it with every element in the Y set and checking if the condition is true

i.e 
- x->1, y->2 so x + y = 1 + 2 = 3 not equal to 5
- x->2, y->3 so x + y = 2 + 3 = 5 equal to 5

so we add the ordered pair (2,3) and not (1,2) because (2,3) meets the condition and (1,2) does not

the result is expressed in this form for the previous relation

{(1,4),(2,3),(3,2)}

this is called the relation set

## Domain
the domain is a set of all x values in the relation set i.e

the domain of this relation set 

{(1,4),(2,3),(3,2)} is {1,2,3}

## Range
the range is a set of all y values in the relation set i.e

the range of this relation set 

{(1,4),(2,3),(3,2)} is {2,3,4}

## Cartesian product
the cartesian product is the set of all ordered pair from the sets X and Y i.e 

if X = {1,2,3} and Y = {2,3,4}

the cartesian product will be 

{(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,2),(3,3),(3,4)}

## Functions 
a function is a relation where every x element is mapped with only 1 element i.e

relation set = {(1,4),(2,3),(3,2)}

X = {1,2,3}, Y = {2,3,4,5}

this is a function because every element in the X set is in the relation set once

while in this example

relation set = {(1,4),(2,3),(3,2),(3,5)}

X = {1,2,3}, Y = {2,3,4,5}

this is not a function because the element 3 appeared 2 times

and in this example

relation set = {(1,4),(2,3)}

X = {1,2,3}, Y = {2,3,4,5}

this is a function because the element 3 did not appear 
### note
not every element in the Y set should be in the relation set



# Author

this is an API Made By Ahmed Farouk Passionate about STEAM, Entrepreneurship

- Leader of Innovations Hack Club
- Founder & CEO of Adapt Community
- Ex Contractor @ Hack club under the Management of Christina (the co founder)
