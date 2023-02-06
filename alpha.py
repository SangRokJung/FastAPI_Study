from typing import Optional
from fastapi import FastAPI

app = FastAPI()

MALES = {
    'alpha' : {'id': 1, "user_img_url" : "url", "age" : 22, "mbti" : "ESTJ", "created_at" : "1998.11.10", "created_by" : "JSR"},
    'beta' : {'id': 2, "user_img_url" : "url", "age" : 22, "mbti" : "ESTJ", "created_at" : "1998.11.10", "created_by" : "JSR"},
    'gamma' : {'id': 3, "user_img_url" : "url", "age" : 22, "mbti" : "ESTJ", "created_at" : "1998.11.10", "created_by" : "JSR"},
    'delta' : {'id': 4, "user_img_url" : "url", "age" : 22, "mbti" : "ESTJ", "created_at" : "1998.11.10", "created_by" : "JSR"},
    'omega' : {'id': 5, "user_img_url" : "url", "age" : 22, "mbti" : "ESTJ", "created_at" : "1998.11.10", "created_by" : "JSR"},
}

@app.get("/")
async def read_all_male(skip_male: Optional[str] = None):
    if skip_male :
        new_males = MALES.copy()
        del new_males[skip_male]
        return new_males
    return MALES

