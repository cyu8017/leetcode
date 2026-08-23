// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

using System.Collections.Generic;

public class Solution {
    public int CountPairs(IList<IList<int>> coordinates, int k) {
        var freq = new Dictionary<(int, int), int>();
        int ans = 0;
        foreach (var p in coordinates) {
            int x = p[0], y = p[1];
            for (int a = 0; a <= k; a++) {
                int b = k - a;
                var key = (x ^ a, y ^ b);
                if (freq.ContainsKey(key)) ans += freq[key];
            }
            var cur = (x, y);
            if (!freq.ContainsKey(cur)) freq[cur] = 0;
            freq[cur]++;
        }
        return ans;
    }
}
