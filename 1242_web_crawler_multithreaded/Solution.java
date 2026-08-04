// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

import java.net.URI;
import java.util.*;
import java.util.concurrent.*;

class HtmlParser {
    public List<String> getUrls(String url) {
        return new ArrayList<>();
    }
}

class Solution {
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        String host = URI.create(startUrl).getHost();
        Set<String> seen = ConcurrentHashMap.newKeySet();
        seen.add(startUrl);
        List<String> frontier = Collections.synchronizedList(new ArrayList<>(List.of(startUrl)));
        ExecutorService pool = Executors.newCachedThreadPool();
        try {
            while (!frontier.isEmpty()) {
                List<String> current = new ArrayList<>(frontier);
                frontier.clear();
                List<Future<?>> futures = new ArrayList<>();
                for (String url : current) {
                    futures.add(pool.submit(() -> {
                        for (String link : htmlParser.getUrls(url)) {
                            if (host.equals(URI.create(link).getHost()) && seen.add(link)) {
                                frontier.add(link);
                            }
                        }
                    }));
                }
                for (Future<?> f : futures) {
                    try {
                        f.get();
                    } catch (Exception e) {
                        throw new RuntimeException(e);
                    }
                }
            }
        } finally {
            pool.shutdown();
        }
        List<String> answer = new ArrayList<>(seen);
        Collections.sort(answer);
        return answer;
    }
}

