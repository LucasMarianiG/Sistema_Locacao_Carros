from controller.generic import create_crud_router, Hooks
from model.models import Locacao, Carro, Locador, Locatario, Seguro
from model.dto import LocacaoCreate, LocacaoUpdate, LocacaoRead
from fastapi import HTTPException
from sqlmodel import Session

class LocacaoHooks(Hooks[Locacao, LocacaoCreate, LocacaoUpdate]):
    def _check_fk(self, session: Session, placa: str, locador_cpf: str, locatario_cpf: str, seguro_id: int | None):
        if not session.get(Carro, placa):
            raise HTTPException(400, "carro_placa inválida")
        if not session.get(Locador, locador_cpf):
            raise HTTPException(400, "locador_cpf inválido")
        if not session.get(Locatario, locatario_cpf):
            raise HTTPException(400, "locatario_cpf inválido")
        if seguro_id is not None and not session.get(Seguro, seguro_id):
            raise HTTPException(400, "seguro_id inválido")

    def pre_create(self, payload: LocacaoCreate, session: Session) -> None:
        self._check_fk(session, payload.carro_placa, payload.locador_cpf, payload.locatario_cpf, payload.seguro_id)

    def pre_update(self, payload: LocacaoUpdate, session: Session, obj: Locacao) -> None:
        placa = payload.carro_placa or obj.carro_placa
        locador = payload.locador_cpf or obj.locador_cpf
        locatario = payload.locatario_cpf or obj.locatario_cpf
        seguro = payload.seguro_id if payload.seguro_id is not None else obj.seguro_id
        self._check_fk(session, placa, locador, locatario, seguro)

router = create_crud_router(
    model=Locacao,
    create_schema=LocacaoCreate,
    update_schema=LocacaoUpdate,
    read_schema=LocacaoRead,
    prefix="/locacoes",
    tags=["locacoes"],
    id_type=int,
    id_param_name="id",
    hooks=LocacaoHooks(),
)
