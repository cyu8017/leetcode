// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

class Solution {
    public int minKBitFlips(int[] nums, int k) {
        int n = nums.length;
        int[] flip = new int[n];
        int ans = 0, flipped = 0;
        for (int i = 0; i < n; i++) {
            if (i >= k) flipped ^= flip[i - k];
            if (nums[i] == flipped) {
                if (i + k > n) return -1;
                ans++;
                flipped ^= 1;
                flip[i] = 1;
            }
        }
        return ans;
    }
}
