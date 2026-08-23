// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

public class Codec {
    private readonly Dictionary<string, string> urlToCode = new();
    private readonly Dictionary<string, string> codeToUrl = new();
    private int counter = 0;
    private readonly string baseUrl = "http://tinyurl.com/";

    public string Encode(string longUrl) {
        if (urlToCode.TryGetValue(longUrl, out string? existing)) {
            return existing;
        }
        string code = counter++.ToString();
        string shortUrl = baseUrl + code;
        urlToCode[longUrl] = shortUrl;
        codeToUrl[shortUrl] = longUrl;
        return shortUrl;
    }

    public string Decode(string shortUrl) {
        return codeToUrl[shortUrl];
    }
}
