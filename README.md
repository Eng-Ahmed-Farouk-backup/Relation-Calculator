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

and replacing the r with your relation and the x with your X set and the y with your Y set

### domain

this endpoint calculates the domain of the relation and takes the same inputs as the relation endpoint and can be accessed using this link:

https://relation-calculator-production.up.railway.app/domain?relation=r&X=x&Y=y

and replacing the r with your relation and the x with your X set and the y with your Y set

### range

this endpoint calculates the range of the relation and takes the same inputs as the relation endpoint and can be accessed using this link:

https://relation-calculator-production.up.railway.app/range?relation=r&X=x&Y=y

and replacing the r with your relation and the x with your X set and the y with your Y set

### cartesian product

this endpoint calculates the cartesian product of X and Y and takes these inputs:

- `X` -> this is the set X and is written in this form "1,2,3,4,5,6" and can be written as a range i.e "1:5" this produces the set "1,2,3,4,5"

- `Y` -> this is the set Y and is written in this form "1,2,3,4,5,6" and can be written as a range i.e "1:5" this produces the set "1,2,3,4,5"

this endpoint can be accessed using this link:

https://relation-calculator-production.up.railway.app/cartesian_product?X=x&Y=y

and replacing the x with your X set and the y with your Y set

### is function

this endpoint checks if a relation is a function or not

a function is a relation where every element in X is mapped to only 1 element

this enpoint can be accessed using this link:

https://relation-calculator-production.up.railway.app/is_function?relation=r&X=x&Y=y

and replacing the r with your relation and the x with your X set and the y with your Y set

# Author

this is an API Made By Ahmed Farouk Passionate about STEAM, Entrepreneurship

- Leader of Innovations Hack Club
- Founder & CEO of Adapt Community
- Ex Contractor @ Hack club under the Management of Christina (the co founder)
