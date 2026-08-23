// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

using System.Collections.Generic;

public class Solution {
    public long DistinctNames(string[] ideas) {
        var groups = new HashSet<string>[26];
        for (int i = 0; i < 26; i++) groups[i] = new HashSet<string>();
        foreach (var idea in ideas) groups[idea[0] - 'a'].Add(idea.Substring(1));
        long ans = 0;
        for (int i = 0; i < 26; ++i) {
            for (int j = i + 1; j < 26; ++j) {
                int overlap = 0;
                foreach (var s in groups[i]) if (groups[j].Contains(s)) overlap++;
                ans += (long)(groups[i].Count - overlap) * (groups[j].Count - overlap) * 2;
            }
        }
        return ans;
    }
}
