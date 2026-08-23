// LeetCode 0507 - Perfect Number
// https://leetcode.com/problems/perfect-number/

class Solution {
    public boolean checkPerfectNumber(int num) {
        if (num <= 1) {
            return false;
        }
        int total = 1;
        int limit = (int) Math.sqrt(num);
        for (int divisor = 2; divisor <= limit; divisor++) {
            if (num % divisor == 0) {
                total += divisor;
                int pair = num / divisor;
                if (pair != divisor) {
                    total += pair;
                }
            }
        }
        return total == num;
    }
}
