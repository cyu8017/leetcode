// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public IList<string> PartitionString(string s) {
        var vis = new HashSet<string>();
        var ans = new List<string>();
        var t = new StringBuilder();
        foreach (char c in s) {
            t.Append(c);
            string cur = t.ToString();
            if (!vis.Contains(cur)) {
                vis.Add(cur);
                ans.Add(cur);
                t.Clear();
            }
        }
        return ans;
    }
}
