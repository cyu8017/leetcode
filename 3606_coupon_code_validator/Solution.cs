// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> ValidateCoupons(string[] code, string[] businessLine, bool[] isActive) {
        var bs = new HashSet<string> { "electronics", "grocery", "pharmacy", "restaurant" };
        bool Check(string s) {
            if (string.IsNullOrEmpty(s)) return false;
            foreach (char c in s)
                if (!char.IsLetterOrDigit(c) && c != '_') return false;
            return true;
        }
        var idx = new List<int>();
        for (int i = 0; i < code.Length; i++) {
            if (isActive[i] && bs.Contains(businessLine[i]) && Check(code[i])) idx.Add(i);
        }
        idx.Sort((i, j) => {
            int c = string.CompareOrdinal(businessLine[i], businessLine[j]);
            if (c != 0) return c;
            return string.CompareOrdinal(code[i], code[j]);
        });
        var ans = new List<string>();
        foreach (int i in idx) ans.Add(code[i]);
        return ans;
    }
}
