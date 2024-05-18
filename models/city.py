from .base_model import BaseModel

class City(BaseModel):
    """City This class inherent for BaseModel.
    Attributes:
        name string - empty strign (will become name of the city)
            state_id - empty string (it will be the state.id from state class)
    """
    state_id = ""
    name = ""