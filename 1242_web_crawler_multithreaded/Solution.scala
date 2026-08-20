// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

trait HtmlParser {
  def getUrls(url: String): List[String]
}

object Solution {
  def crawl(startUrl: String, htmlParser: HtmlParser): List[String] = {
    def host(url: String): String = {
      val without = url.stripPrefix("http://")
      without.takeWhile(_ != '/')
    }
    val h = host(startUrl)
    val seen = scala.collection.mutable.Set(startUrl)
    var frontier = List(startUrl)
    while (frontier.nonEmpty) {
      val next = scala.collection.mutable.ListBuffer.empty[String]
      for (urls <- frontier.map(htmlParser.getUrls); url <- urls if host(url) == h && !seen.contains(url)) {
        seen += url
        next += url
      }
      frontier = next.toList
    }
    seen.toList.sorted
  }
}
