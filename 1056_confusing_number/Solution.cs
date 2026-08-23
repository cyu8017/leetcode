// LeetCode 1056 - Confusing Number
// https://leetcode.com/problems/confusing-number/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public bool ConfusingNumber(int n) {
        var rotate = new Dictionary<char, char> {
            ['0'] = '0', ['1'] = '1', ['6'] = '9', ['8'] = '8', ['9'] = '6'
        };
        string s = n.ToString();
        var rotated = new StringBuilder();
        for (int i = s.Length - 1; i >= 0; i--) {
            if (!rotate.ContainsKey(s[i])) {
                return false;
            }
            rotated.Append(rotate[s[i]]);
        }
        return rotated.ToString() != s;
    }
}
