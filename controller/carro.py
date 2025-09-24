from controller.generic import create_crud_router, Hooks
from model.models import Carro
from model.dto import CarroCreate, CarroUpdate, CarroRead

class CarroHooks(Hooks[Carro, CarroCreate, CarroUpdate]):
    pass

router = create_crud_router(
    model=Carro,
    create_schema=CarroCreate,
    update_schema=CarroUpdate,
    read_schema=CarroRead,
    prefix="/carros",
    tags=["carros"],
    id_type=str,           # PK = placa
    id_param_name="placa",
)
