// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

using System.Collections.Generic;

public class Solution {
    public int NumberOfGoodSubarraySplits(int[] nums) {
        const int MOD = 1000000007;
        var ones = new List<int>();
        for (int i = 0; i < nums.Length; i++) if (nums[i] == 1) ones.Add(i);
        if (ones.Count == 0) return 0;
        long ans = 1;
        for (int i = 1; i < ones.Count; i++)
            ans = ans * (ones[i] - ones[i - 1]) % MOD;
        return (int)ans;
    }
}
