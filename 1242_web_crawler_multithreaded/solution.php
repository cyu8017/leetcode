<?php
// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

class Solution {
    /**
     * @param String $startUrl
     * @param HtmlParser $htmlParser
     * @return String[]
     */
    function crawl($startUrl, $htmlParser) {
        $host = parse_url($startUrl, PHP_URL_HOST);
        $seen = [$startUrl => true];
        $frontier = [$startUrl];
        while (!empty($frontier)) {
            $next = [];
            foreach ($frontier as $cur) {
                foreach ($htmlParser->getUrls($cur) as $url) {
                    if (parse_url($url, PHP_URL_HOST) === $host && !isset($seen[$url])) {
                        $seen[$url] = true;
                        $next[] = $url;
                    }
                }
            }
            $frontier = $next;
        }
        $ans = array_keys($seen);
        sort($ans);
        return $ans;
    }
}
