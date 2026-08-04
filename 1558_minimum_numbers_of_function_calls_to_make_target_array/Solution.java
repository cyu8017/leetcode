// LeetCode 1558 - Minimum Numbers of Function Calls to Make Target Array
// https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

class Solution {
    public int minOperations(int[] nums) {
        int adds = 0, maxBits = 0;
        for (int x : nums) {
            int bits = 0;
            for (int t = x; t > 0; t >>= 1) {
                adds += t & 1;
                bits++;
            }
            maxBits = Math.max(maxBits, bits - 1);
        }
        return adds + maxBits;
    }
}
