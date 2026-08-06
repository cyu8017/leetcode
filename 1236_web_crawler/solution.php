<?php
// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

class Solution {
    /**
     * @param String $startUrl
     * @param HtmlParser $htmlParser
     * @return String[]
     */
    function crawl($startUrl, $htmlParser) {
        $host = parse_url($startUrl, PHP_URL_HOST);
        $seen = [$startUrl => true];
        $stack = [$startUrl];
        while (!empty($stack)) {
            $cur = array_pop($stack);
            foreach ($htmlParser->getUrls($cur) as $url) {
                if (parse_url($url, PHP_URL_HOST) === $host && !isset($seen[$url])) {
                    $seen[$url] = true;
                    $stack[] = $url;
                }
            }
        }
        $ans = array_keys($seen);
        sort($ans);
        return $ans;
    }
}
