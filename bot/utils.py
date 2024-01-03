import aiohttp

from bot.config import API_ADDRESS, API_PORT


async def get_weather_data(city: str) -> dict:
    url = f'http://{API_ADDRESS}:{API_PORT}/weather'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params={'city': city}) as response:
                status = response.status
                if status == 200:
                    return await response.json()
                elif status == 404:
                    return {'error': f'Город "{city}" не найден. Укажите правильное наименование города'}
                elif status == 500:
                    return {'error': 'Ошибка на стороне сервера. Попробуйте повторить запрос позже'}
    except aiohttp.ClientConnectorError:
        return {'error': 'Ошибка соединения с сервером'}

