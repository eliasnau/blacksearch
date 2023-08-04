import argparse

import googlesearch

def main():
    parser = argparse.ArgumentParser(description="BlackSearch - A custom search tool")
    parser.add_argument("--google", action="store_true", help="Use Google Custom Search API")
    parser.add_argument("--username", action="store_true", help="Perform social media username search")
    parser.add_argument("-q", "--query", help="The search query")
    parser.add_argument("-s","--site" ,help="Search only on a spesific site")
    parser.add_argument("-t","--type" ,help="Search only on a spesific site")
    parser.add_argument("-r", "--max_results", type=int, default=10, help="Maximum number of results (default: 10)")

    args = parser.parse_args()

    if args.google and args.query:
        search_query = args.query
        if args.site:
            search_query = 'site:"' + args.site + '" ' + args.query
        if args.type:
            search_query = 'filetype:"' + args.type + '" ' + search_query

        if args.max_results:
            googlesearch.search(search_query, args.max_results)
        else:
            max_results = 0
            googlesearch.search(search_query, max_results)
        
    # elif args.username and args.query:
    #     username_results = username.search_username(args.query)
    #     for app, data in username_results.items():
    #         print(f"Results for {app}:")
    #         print(json.dumps(data, indent=2))
    else:
        print("Unsupported search engine or invalid arguments. Please use --google for regular search or --username to perform social media username search.")

if __name__ == "__main__":
    main()
