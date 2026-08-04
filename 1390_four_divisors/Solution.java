// LeetCode 1390 - Four Divisors
// https://leetcode.com/problems/four-divisors/

import java.util.*;

class Solution {
    public int sumFourDivisors(int[] nums) {
        int ans = 0;
        for (int x : nums) {
            var ds = new HashSet<>();
            for (int d = 1; d * d <= x; d++) {
                if (x % d == 0) { ds.add(d); ds.add(x / d); }
                if (ds.size() > 4) break;
            }
            if (ds.size() == 4) { int s = 0; for (int v : ds) s += v; ans += s; }
        }
        return ans;
    }
}
