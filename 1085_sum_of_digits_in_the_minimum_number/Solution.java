// LeetCode 1085 - Sum of Digits in the Minimum Number
// https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

class Solution {
    public int sumOfDigits(int[] nums) {
        int n = nums[0];
        for (int x : nums) {
            if (x < n) {
                n = x;
            }
        }
        int digitSum = 0;
        while (n > 0) {
            digitSum += n % 10;
            n /= 10;
        }
        return digitSum % 2 == 0 ? 1 : 0;
    }
}
