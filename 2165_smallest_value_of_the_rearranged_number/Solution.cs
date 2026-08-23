// LeetCode 2165 - Smallest Value of the Rearranged Number
// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

public class Solution {
    public long SmallestNumber(long num) {
        bool neg = num < 0;
        if (neg) num = -num;
        if (num == 0) return 0;
        var digits = new List<char>();
        while (num > 0) { digits.Add((char)('0' + num % 10)); num /= 10; }
        if (neg) {
            digits.Sort((a, b) => b.CompareTo(a));
            long ans = 0;
            foreach (char d in digits) ans = ans * 10 + (d - '0');
            return -ans;
        }
        digits.Sort();
        if (digits[0] == '0') {
            for (int i = 1; i < digits.Count; i++) {
                if (digits[i] != '0') { var t = digits[0]; digits[0] = digits[i]; digits[i] = t; break; }
            }
        }
        long res = 0;
        foreach (char d in digits) res = res * 10 + (d - '0');
        return res;
    }
}
