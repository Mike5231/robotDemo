import json
from typing import Dict, Any, List
from datetime import datetime, timedelta


def round_up_to_nearest_hour(dt):
    return (dt + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)


def create_availability_payload(
    currency_code: str = "COP",
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
    start_dt = datetime.fromisoformat(start) if start else round_up_to_nearest_hour(datetime.utcnow())
    end_dt = (datetime.fromisoformat(end) if end else round_up_to_nearest_hour(datetime.utcnow())) + timedelta(hours=2)
    return {
        "currency_code": currency_code,
        "start": start_dt.isoformat() + "Z",
        "end": end_dt.isoformat() + "Z",
        "slot_size": slot_size,
        "min_slot_size": min_slot_size,
        "operational_models_priority": operational_models_priority or ["PICK_AND_DELIVERY"],
        "express": express,
        "fallback": fallback,
        "store_reference": store_reference or 'instaleapmx-yingyangstore',
        "destination": destination or {
            "name": "Automation User",
            "address": "Automation #35-28",
            "address_two": "",
            "description": "",
            "country": "COL",
            "city": "BOGOTA D.C.",
            "state": "BOGOTA",
            "zip_code": "",
            "latitude": 4.692281,
            "longitude": -74.09083,
        },
        "job_items": job_items or [
            {
                "id": "12000229",
                "name": "ACEITE DE CANOLA DON OLIO 1000 ML",
                "barcodes": ["1024001015695"],
                "photo_url": "https://stockimages.tiendasd1.com/stockimages.tiendasd1.com/kobastockimages/IMAGENES/12000229.png",
                "unit": "UN",
                "quantity": 1,
                "sub_unit": "UN",
                "sub_quantity": 1,
                "weight": 0,
                "volume": 0,
                "price": 6690.0,
                "comment": "C44",
                "attributes": {"category": "C44"},
            },
            {
                "id": "12003475",
                "name": "CARNE MOLIDA DE RES LLANO ALTO 500 GR 90/10 GRASA CONGELADA",
                "barcodes": ["7707245266316"],
                "photo_url": "https://stockimages.tiendasd1.com/stockimages.tiendasd1.com/kobastockimages/IMAGENES/12003475.png",
                "unit": "UN",
                "quantity": 1,
                "sub_unit": "UN",
                "sub_quantity": 1,
                "weight": 0,
                "volume": 0,
                "price": 8190.0,
                "comment": "D12",
                "attributes": {"category": "D12"},
            }
        ]
    }
