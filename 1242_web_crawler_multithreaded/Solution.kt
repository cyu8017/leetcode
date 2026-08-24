// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

import java.net.URI
import java.util.Collections
import java.util.concurrent.ConcurrentHashMap
import java.util.concurrent.Executors

interface HtmlParser {
    fun getUrls(url: String): List<String>
}

class Solution {
    fun crawl(startUrl: String, htmlParser: HtmlParser): List<String> {
        val host = URI.create(startUrl).host
        val seen = ConcurrentHashMap.newKeySet<String>()
        seen.add(startUrl)
        val frontier = Collections.synchronizedList(mutableListOf(startUrl))
        val pool = Executors.newCachedThreadPool()
        try {
            while (frontier.isNotEmpty()) {
                val current = ArrayList(frontier)
                frontier.clear()
                val futures = current.map { url ->
                    pool.submit {
                        for (link in htmlParser.getUrls(url)) {
                            if (host == URI.create(link).host && seen.add(link)) frontier.add(link)
                        }
                    }
                }
                for (f in futures) f.get()
            }
        } finally {
            pool.shutdown()
        }
        return seen.sorted()
    }
}
