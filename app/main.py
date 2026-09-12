from fastapi import FastAPI

app = FastAPI(title="非遗工坊订单")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
