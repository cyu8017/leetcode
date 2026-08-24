// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

class Solution {
    public int findClosestNumber(int[] nums) {
        int ans = nums[0];
        for (int x : nums) {
            if (Math.abs(x) < Math.abs(ans) || (Math.abs(x) == Math.abs(ans) && x > ans)) ans = x;
        }
        return ans;
    }
}
