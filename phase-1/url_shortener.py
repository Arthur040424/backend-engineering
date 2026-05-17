url_map = {"aaa111": "https://google.com", "bbb222": "https://github.com", "ccc333": "https://chatgpt.com"}

def get_url(short_code):
    return url_map.get(short_code, "URL Not Found")

print(get_url("aaa111"))
print(get_url("bbb222"))
print(get_url("ccc333"))
print(get_url("zzz999"))