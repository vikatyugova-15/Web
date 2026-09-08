from fastapi import APIRouter, Request, Query, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from typing import Optional
from api.data.collections import get_all_published, get_draft, get_by_id, get_next_published

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def root(request: Request):
    published = get_all_published()
    if published:
        first_id = published[0]["id"]
        return RedirectResponse(url=f"/feed?id={first_id}")
    else:
        return templates.TemplateResponse(request=request, name="base.html", context={"title": "Нет данных"})

@router.get("/feed")
async def feed(
    request: Request,
    id: int = Query(..., description="ID услуги"),
    next: bool = Query(False, description="Следующая?"),
    full: bool = Query(False, description="Полное описание?")
):
    if next:
        service = get_next_published(id)
    else:
        service = get_by_id(id)
    if not service:
        raise HTTPException(status_code=404, detail="Услуга не найдена")
    likes_count = len(service.get("likes", []))
    return templates.TemplateResponse(
        request=request,
        name="feed.html",
        context={"service": service, "likes_count": likes_count, "full": full, "next": next}
    )

@router.get("/add")
async def add(request: Request):
    draft = get_draft()
    if not draft:
        raise HTTPException(status_code=404, detail="Черновик не найден")
    return templates.TemplateResponse(
        request=request,
        name="add.html",
        context={"draft": draft}
    )

@router.get("/catalog")
async def catalog(
    request: Request,
    filter_freq: Optional[str] = Query(None, description="Фильтр по частоте")
):
    published = get_all_published()
    if filter_freq is not None and filter_freq.strip() != "":
        try:
            freq = float(filter_freq)
            published = [s for s in published if abs(s["frequency"] - freq) < 0.001]
        except ValueError:
            pass
    for service in published:
        service["likes_count"] = len(service.get("likes", []))
    return templates.TemplateResponse(
        request=request,
        name="catalog.html",
        context={"services": published, "filter_freq": filter_freq}
    )