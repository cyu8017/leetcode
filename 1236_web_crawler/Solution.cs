// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

using System;
using System.Collections.Generic;
using System.Linq;

public class HtmlParser {
    public virtual IList<string> GetUrls(string url) => new List<string>();
}

public class Solution {
    public IList<string> Crawl(string startUrl, HtmlParser htmlParser) {
        string host = new Uri(startUrl).Host;
        var seen = new HashSet<string> { startUrl };
        var stack = new Stack<string>();
        stack.Push(startUrl);
        while (stack.Count > 0) {
            string current = stack.Pop();
            foreach (string url in htmlParser.GetUrls(current)) {
                if (new Uri(url).Host == host && seen.Add(url)) {
                    stack.Push(url);
                }
            }
        }
        return seen.OrderBy(x => x).ToList();
    }
}
