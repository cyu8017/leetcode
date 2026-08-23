// LeetCode 3728 - Stable Subarrays With Equal Boundary And Interior Sum
// https://leetcode.com/problems/stable_subarrays_with_equal_boundary_and_interior_sum/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long countStableSubarrays(int[] capacity) {
        int n = capacity.length;
        long[] s = new long[n + 1];
        for (int i = 1; i <= n; i++) s[i] = s[i - 1] + capacity[i - 1];
        Map<String, Integer> cnt = new HashMap<>();
        long ans = 0;
        for (int r = 2; r < n; r++) {
            int l = r - 2;
            String keyL = capacity[l] + "#" + (capacity[l] + s[l + 1]);
            cnt.merge(keyL, 1, Integer::sum);
            String keyR = capacity[r] + "#" + s[r];
            ans += cnt.getOrDefault(keyR, 0);
        }
        return ans;
    }
}
