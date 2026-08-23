// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

using System.Collections.Generic;

public class Solution {
    public int SumDivisibleByK(int[] nums, int k) {
        var cnt = new Dictionary<int, int>();
        foreach (int x in nums) {
            if (!cnt.ContainsKey(x)) cnt[x] = 0;
            cnt[x]++;
        }
        int ans = 0;
        foreach (var kv in cnt) {
            if (kv.Value % k == 0) ans += kv.Key * kv.Value;
        }
        return ans;
    }
}
