import asyncio
import aiohttp

import os

async def get_html(session, url):
    async with session.get(url, ssl=False) as res:
        website_name = f'{os.path.basename(url)}'

        async with aiofiles.open('output.csv', 'wb') as f:
            

async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await get_html(session, url)
