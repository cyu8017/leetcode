// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

public class Solution {
    public bool HasTrailingZeros(int[] nums) {
        int even = 0;
        foreach (int v in nums) {
            if (v % 2 == 0) {
                even++;
                if (even >= 2) return true;
            }
        }
        return false;
    }
}
