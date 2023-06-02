from fastapi import APIRouter, Depends

from app.schemas.sample_schema import SampleBase, SampleCreate
from app.services import SampleService
from app.services.test_class_service import TestClassService
from app.services.test_service import print_sample_text

router = APIRouter(
    prefix="/samples",
    tags=["samples"],
    dependencies=[
        Depends(print_sample_text),
        Depends(TestClassService),
        Depends(SampleService),
    ],
)


@router.get("/")
async def index(test_class_service: TestClassService = Depends(TestClassService)):
    print(test_class_service.test_method())
    return [{"name": "sample1"}, {"name": "sample2"}]


@router.get("/{sample_id}")
async def show(sample_id: int, sample_service: SampleService = Depends(SampleService)):
    res = await sample_service.findById(sample_id)
    return res


@router.post("/", response_model=SampleBase)
async def store(body: SampleCreate):
    return body
