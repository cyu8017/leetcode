// LeetCode 2165 - Smallest Value of the Rearranged Number
// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

import java.util.*;

class Solution {
    public long smallestNumber(long num) {
        boolean neg = num < 0;
        if (neg) num = -num;
        if (num == 0) return 0;
        List<Character> digits = new ArrayList<>();
        while (num > 0) { digits.add((char) ('0' + num % 10)); num /= 10; }
        if (neg) {
            digits.sort(Collections.reverseOrder());
            long ans = 0;
            for (char d : digits) ans = ans * 10 + (d - '0');
            return -ans;
        }
        Collections.sort(digits);
        if (digits.get(0) == '0') {
            for (int i = 1; i < digits.size(); i++) {
                if (digits.get(i) != '0') {
                    char t = digits.get(0); digits.set(0, digits.get(i)); digits.set(i, t);
                    break;
                }
            }
        }
        long res = 0;
        for (char d : digits) res = res * 10 + (d - '0');
        return res;
    }
}
