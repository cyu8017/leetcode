// LeetCode 0507 - Perfect Number
// https://leetcode.com/problems/perfect-number/

public class Solution {
    public bool CheckPerfectNumber(int num) {
        if (num <= 1) {
            return false;
        }
        int total = 1;
        int limit = (int)Math.Sqrt(num);
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
