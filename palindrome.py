from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/add/{num_1}/{num_2}")
def add(num_1: int, num_2: int):
    return {"answer": num_1+num_2}

def is_palindrome(num:str):
    return num == num[::-1]

@app.get("/palindrome")
def palindrome():
    max_num = [0,0]
    max_pal = 0
    for i in range(100, 1000):
        for j in range(100,1000):
            if is_palindrome(str(i*j)):
                if max(i*j,max_pal) == i*j:
                    max_pal = i*j
                    max_num[0]= i
                    max_num[1]= j
    return {"max palindrome": max_pal, "By": max_num}

