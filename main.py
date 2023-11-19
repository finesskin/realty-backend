from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI()


@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/docs", status_code=308)

# if __name__ == '__main__':
#     uvicorn.run(app=app)
