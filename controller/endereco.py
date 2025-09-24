from controller.generic import create_crud_router, Hooks
from model.models import Endereco
from model.dto import EnderecoCreate, EnderecoUpdate, EnderecoRead

class EnderecoHooks(Hooks[Endereco, EnderecoCreate, EnderecoUpdate]):
    pass  # nenhuma regra especial por enquanto

router = create_crud_router(
    model=Endereco,
    create_schema=EnderecoCreate,
    update_schema=EnderecoUpdate,
    read_schema=EnderecoRead,
    prefix="/enderecos",
    tags=["enderecos"],
    id_type=int,
    id_param_name="id",
)
