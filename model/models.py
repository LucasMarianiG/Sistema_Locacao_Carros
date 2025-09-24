from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from __future__ import annotations

class Carro(SQLModel, table=True):
    modelo :str = Field(index=True)
    ano :int
    placa :str = Field(primary_key=True)
    cor :str
    locacoes: List["Locacao"] = Relationship(back_populates="carro")

class Pessoa(SQLModel, table=True):
    cpf: str = Field(primary_key=True)
    nome: str = Field(index=True)
    telefone: Optional[str] = None
    endereco_id: Optional[int] = Field(default=None, foreign_key="endereco.id")
    endereco: Optional["Endereco"] = Relationship(back_populates="pessoas")


class Endereco(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    logradouro: str = Field(index=True)
    numero: Optional[str] = None
    bairro: str
    cidade: str
    estado: str
    cep: str = Field(index=True)
    complemento: Optional[str] = None
    pessoas: List["Pessoa"] = Relationship(back_populates="endereco")


class Seguro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(index=True)
    categoria: str
    cobertura: str
    valor: float
    locacoes: List["Locacao"] = Relationship(back_populates="seguro")

class Locador(Pessoa, table=True):
    salario : float
    locacoes: List["Locacao"] = Relationship(back_populates="locador")

class Locatario(Pessoa, table=True):
    cnh : str
    locacoes: List["Locacao"] = Relationship(back_populates="locatario")

class Locacao(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    data_inicio: date
    data_fim: Optional[date] = None

    # foreign keys
    carro_placa: str = Field(foreign_key="carro.placa")
    locador_cpf: str = Field(foreign_key="locador.cpf")
    locatario_cpf: str = Field(foreign_key="locatario.cpf")
    seguro_id: Optional[int] = Field(default=None, foreign_key="seguro.id")

    # relacionamentos
    carro: Carro = Relationship(back_populates="locacoes")
    locador: Locador = Relationship(back_populates="locacoes")
    locatario: Locatario = Relationship(back_populates="locacoes")
    seguro: Optional[Seguro] = Relationship(back_populates="locacoes")
    

