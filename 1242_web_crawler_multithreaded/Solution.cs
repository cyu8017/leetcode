// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

public class HtmlParser {
    public virtual IList<string> GetUrls(string url) => new List<string>();
}

public class Solution {
    public IList<string> Crawl(string startUrl, HtmlParser htmlParser) {
        string host = new Uri(startUrl).Host;
        var seen = new ConcurrentDictionary<string, byte>();
        seen.TryAdd(startUrl, 0);
        var frontier = new List<string> { startUrl };
        while (frontier.Count > 0) {
            var next = new ConcurrentBag<string>();
            Parallel.ForEach(frontier, url => {
                foreach (string link in htmlParser.GetUrls(url)) {
                    if (new Uri(link).Host == host && seen.TryAdd(link, 0)) {
                        next.Add(link);
                    }
                }
            });
            frontier = next.ToList();
        }
        return seen.Keys.OrderBy(x => x).ToList();
    }
}
