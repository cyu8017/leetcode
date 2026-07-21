// LeetCode 1822 - Sign of the Product of an Array
// https://leetcode.com/problems/sign-of-the-product-of-an-array/

public class Solution {
    public int ArraySign(int[] nums) {
        int sign = 1;
        foreach (int num in nums) {
            if (num == 0) return 0;
            if (num < 0) sign = -sign;
        }
        return sign;
    }
}
