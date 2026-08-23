// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum_deletion_cost_to_make_all_characters_equal/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long minCost(String s, int[] cost) {
        long tot = 0;
        Map<Character, Long> g = new HashMap<>();
        for (int i = 0; i < cost.length; i++) {
            tot += cost[i];
            g.merge(s.charAt(i), (long) cost[i], Long::sum);
        }
        long ans = tot;
        for (long x : g.values()) ans = Math.min(ans, tot - x);
        return ans;
    }
}
