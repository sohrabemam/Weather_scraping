from requests_html import HTMLSession

s = HTMLSession()

try:
    query = input('Enter Location to check weather:').strip()
    if not query.isalpha():
        raise ValueError("Please enter a valid location name.")

    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers = {'User-Agent': 'Mozilla/5.0 \
                              (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                               Chrome/127.0.0.0 Safari/537.36'})

    temp = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    desc = r.html.find('div.VQF4g', first=True).find('div.wob_dcp', first=True).text

    print(f"{query}: {temp} {unit}, {desc}")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print("An error occurred:", e)
