import fastapi


router = fastapi.APIRouter()


@router.get("/account")
def about():
    return {}


@router.get("/account/register")
def about():
    return {}


@router.get("/account/login")
def about():
    return {}


@router.get("/account/logout")
def about():
    return {}
