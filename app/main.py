from fastapi import FastAPI

app = FastAPI()


@app.get("/health_check")
async def health_check():
    return {"status": "ok"}


@app.get("/hello_word")
async def hello_word():
    return {"message": "Hello, world!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)

