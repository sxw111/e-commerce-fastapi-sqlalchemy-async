from fastapi import APIRouter, status

from app.api.deps import SessionDep
from app.models.db.models import Brand
from app.models.schemas.brand import BrandCreate, BrandOut


router = APIRouter()


@router.post("/", response_model=BrandOut, status_code=status.HTTP_201_CREATED)
async def create_brand(db: SessionDep, brand: BrandCreate) -> BrandOut:
    new_brand = Brand(**brand.model_dump())

    db.add(new_brand)
    await db.commit()
    await db.refresh(new_brand)

    return new_brand
