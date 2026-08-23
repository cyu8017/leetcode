// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

using System.Collections.Generic;

public class Solution {
    public int AlternateDigitSum(int n) {
        var s = new List<int>();
        while (n > 0) {
            s.Add(n % 10);
            n /= 10;
        }
        int ans = 0, sign = 1;
        for (int i = s.Count - 1; i >= 0; --i) {
            ans += sign * s[i];
            sign = -sign;
        }
        return ans;
    }
}
