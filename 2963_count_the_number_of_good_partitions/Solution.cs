// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

using System.Collections.Generic;

public class Solution {
    public int NumberOfGoodPartitions(int[] nums) {
        const int mod = 1000000007;
        var last = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) last[nums[i]] = i;
        int ans = 1, end = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (last[nums[i]] > end) end = last[nums[i]];
            if (i == end && i != nums.Length - 1) ans = (int)(ans * 2L % mod);
        }
        return ans;
    }
}
