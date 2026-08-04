// LeetCode 1991 - Find the Middle Index in Array
// https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution {
    public int findMiddleIndex(int[] nums) {
        int total = 0;
        for (int x : nums) total += x;
        int left = 0;
        for (int i = 0; i < nums.length; i++) {
            if (left == total - left - nums[i]) return i;
            left += nums[i];
        }
        return -1;
    }
}
