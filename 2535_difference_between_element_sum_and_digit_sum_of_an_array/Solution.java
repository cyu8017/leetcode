// LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution {
    public int differenceOfSum(int[] nums) {
        int elem = 0, digit = 0;
        for (int num : nums) {
            elem += num;
            int x = num;
            while (x > 0) {
                digit += x % 10;
                x /= 10;
            }
        }
        return Math.abs(elem - digit);
    }
}
