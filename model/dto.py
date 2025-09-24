from model.models import User, Post
from typing import List, Optional
from sqlmodel import SQLModel, Field
from datetime import date
#------------------DTO para Endereco--------------
class EnderecoBase(SQLModel):
    logradouro: str
    numero: Optional[str] = None
    bairro: str
    cidade: str
    estado: str
    cep: str
    complemento: Optional[str] = None

class EnderecoCreate(EnderecoBase):
    """Usado no POST (entrada): não inclui id."""
    pass

class EnderecoUpdate(SQLModel):
    """Usado no PUT/PATCH (entrada): todos opcionais."""
    logradouro: Optional[str] = None
    numero: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    cep: Optional[str] = None
    complemento: Optional[str] = None

class EnderecoRead(EnderecoBase):
    """Usado nas respostas (saída)"""
    id: int

#------------------DTO para locatario--------------

class LocatarioBase(SQLModel):
    cpf: str
    nome: str
    telefone: Optional[str] = None
    endereco_id: Optional[int] = None
    cnh: str

class LocatarioCreate(LocatarioBase):
    """Usado no POST (entrada): não inclui relacionamentos."""
    pass
class LocatarioUpdate(SQLModel):
    """Usado no PUT/PATCH (entrada): todos opcionais."""
    cpf: Optional[str] = None
    nome: Optional[str] = None
    telefone: Optional[str] = None
    endereco_id: Optional[int] = None
    cnh: Optional[str] = None

class LocatarioRead(SQLModel):
    """Saída nas respostas"""
    cpf: str
    nome: str
    telefone: Optional[str] = None
    cnh: str
    endereco_id: int

 #------------------DTO para locador--------------   

class LocadorBase(SQLModel):
    cpf: str               
    nome: str
    telefone: Optional[str] = None
    salario: float
    endereco_id: int       

class LocadorCreate(LocadorBase):
    """Entrada no POST (criação)."""
    pass

class LocadorUpdate(SQLModel):
    """Entrada no PUT/PATCH (atualização parcial)."""
    nome: Optional[str] = None
    telefone: Optional[str] = None
    salario: Optional[float] = None
    endereco_id: Optional[int] = None
    # (cpf fica fora do corpo: é a PK e vai na URL)

class LocadorRead(SQLModel):
    """Saída (respostas da API)."""
    cpf: str
    nome: str
    telefone: Optional[str] = None
    salario: float
    endereco_id: int

#------------------DTO para carro--------------
class CarroBase(SQLModel):
    placa: str
    modelo: str
    ano: int
    cor: str

class CarroCreate(CarroBase):
    """Usado no POST (entrada): não inclui relacionamentos."""
    pass

class CarroUpdate(SQLModel):
    """Usado no PUT/PATCH (entrada): todos opcionais."""
    modelo: Optional[str] = None
    ano: Optional[int] = None
    cor: Optional[str] = None

class CarroRead(CarroBase):
    """Usado nas respostas (saída)"""
    placa: str
    modelo: str
    ano: int
    cor: str

#------------------DTO para seguro--------------
class SeguroBase(SQLModel):
    nome: str
    categoria: str
    cobertura: str
    valor: float

class SeguroCreate(SeguroBase):
    """Usado no POST (entrada): não inclui relacionamentos."""
    pass

class SeguroUpdate(SQLModel):
    """Usado no PUT/PATCH (entrada): todos opcionais."""
    nome: Optional[str] = None
    categoria: Optional[str] = None
    cobertura: Optional[str] = None
    valor: Optional[float] = None

class SeguroRead(SeguroBase):
    """Usado nas respostas (saída)"""
    id: int

#------------------DTO para locacao--------------
class LocacaoBase(SQLModel):
    data_inicio: date
    data_fim: Optional[date] = None
    
    carro_placa: str
    locador_cpf: str
    locatario_cpf: str
    seguro_id: Optional[int] = None

class LocacaoCreate(LocacaoBase):
    """Entrada no POST: todos os campos necessários para criar."""
    pass

class LocacaoUpdate(SQLModel):
    """Entrada no PUT/PATCH: atualização parcial."""
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    carro_placa: Optional[str] = None
    locador_cpf: Optional[str] = None
    locatario_cpf: Optional[str] = None
    seguro_id: Optional[int] = None

class LocacaoRead(SQLModel):
    """Saída (respostas da API)."""
    id: int
    data_inicio: date
    data_fim: Optional[date] = None
    carro_placa: str
    locador_cpf: str
    locatario_cpf: str
    seguro_id: Optional[int] = None