// LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

public class Solution {
    public int MinimumCost(int[] nums) {
        int a = nums[0], b = 100, c = 100;
        for (int i = 1; i < nums.Length; i++) {
            int x = nums[i];
            if (x < b) {
                c = b;
                b = x;
            } else if (x < c) {
                c = x;
            }
        }
        return a + b + c;
    }
}
