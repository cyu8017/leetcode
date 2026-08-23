// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

public class Solution {
    public int MinKBitFlips(int[] nums, int k) {
        int n = nums.Length;
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
