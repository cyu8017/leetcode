// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

using System.Collections.Generic;

public class Solution {
    public int SubarraysDivByK(int[] nums, int k) {
        var count = new Dictionary<int, int> { [0] = 1 };
        int prefix = 0, ans = 0;
        foreach (int x in nums) {
            prefix = ((prefix + x) % k + k) % k;
            if (count.ContainsKey(prefix)) ans += count[prefix];
            if (!count.ContainsKey(prefix)) count[prefix] = 0;
            count[prefix]++;
        }
        return ans;
    }
}
