// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

import java.net.URI;
import java.util.*;

class HtmlParser {
    public List<String> getUrls(String url) {
        return new ArrayList<>();
    }
}

class Solution {
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        String host = URI.create(startUrl).getHost();
        Set<String> seen = new HashSet<>();
        seen.add(startUrl);
        Deque<String> stack = new ArrayDeque<>();
        stack.push(startUrl);
        while (!stack.isEmpty()) {
            String current = stack.pop();
            for (String url : htmlParser.getUrls(current)) {
                if (host.equals(URI.create(url).getHost()) && seen.add(url)) {
                    stack.push(url);
                }
            }
        }
        List<String> answer = new ArrayList<>(seen);
        Collections.sort(answer);
        return answer;
    }
}

