from controller.generic import create_crud_router, Hooks
from model.models import Locador, Endereco
from model.dto import LocadorCreate, LocadorUpdate, LocadorRead
from fastapi import HTTPException
from sqlmodel import Session

class LocadorHooks(Hooks[Locador, LocadorCreate, LocadorUpdate]):
    def pre_create(self, payload: LocadorCreate, session: Session) -> None:
        if not session.get(Endereco, payload.endereco_id):
            raise HTTPException(400, "endereco_id inválido")

    def pre_update(self, payload: LocadorUpdate, session: Session, obj: Locador) -> None:
        if payload.endereco_id is not None and not session.get(Endereco, payload.endereco_id):
            raise HTTPException(400, "endereco_id inválido")

router = create_crud_router(
    model=Locador,
    create_schema=LocadorCreate,
    update_schema=LocadorUpdate,
    read_schema=LocadorRead,
    prefix="/locadores",
    tags=["locadores"],
    id_type=str,           # PK = cpf
    id_param_name="cpf",
    hooks=LocadorHooks(),
)
