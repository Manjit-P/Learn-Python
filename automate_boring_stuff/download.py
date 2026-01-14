import requests
response = requests.get('https://gutenberg.org/cache/epub/2701/pg2701.txt')
response.raise_for_status()
with open('RomeoAndJuliet.txt', 'wb') as f:
    for chunk in response.iter_content(100_000):
        f.write(chunk)