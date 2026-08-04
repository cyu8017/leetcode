// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

class Solution {
    public boolean isArmstrong(int n) {
        String digits = String.valueOf(n);
        int power = digits.length(), sum = 0;
        for (char d : digits.toCharArray()) {
            sum += (int) Math.pow(d - '0', power);
        }
        return n == sum;
    }
}
