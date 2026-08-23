// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

using System.Collections.Generic;

public class Solution {
    public IList<string> SubdomainVisits(string[] cpdomains) {
        var counts = new Dictionary<string, int>();
        foreach (string item in cpdomains) {
            int space = item.IndexOf(' ');
            int count = int.Parse(item.Substring(0, space));
            string domain = item.Substring(space + 1);
            while (true) {
                if (!counts.ContainsKey(domain)) counts[domain] = 0;
                counts[domain] += count;
                int dot = domain.IndexOf('.');
                if (dot < 0) break;
                domain = domain.Substring(dot + 1);
            }
        }
        var ans = new List<string>();
        foreach (var kv in counts) ans.Add(kv.Value + " " + kv.Key);
        return ans;
    }
}
