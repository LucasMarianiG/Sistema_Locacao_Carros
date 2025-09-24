from fastapi import FastAPI
from util.database import init_db
from controller.endereco import router as endereco_router
from controller.locatario import router as locatario_router
from controller.locador import router as locador_router
from controller.carro import router as carro_router
from controller.seguro import router as seguro_router
from controller.locacao import router as locacao_router

app = FastAPI(title="Locadora")
init_db()

app.include_router(endereco_router)
app.include_router(locatario_router)
app.include_router(locador_router)
app.include_router(carro_router)
app.include_router(seguro_router)
app.include_router(locacao_router)

@app.get("/")
def health():
    return {"status": "ok"}
