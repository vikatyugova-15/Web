
services_db = [
    {
        "id": 1,
        "title": "Хроника",
        "description": "Документальное повествование о реальных событиях в хронологическом порядке. Обычно включает даты, имена и факты.",
        "frequency": 0.72,
        "confidence": 0.89,
        "image_key": "http://localhost:9000/genre-assets/hronica.jpg",
        "video_key": "http://localhost:9000/genre-assets/video.mp4",
        "likes": [101, 102, 103, 104, 105],
        "status": "published"
    },
    {
        "id": 2,
        "title": "Житие",
        "description": "Жизнеописание святого, описание подвигов, чудес и духовного пути.",
        "frequency": 0.65,
        "confidence": 0.78,
        "image_key": "http://localhost:9000/genre-assets/zitie.jpg",
        "video_key": "http://localhost:9000/genre-assets/video.mp4",
        "likes": [201, 202, 203],
        "status": "published"
    },
    {
        "id": 3,
        "title": "Договор",
        "description": "Юридический документ, фиксирующий соглашение между сторонами с перечнем условий и обязательств.",
        "frequency": 0.81,
        "confidence": 0.95,
        "image_key": "http://localhost:9000/genre-assets/dogovor.jpg",
        "video_key": "http://localhost:9000/genre-assets/video.mp4",
        "likes": [301, 302, 303, 304, 305, 306],
        "status": "published"
    },
    {
        "id": 4,
        "title": "Поэма",
        "description": "Лирическое или эпическое стихотворное произведение с ритмом, рифмой и образным языком.",
        "frequency": 0.58,
        "confidence": 0.67,
        "image_key": "http://localhost:9000/genre-assets/poem.jpg",
        "video_key": "http://localhost:9000/genre-assets/video.mp4",
        "likes": [401, 402],
        "status": "published"
    },
    
    {
        "id": 5,
        "title": "Черновик: Новый жанр",
        "description": "Пример черновика для заполнения",
        "frequency": 0.50,
        "confidence": 0.50,
        "image_key": "http://localhost:9000/genre-assets/draft.jpg",
        "video_key": "http://localhost:9000/genre-assets/video.mp4",
        "likes": [],
        "status": "draft"
    },
    
    {
        "id": 6,
        "title": "Устаревший жанр",
        "description": "Больше не используется",
        "frequency": 0.30,
        "confidence": 0.40,
        "image_key": "http://localhost:9000/genre-assets/deleted.jpg",
        "video_key": "http://localhost:9000/genre-assets/video.mp4",
        "likes": [],
        "status": "deleted"
    }
]

def get_all_published():
    return [s for s in services_db if s["status"] == "published"]

def get_draft():
    drafts = [s for s in services_db if s["status"] == "draft"]
    return drafts[0] if drafts else None

def get_by_id(service_id):
    for s in services_db:
        if s["id"] == service_id:
            return s
    return None

def get_next_published(current_id):
    published = get_all_published()
    if not published:
        return None
    try:
        index = next(i for i, s in enumerate(published) if s["id"] == current_id)
    except StopIteration:
        return published[0]
    next_index = (index + 1) % len(published)
    return published[next_index]