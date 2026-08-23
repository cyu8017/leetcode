// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

using System.Collections.Generic;

public class Solution {
    public int RangeSum(int[] nums) {
        const int mod = 1000000007;
        var cnt = new Dictionary<int, int>();
        var sum = new Dictionary<int, int>();
        int Get(Dictionary<int, int> d, int k) => d.TryGetValue(k, out int v) ? v : 0;
        int ans = 0;
        foreach (int x in nums) {
            int cL = Get(cnt, x - 1), sL = Get(sum, x - 1);
            int cR = Get(cnt, x + 1), sR = Get(sum, x + 1);
            int c = (1 + cL + cR) % mod;
            int s = (int)(((long)x + sL + (long)cL * x % mod + sR + (long)cR * x % mod) % mod);
            if (cL > 0 && cR > 0) {
                c = (c + (int)((long)cL * cR % mod)) % mod;
                s = (int)((s + (long)sL * cR % mod + (long)sR * cL % mod + (long)cL * cR % mod * x % mod) % mod);
            }
            cnt[x] = (Get(cnt, x) + c) % mod;
            sum[x] = (Get(sum, x) + s) % mod;
            ans = (ans + s) % mod;
        }
        return ans;
    }
}
