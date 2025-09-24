from controller.generic import create_crud_router, Hooks
from model.models import Locatario, Endereco
from model.dto import LocatarioCreate, LocatarioUpdate, LocatarioRead
from fastapi import HTTPException
from sqlmodel import Session

class LocatarioHooks(Hooks[Locatario, LocatarioCreate, LocatarioUpdate]):
    def pre_create(self, payload: LocatarioCreate, session: Session) -> None:
        if not session.get(Endereco, payload.endereco_id):
            raise HTTPException(400, "endereco_id inválido")

    def pre_update(self, payload: LocatarioUpdate, session: Session, obj: Locatario) -> None:
        if payload.endereco_id is not None and not session.get(Endereco, payload.endereco_id):
            raise HTTPException(400, "endereco_id inválido")

router = create_crud_router(
    model=Locatario,
    create_schema=LocatarioCreate,
    update_schema=LocatarioUpdate,
    read_schema=LocatarioRead,
    prefix="/locatarios",
    tags=["locatarios"],
    id_type=str,           # PK = cpf
    id_param_name="cpf",
    hooks=LocatarioHooks(),
)
