// LeetCode 1012 - Numbers With Repeated Digits
// https://leetcode.com/problems/numbers-with-repeated-digits/

using System.Collections.Generic;

public class Solution {
    public int NumDupDigitsAtMostN(int n) {
        var s = n.ToString();
        int m = s.Length;
        int totalUnique = 0;
        for (int length = 1; length < m; length++)
            totalUnique += 9 * P(9, length - 1);

        var used = new HashSet<int>();
        bool broken = false;
        for (int i = 0; i < m; i++) {
            int d = s[i] - '0';
            for (int x = (i == 0 ? 1 : 0); x < d; x++) {
                if (used.Contains(x)) continue;
                totalUnique += P(9 - i, m - i - 1);
            }
            if (used.Contains(d)) {
                broken = true;
                break;
            }
            used.Add(d);
        }
        if (!broken) totalUnique++;
        return n - totalUnique;
    }

    private static int P(int a, int b) {
        int res = 1;
        for (int i = 0; i < b; i++) res *= a - i;
        return res;
    }
}
