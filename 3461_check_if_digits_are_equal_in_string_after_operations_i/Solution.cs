// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

using System.Collections.Generic;

public class Solution {
    public bool HasSameDigits(string s) {
        var b = new List<char>(s);
        while (b.Count > 2) {
            var nb = new List<char>(b.Count - 1);
            for (int i = 0; i + 1 < b.Count; i++) {
                nb.Add((char)('0' + (b[i] - '0' + b[i + 1] - '0') % 10));
            }
            b = nb;
        }
        return b[0] == b[1];
    }
}
