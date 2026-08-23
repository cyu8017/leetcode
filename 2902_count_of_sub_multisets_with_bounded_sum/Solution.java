// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countSubMultisets(int[] nums, int l, int r) {
        final int mod = 1000000007;
        Map<Integer, Integer> freq = new HashMap<>();
        int total = 0;
        for (int v : nums) {
            freq.merge(v, 1, Integer::sum);
            total += v;
        }
        if (total < l) return 0;
        if (r > total) r = total;
        int[] dp = new int[r + 1];
        dp[0] = 1;
        int zeros = freq.getOrDefault(0, 0);
        freq.remove(0);
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            int v = e.getKey(), c = e.getValue();
            int[] ndp = new int[r + 1];
            for (int sum = 0; sum <= r; sum++) {
                if (dp[sum] == 0) continue;
                for (int k = 0; k <= c && sum + k * v <= r; k++)
                    ndp[sum + k * v] = (ndp[sum + k * v] + dp[sum]) % mod;
            }
            dp = ndp;
        }
        int ans = 0;
        for (int s = l; s <= r; s++) ans = (ans + dp[s]) % mod;
        ans = (int) (1L * ans * (zeros + 1) % mod);
        return ans;
    }
}
