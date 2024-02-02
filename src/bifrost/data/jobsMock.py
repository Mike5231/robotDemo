from typing import Dict, Any, List
from datetime import datetime, timedelta


def round_up_to_nearest_hour(dt):
    return (dt + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)


def create_availability_payload(
    currency_code: str = None,
    start: str = None,
    end: str = None,
    slot_size: int = 60,
    min_slot_size: int = 60,
    operational_models_priority: List[str] = None,
    express: bool = True,
    fallback: bool = True,
    store_reference: str = None,
    destination: Dict[str, Any] = None,
    job_items: List[Dict[str, Any]] = None,
):
    start_dt = (
        datetime.fromisoformat(start)
        if start
        else round_up_to_nearest_hour(datetime.utcnow())
    )
    end_dt = (
        datetime.fromisoformat(end)
        if end
        else round_up_to_nearest_hour(datetime.utcnow())
    ) + timedelta(hours=2)

    return {
        "currency_code": currency_code or "COP",
        "start": start_dt.isoformat() + "Z",
        "end": end_dt.isoformat() + "Z",
        "slot_size": slot_size,
        "min_slot_size": min_slot_size,
        "operational_models_priority": operational_models_priority
        or ["PICK_AND_DELIVERY"],
        "express": express,
        "fallback": fallback,
        "store_reference": store_reference or "AutomationStore52",
        "destination": destination
        or {
            "name": "Automation User",
            "address": "Automation #35-28",
            "address_two": "",
            "description": "",
            "country": "COL",
            "city": "BOGOTA D.C.",
            "state": "BOGOTA",
            "zip_code": "",
            "latitude": 4.679772510806783,
            "longitude": -74.0505997728016,
        },
        "job_items": job_items or [create_item_payload()],
    }


def create_add_item(
    item_id: str = None,
    name: str = None,
    barcodes: List[str] = None,
    photo_url: str = None,
    unit: str = None,
    quantity: int = None,
    sub_unit: str = None,
    sub_quantity: int = None,
    weight: float = None,
    volume: float = None,
    price: float = None,
    comment: str = None,
    attributes: Dict[str, Any] = None,
):
    return {
        "item_to_add": create_item_payload(
            item_id,
            name,
            barcodes,
            photo_url,
            unit,
            quantity,
            sub_unit,
            sub_quantity,
            weight,
            volume,
            price,
            comment,
            attributes,
        )
    }


def create_item_payload(
    item_id: str = None,
    name: str = None,
    barcodes: List[str] = None,
    photo_url: str = None,
    unit: str = None,
    quantity: int = None,
    sub_unit: str = None,
    sub_quantity: int = None,
    weight: float = None,
    volume: float = None,
    price: float = None,
    comment: str = None,
    attributes: Dict[str, Any] = None,
) -> Dict[str, Any]:
    return {
        "id": item_id or "12000229",
        "name": name or "ACEITE DE CANOLA DON OLIO 1000 ML",
        "barcodes": barcodes or ["1024001015695"],
        "photo_url": photo_url
        or "https://stockimages.tiendasd1.com/"
        "stockimages.tiendasd1.com/kobastockimages/"
        "IMAGENES/12000229.png",
        "unit": unit or "UN",
        "quantity": quantity or 1,
        "sub_unit": sub_unit or "UN",
        "sub_quantity": sub_quantity or 1,
        "weight": weight or 0.0,
        "volume": volume or 1,
        "price": price or 66.55,
        "comment": comment or "C44",
        "attributes": attributes or {"category": "C44"},
    }
