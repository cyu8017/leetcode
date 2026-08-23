// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec {
    constructor() {
        this.urlToCode = new Map();
        this.codeToUrl = new Map();
        this.counter = 0;
        this.base = "http://tinyurl.com/";
    }

    encode(longUrl) {
        if (this.urlToCode.has(longUrl)) {
            return this.urlToCode.get(longUrl);
        }
        const code = String(this.counter++);
        const shortUrl = this.base + code;
        this.urlToCode.set(longUrl, shortUrl);
        this.codeToUrl.set(shortUrl, longUrl);
        return shortUrl;
    }

    decode(shortUrl) {
        return this.codeToUrl.get(shortUrl);
    }
}

module.exports = { Codec };
