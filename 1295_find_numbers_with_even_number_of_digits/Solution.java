// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int value : nums) {
            int digits = value == 0 ? 1 : 0;
            int x = value;
            while (x > 0) {
                digits++;
                x /= 10;
            }
            if (digits % 2 == 0) count++;
        }
        return count;
    }
}
