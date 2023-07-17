from pydantic import Field, BaseModel


class TariffDTORequest(BaseModel):
    cargo_type: str = Field(max_length=30)
    rate: float = Field(ge=0)
