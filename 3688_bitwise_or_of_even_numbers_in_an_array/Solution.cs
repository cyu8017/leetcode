// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

public class Solution {
    public int EvenNumberBitwiseORs(int[] nums) {
        int ans = 0;
        foreach (int x in nums) if (x % 2 == 0) ans |= x;
        return ans;
    }
}
