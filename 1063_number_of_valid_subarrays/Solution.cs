// LeetCode 1063 - Number of Valid Subarrays
// https://leetcode.com/problems/number-of-valid-subarrays/

using System.Collections.Generic;

public class Solution {
    public int ValidSubarrays(int[] nums) {
        var stack = new Stack<int>();
        int ans = 0;
        for (int i = 0; i < nums.Length; i++) {
            while (stack.Count > 0 && nums[stack.Peek()] > nums[i]) {
                int j = stack.Pop();
                ans += i - j;
            }
            stack.Push(i);
        }
        while (stack.Count > 0) {
            int j = stack.Pop();
            ans += nums.Length - j;
        }
        return ans;
    }
}
