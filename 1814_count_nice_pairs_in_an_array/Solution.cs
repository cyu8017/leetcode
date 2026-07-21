// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

using System.Collections.Generic;

public class Solution {
    public int CountNicePairs(int[] nums) {
        const int MOD = 1_000_000_007;
        var freq = new Dictionary<int, int>();
        long ans = 0;
        foreach (int num in nums) {
            int diff = num - Rev(num);
            if (freq.TryGetValue(diff, out int count)) {
                ans = (ans + count) % MOD;
                freq[diff] = count + 1;
            } else {
                freq[diff] = 1;
            }
        }
        return (int)ans;
    }

    private int Rev(int x) {
        int result = 0;
        while (x > 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return result;
    }
}
