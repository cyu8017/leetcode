// LeetCode 1390 - Four Divisors
// https://leetcode.com/problems/four-divisors/

using System.Collections.Generic;
public class Solution {
    public int SumFourDivisors(int[] nums) {
        int ans = 0;
        foreach (int x in nums) {
            var ds = new HashSet<int>();
            for (int d = 1; d * d <= x; d++) {
                if (x % d == 0) { ds.Add(d); ds.Add(x / d); }
                if (ds.Count > 4) break;
            }
            if (ds.Count == 4) { int s = 0; foreach (int v in ds) s += v; ans += s; }
        }
        return ans;
    }
}
