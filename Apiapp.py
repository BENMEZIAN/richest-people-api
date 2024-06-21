from fastapi import FastAPI

app = FastAPI()

"""
@app.get("/")
async def root():
    return {"message" : "Hello World"}
"""
richest_people_list = {
    "Abdelmalek Benmeziane": "350 billion usd",
    "Elon Musk": "280 billion usd",
    "Jeff Bezos": "250 billion usd",
    "Bill Gates": "190 billion usd",
    "Mark Zuckerberg": "150 billion usd",
}

@app.get("/richest-people")
def richest_people():
    return richest_people_list
