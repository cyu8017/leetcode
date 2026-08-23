// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

using System.Collections.Generic;

public class Solution {
    public long CountBadPairs(int[] nums) {
        long n = nums.Length;
        long total = n * (n - 1) / 2;
        var freq = new Dictionary<int, long>();
        long good = 0;
        for (int i = 0; i < nums.Length; i++) {
            int key = nums[i] - i;
            if (freq.TryGetValue(key, out long c)) good += c;
            else c = 0;
            freq[key] = c + 1;
        }
        return total - good;
    }
}
