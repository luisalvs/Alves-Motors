import db
import json


def cadastrar_veiculo(modelo, marca, cor, ano):
    return db.add_veiculo(modelo, marca, cor, ano)


def listar_veiculos():
    for veiculo in db.listar_veiculos():
        print(json.dumps(veiculo, indent=4))


listar_veiculos()
