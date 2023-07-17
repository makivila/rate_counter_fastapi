import datetime
from typing import Any, Annotated
from fastapi import APIRouter, HTTPException, Query
from app.dto import TariffDTORequest
from app.models import Tariff


router = APIRouter()


@router.post("/tariffs")
async def load_tariffs(
    tariff_dtos_by_date: dict[datetime.date, list[TariffDTORequest]]
):
    for date, tariff_dto_list in tariff_dtos_by_date.items():
        for tariff_dto in tariff_dto_list:
            await Tariff.create(
                cargo_type=tariff_dto.cargo_type,
                rate=tariff_dto.rate,
                date=date,
            )
    return {"result": "tariffs successfully loaded"}


@router.get("/cost")
async def get_cost(
    declared_value: Annotated[float, Query(ge=0)],
    cargo_type: str,
    date: datetime.date,
):
    tariff = await Tariff.get_or_none(date=date, cargo_type=cargo_type)

    if not tariff:
        raise HTTPException(status_code=404, detail="tariff not found")

    return {"result": f"{declared_value * tariff.rate}"}
