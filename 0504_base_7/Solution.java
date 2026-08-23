// LeetCode 0504 - Base 7
// https://leetcode.com/problems/base-7/

class Solution {
    public String convertToBase7(int num) {
        if (num == 0) {
            return "0";
        }
        boolean negative = num < 0;
        num = Math.abs(num);
        StringBuilder digits = new StringBuilder();
        while (num > 0) {
            digits.append(num % 7);
            num /= 7;
        }
        String result = digits.reverse().toString();
        return negative ? "-" + result : result;
    }
}
