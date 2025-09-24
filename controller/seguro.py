from controller.generic import create_crud_router, Hooks
from model.models import Seguro
from model.dto import SeguroCreate, SeguroUpdate, SeguroRead

class SeguroHooks(Hooks[Seguro, SeguroCreate, SeguroUpdate]):
    pass

router = create_crud_router(
    model=Seguro,
    create_schema=SeguroCreate,
    update_schema=SeguroUpdate,
    read_schema=SeguroRead,
    prefix="/seguros",
    tags=["seguros"],
    id_type=int,
    id_param_name="id",
)
