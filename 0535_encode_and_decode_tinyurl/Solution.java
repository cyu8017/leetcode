// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

import java.util.HashMap;
import java.util.Map;

class Codec {
    private final Map<String, String> urlToCode = new HashMap<>();
    private final Map<String, String> codeToUrl = new HashMap<>();
    private int counter = 0;
    private final String base = "http://tinyurl.com/";

    public String encode(String longUrl) {
        if (urlToCode.containsKey(longUrl)) {
            return urlToCode.get(longUrl);
        }
        String code = String.valueOf(counter++);
        String shortUrl = base + code;
        urlToCode.put(longUrl, shortUrl);
        codeToUrl.put(shortUrl, longUrl);
        return shortUrl;
    }

    public String decode(String shortUrl) {
        return codeToUrl.get(shortUrl);
    }
}
