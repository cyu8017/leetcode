# LeetCode 0535 - Encode and Decode TinyURL
# https://leetcode.com/problems/encode-and-decode-tinyurl/


class Codec:
    def __init__(self) -> None:
        self._url_to_code: dict[str, str] = {}
        self._code_to_url: dict[str, str] = {}
        self._counter = 0
        self._base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        if longUrl in self._url_to_code:
            return self._url_to_code[longUrl]
        code = str(self._counter)
        self._counter += 1
        short_url = self._base + code
        self._url_to_code[longUrl] = short_url
        self._code_to_url[short_url] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        return self._code_to_url[shortUrl]
