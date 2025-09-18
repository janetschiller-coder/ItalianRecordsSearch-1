from fastapi import FastAPI, Query
from typing import Optional
import httpx
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Italian Genealogy API is running"}

@app.get("/search-records")
async def search_records(
    location: str,
    surname: Optional[str] = None,
    given_name: Optional[str] = None,
    year_range: Optional[str] = None
):
    base_url = "https://antenati.cultura.gov.it/search/"
    query_pa_
from fastapi import FastAPI, Query
from typing import Optional
import httpx
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Italian Genealogy API is running"}

@app.get("/search-records")
async def search_records(
    location: str,
    surname: Optional[str] = None,
    given_name: Optional[str] = None,
    year_range: Optional[str] = None
):
    base_url = "https://antenati.cultura.gov.it/search/"
    query_parts = [location]

    if surname:
        query_parts.append(surname)
    if given_name:
        query_parts.append(given_name)
    if year_range:
        query_parts.append(year_range)

    search_query = "+".join(query_parts)
    search_url = f"{base_url}?q={search_query}"

    async with httpx.AsyncClient() as client:
        response = await client.get(search_url)
        soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for item in soup.select(".search-result"):
        title = item.select_one(".search-result-title")
        link = item.select_one("a")
        description = item.select_one(".search-result-description")
        results.append({
            "title": title.get_text(strip=True) if title else "No title",
            "link": link["href"] if link else "",
            "description": description.get_text(strip=True) if description else "No description"
        })

    return {"results": results}
