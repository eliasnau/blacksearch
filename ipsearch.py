import aiohttp

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


async def fetch_data(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            return None


async def search_ip(ip_address):
    async with aiohttp.ClientSession() as session:
        # Fetch geolocation data
        geolocation_url = f"https://api.hackertarget.com/geoip/?q={ip_address}"
        geolocation_data = await fetch_data(session, geolocation_url)

        # Fetch hosting information
        hosting_url = f"https://api.hackertarget.com/hostsearch/?q={ip_address}"
        hosting_data = await fetch_data(session, hosting_url)

        # Print the IP address, country, state, city, and hosting information
        print("/n" + "=" * 10 + " " + YELLOW + f"{ip_address} " + RESET + "=" * 10)
        if geolocation_data:
            geolocation_json = dict(
                item.split(":") for item in geolocation_data.strip().split("\n")
            )
            print(CYAN + f"Country: {geolocation_json.get('Country', 'N/A')}")
            print(f"State: {geolocation_json.get('State', 'N/A')}")
            print(f"City: {geolocation_json.get('City', 'N/A')}" + RESET)
        else:
            print("Geolocation data not available.")

        if hosting_data:
            print(f"Hosting: {hosting_data}")
        else:
            print("Hosting information not available.")
