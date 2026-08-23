// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

public class Solution {
    public int MinOperations(int[] nums, int k) {
        int ans = 0;
        foreach (int x in nums) if (x < k) ans++;
        return ans;
    }
}
