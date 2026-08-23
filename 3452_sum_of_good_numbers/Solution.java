// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

class Solution {
    public int sumOfGoodNumbers(int[] nums, int k) {
        int ans = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            boolean good = true;
            if (i - k >= 0 && x <= nums[i - k]) good = false;
            if (i + k < n && x <= nums[i + k]) good = false;
            if (good) ans += x;
        }
        return ans;
    }
}
