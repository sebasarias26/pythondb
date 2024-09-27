from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosAPP import Usuario, Gasto, Categoria, MetodoPago
from app.api.routes import rutas
from starlette.responses import RedirectResponse

#variable para administrar la aplicación
app=FastAPI()

#Activo el api
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)