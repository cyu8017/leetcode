// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

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
    val stack = scala.collection.mutable.Stack(startUrl)
    while (stack.nonEmpty) {
      for (url <- htmlParser.getUrls(stack.pop()) if host(url) == h && !seen.contains(url)) {
        seen += url
        stack.push(url)
      }
    }
    seen.toList.sorted
  }
}
