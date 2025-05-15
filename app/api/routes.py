from fastapi import APIRouter

router = APIRouter()

@router.get('/greeting')
async def get_greeting():
    return {"message": "Hello from the API!"}