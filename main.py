from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 10},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 10},
    3: {"item": "garrafa 500ml", "preco_unitario": 10, "quantidade": 10},
    4: {"item": "KS", "preco_unitario": 3, "quantidade": 10},
    5: {"item": "garrafa 1L", "preco_unitario": 8, "quantidade": 10},
}

@app.get("/")
def home():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"error": "Venda não encontrada"}