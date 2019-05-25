import aiohttp


async def index(request):
    return aiohttp.web.Response('ok')
