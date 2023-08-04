import aiohttp
import time

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


async def fetch_data(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()
        else:
            return None


async def search_ip(ip_address):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        # Fetch geolocation data
        geolocation_url = f"http://ip-api.com/json/{ip_address}"
        geolocation_data = await fetch_data(session, geolocation_url)

        # Print the IP address, country, state, city, and hosting information
        print("\n" + "=" * 10 + " " + YELLOW + f"{ip_address} " + RESET + "=" * 10)
        if geolocation_data:
            print(CYAN + f"Country: {geolocation_data.get('country', 'N/A')}")
            print(f"Region: {geolocation_data.get('regionName', 'N/A')}")
            print(f"City: {geolocation_data.get('city', 'N/A')}")
            print(f"Lat: {geolocation_data.get('lat', 'N/A')}, Lon: {geolocation_data.get('lon', 'N/A')}")
            print(f"zip: {geolocation_data.get('zip', 'N/A')}")
            print(f"Service Provider: {geolocation_data.get('isp', 'N/A')}")
            print(YELLOW)
            finish_time = time.time()
            print(f"Search completed in {finish_time - start_time:.2f} seconds." + RESET)
        else:
            print("Service not available. Try again later")
