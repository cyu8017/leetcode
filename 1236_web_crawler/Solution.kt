// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

import java.net.URI

interface HtmlParser {
    fun getUrls(url: String): List<String>
}

class Solution {
    fun crawl(startUrl: String, htmlParser: HtmlParser): List<String> {
        val host = URI.create(startUrl).host
        val seen = linkedSetOf(startUrl)
        val stack = ArrayDeque<String>()
        stack.addLast(startUrl)
        while (stack.isNotEmpty()) {
            val current = stack.removeLast()
            for (url in htmlParser.getUrls(current)) {
                if (host == URI.create(url).host && seen.add(url)) stack.addLast(url)
            }
        }
        return seen.sorted()
    }
}
