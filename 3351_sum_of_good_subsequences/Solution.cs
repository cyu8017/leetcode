// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

using System.Collections.Generic;

public class Solution {
    public int SumOfGoodSubsequences(int[] nums) {
        const int mod = 1000000007;
        var cnt = new Dictionary<int, int>();
        var sum = new Dictionary<int, int>();
        int Get(Dictionary<int, int> d, int k) => d.TryGetValue(k, out int v) ? v : 0;
        int ans = 0;
        foreach (int x in nums) {
            int c = 1;
            int s = x;
            if (Get(cnt, x - 1) > 0) {
                c = (c + cnt[x - 1]) % mod;
                s = (int)(((long)s + sum[x - 1] + (long)cnt[x - 1] * x % mod) % mod);
            }
            if (Get(cnt, x + 1) > 0) {
                c = (c + cnt[x + 1]) % mod;
                s = (int)(((long)s + sum[x + 1] + (long)cnt[x + 1] * x % mod) % mod);
            }
            cnt[x] = (Get(cnt, x) + c) % mod;
            sum[x] = (Get(sum, x) + s) % mod;
            ans = (ans + s) % mod;
        }
        return ans;
    }
}
