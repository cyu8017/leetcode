// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/

using System.Collections.Generic;

public class Solution {
    public int CountSubMultisets(IList<int> nums, int l, int r) {
        const int mod = 1000000007;
        var freq = new Dictionary<int, int>();
        int total = 0;
        foreach (int v in nums) {
            if (!freq.ContainsKey(v)) freq[v] = 0;
            freq[v]++;
            total += v;
        }
        if (total < l) return 0;
        if (r > total) r = total;
        int[] dp = new int[r + 1];
        dp[0] = 1;
        int zeros = freq.ContainsKey(0) ? freq[0] : 0;
        freq.Remove(0);
        foreach (var kv in freq) {
            int v = kv.Key, c = kv.Value;
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
        ans = (int)(1L * ans * (zeros + 1) % mod);
        return ans;
    }
}
