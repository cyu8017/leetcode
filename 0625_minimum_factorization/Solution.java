// LeetCode 0625 - Minimum Factorization
// https://leetcode.com/problems/minimum-factorization/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int smallestFactorization(int num) {
        if (num < 10) {
            return num;
        }
        List<Integer> digits = new ArrayList<>();
        for (int digit = 9; digit >= 2; --digit) {
            while (num % digit == 0) {
                digits.add(digit);
                num /= digit;
            }
        }
        if (num != 1) {
            return 0;
        }
        long result = 0;
        for (int i = digits.size() - 1; i >= 0; --i) {
            result = result * 10 + digits.get(i);
            if (result > Integer.MAX_VALUE) {
                return 0;
            }
        }
        return (int) result;
    }
}
