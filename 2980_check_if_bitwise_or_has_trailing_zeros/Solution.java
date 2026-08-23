// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

class Solution {
    public boolean hasTrailingZeros(int[] nums) {
        int even = 0;
        for (int v : nums) {
            if (v % 2 == 0) {
                even++;
                if (even >= 2) return true;
            }
        }
        return false;
    }
}
