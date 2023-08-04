import requests
import time
import json

# Load the API key and search engine ID from the config.json file
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    API_KEY = config.get("GOOGLE_SEARCH_API_KEY")
    SEARCH_ENGINE_ID = config.get("SEARCH_ENGINE_ID")
    STANDART_RESULTS = config.get("STANDART_RESULTS")


# ANSI escape sequences for colored output
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def search(query, max_results):
    if not API_KEY or not SEARCH_ENGINE_ID:
        raise ValueError("API_KEY or SEARCH_ENGINE_ID not found in config.json.")
    
    page = 1
    num_results_per_page = 10
    start_time = time.time()
    total_results = 0

    if max_results == 0:
        max_results = STANDART_RESULTS

    print(f"Searching for '{query}'...")
    while total_results < max_results:
        start = (page - 1) * num_results_per_page + 1
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
        data = requests.get(url).json()
        search_items = data.get("items")
        
        if not search_items:
            break

        num_items = len(search_items)
        remaining_results = max_results - total_results
        num_results_to_print = min(num_items, remaining_results)

        for i, search_item in enumerate(search_items[:num_results_to_print], start=start):
            try:
                long_description = search_item["pagemap"]["metatags"][0]["og:description"]
            except KeyError:
                long_description = "N/A"
            # get the page title
            title = search_item.get("title")
            # page snippet
            snippet = search_item.get("snippet")
            # alternatively, you can get the HTML snippet (bolded keywords)
            html_snippet = search_item.get("htmlSnippet")
            # extract the page url
            link = search_item.get("link")
            
            # print the results with colors
            print("="*10, YELLOW + f"Result #{i}" + RESET, "="*10)
            print(CYAN + "Title:", title + RESET)
            print("Description:", snippet)
            print(GREEN + "URL:", link + RESET, "\n")
        
        total_results += num_results_to_print
        page += 1

    finish_time = time.time()
    print(YELLOW + f"Search completed in {finish_time - start_time:.2f} seconds. Found {total_results} results." + RESET)