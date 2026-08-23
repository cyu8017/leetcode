// LeetCode 0930 - Binary Subarrays With Sum
// https://leetcode.com/problems/binary-subarrays-with-sum/

using System.Collections.Generic;

public class Solution {
    public int NumSubarraysWithSum(int[] nums, int goal) {
        var count = new Dictionary<int, int> { [0] = 1 };
        int prefix = 0, ans = 0;
        foreach (int x in nums) {
            prefix += x;
            if (count.ContainsKey(prefix - goal)) ans += count[prefix - goal];
            if (!count.ContainsKey(prefix)) count[prefix] = 0;
            count[prefix]++;
        }
        return ans;
    }
}
