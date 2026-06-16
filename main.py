from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="API Inova Lab - Inventário Maker")

class ComponenteSchema(BaseModel):
    nome: str = Field(..., min_length=2, description="Nome do componente maker")
    quantidade: int = Field(..., ge=0, description="Quantidade em estoque (deve ser maior ou igual a zero)")
    categoria: str = Field(..., description="Categoria do item (ex: Atuadores, Microcontroladores)")
    estado_conservacao: str = Field(..., description="Estado de conservação do item (ex: Ótimo, Bom, Ruim)")

estoque_laboratorio = [
    {"id": 1, "nome": "Arduino Sensor Shield", "quantidade": 15, "categoria": "Placas de Expansão", "estado_conservacao": "Ótimo"},
    {"id": 2, "nome": "Micro Servo Motor SG90", "quantidade": 42, "categoria": "Atuadores", "estado_conservacao": "Bom"},
    {"id": 3, "nome": "Esteira em Acrílico", "quantidade": 2, "categoria": "Mecânica", "estado_conservacao": "Ruim"}
]

@app.get("/")
def raiz():
    return {"mensagem": "API do Laboratório Maker operante. Acesse /docs para ver a documentação."}

@app.get("/componentes")
def listar_componentes():
    return estoque_laboratorio

@app.post("/componentes", status_code=201)
def adicionar_componente(novo_componente: ComponenteSchema):
    if estoque_laboratorio:
        maior_id = max(item["id"] for item in estoque_laboratorio)
        novo_id = maior_id + 1
    else:
        novo_id = 1

    componente_dict = novo_componente.model_dump()
    componente_dict["id"] = novo_id
    estoque_laboratorio.append(componente_dict)
    return {"mensagem": "Componente adicionado com sucesso!", "componente": componente_dict}

@app.put("/componentes/{componente_id}")
def atualizar_componente(componente_id: int, dados_atualizados: ComponenteSchema):
    for item in estoque_laboratorio:
        if item["id"] == componente_id:
            item["nome"] = dados_atualizados.nome
            item["quantidade"] = dados_atualizados.quantidade
            item["categoria"] = dados_atualizados.categoria
            item["estado_conservacao"] = dados_atualizados.estado_conservacao
            return {"mensagem": "Componente atualizado com sucesso!", "componente": item}

    raise HTTPException(status_code=404, detail="Componente não encontrado no laboratório.")

@app.delete("/componentes/{componente_id}")
def remover_componente(componente_id: int):
    for index, item in enumerate(estoque_laboratorio):
        if item["id"] == componente_id:
            estoque_laboratorio.pop(index)
            return {"mensagem": f"Componente com ID {componente_id} foi removido do estoque."}

    raise HTTPException(status_code=404, detail="Componente não encontrado no laboratório.")