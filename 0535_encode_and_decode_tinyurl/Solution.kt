// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec {
    private val urlToCode = mutableMapOf<String, String>()
    private val codeToUrl = mutableMapOf<String, String>()
    private var counter = 0
    private val base = "http://tinyurl.com/"

    fun encode(longUrl: String): String {
        urlToCode[longUrl]?.let { return it }
        val code = counter++.toString()
        val shortUrl = base + code
        urlToCode[longUrl] = shortUrl
        codeToUrl[shortUrl] = longUrl
        return shortUrl
    }

    fun decode(shortUrl: String): String = codeToUrl[shortUrl]!!
}
