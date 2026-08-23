// LeetCode 0724 - Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/

public class Solution {
    public int PivotIndex(int[] nums) {
        int total = 0;
        foreach (int x in nums) total += x;
        int left = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (left == total - left - nums[i]) return i;
            left += nums[i];
        }
        return -1;
    }
}
