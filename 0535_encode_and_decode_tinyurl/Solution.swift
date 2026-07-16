// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec {
    private var urlToCode: [String: String] = [:]
    private var codeToUrl: [String: String] = [:]
    private var counter = 0
    private let base = "http://tinyurl.com/"

    func encode(_ longUrl: String) -> String {
        if let existing = urlToCode[longUrl] {
            return existing
        }
        let code = String(counter)
        counter += 1
        let shortUrl = base + code
        urlToCode[longUrl] = shortUrl
        codeToUrl[shortUrl] = longUrl
        return shortUrl
    }

    func decode(_ shortUrl: String) -> String {
        return codeToUrl[shortUrl]!
    }
}
