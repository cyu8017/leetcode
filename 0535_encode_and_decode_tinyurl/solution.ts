// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

export class Codec {
    private urlToCode = new Map<string, string>();
    private codeToUrl = new Map<string, string>();
    private counter = 0;
    private base = "http://tinyurl.com/";

    encode(longUrl: string): string {
        if (this.urlToCode.has(longUrl)) {
            return this.urlToCode.get(longUrl)!;
        }
        const code = String(this.counter++);
        const shortUrl = this.base + code;
        this.urlToCode.set(longUrl, shortUrl);
        this.codeToUrl.set(shortUrl, longUrl);
        return shortUrl;
    }

    decode(shortUrl: string): string {
        return this.codeToUrl.get(shortUrl)!;
    }
}
