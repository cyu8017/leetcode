// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec {
  private val urlToCode = scala.collection.mutable.Map.empty[String, String]
  private val codeToUrl = scala.collection.mutable.Map.empty[String, String]
  private var counter = 0
  private val base = "http://tinyurl.com/"

  def encode(longUrl: String): String = {
    urlToCode.get(longUrl) match {
      case Some(existing) => existing
      case None =>
        val code = counter.toString
        counter += 1
        val shortUrl = base + code
        urlToCode(longUrl) = shortUrl
        codeToUrl(shortUrl) = longUrl
        shortUrl
    }
  }

  def decode(shortUrl: String): String = codeToUrl(shortUrl)
}
