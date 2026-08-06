// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

use std::collections::HashSet;

trait HtmlParser {
    fn get_urls(&self, url: String) -> Vec<String>;
}

impl Solution {
    pub fn crawl(start_url: String, html_parser: &impl HtmlParser) -> Vec<String> {
        fn host_of(url: &str) -> &str {
            let u = url.strip_prefix("http://").unwrap_or(url);
            u.split('/').next().unwrap_or(u)
        }
        let host = host_of(&start_url).to_string();
        let mut seen = HashSet::new();
        seen.insert(start_url.clone());
        let mut frontier = vec![start_url];
        while !frontier.is_empty() {
            let mut next = Vec::new();
            for cur in frontier {
                for url in html_parser.get_urls(cur) {
                    if host_of(&url) == host && seen.insert(url.clone()) {
                        next.push(url);
                    }
                }
            }
            frontier = next;
        }
        let mut ans: Vec<String> = seen.into_iter().collect();
        ans.sort();
        ans
    }
}
