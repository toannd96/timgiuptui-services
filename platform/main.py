from constants import PubSubTopicIds
from event_handler import pubsub_publish
from fastapi import FastAPI, HTTPException, status
from logs import logger
from models import Source
from provider import Provider

app = FastAPI(
    version="0.1.0",
    title="[timgiuptui] Platform Service",
    description="Platform service documentation",
)

provider = Provider()


@app.get("/", status_code=status.HTTP_200_OK)
def health():
    return "OK"


@app.get("/topics", status_code=status.HTTP_200_OK)
def get_topics():
    try:
        topics = provider.get_topics()
        return topics
    except Exception as e:
        logger.error(e)
        return []


@app.get("/editors", status_code=status.HTTP_200_OK)
def get_editors():
    try:
        editors = provider.get_editors()
        return editors
    except Exception as e:
        logger.error(e)
        return []


@app.post("/crawler/sources", status_code=status.HTTP_200_OK)
def get_sources():
    sources: list[Source] = []
    try:
        sources = provider.get_sources()
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Cannot get sources",
        )
    sources_json = [source.dict() for source in sources]
    pubsub_publish(topic=PubSubTopicIds.START_CRAWLING, data=sources_json)
    return sources_json
