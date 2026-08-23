// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

using System;
using System.Collections.Generic;

public class Solution {
    public int SplitNum(int num) {
        var digits = new List<int>();
        while (num > 0) {
            digits.Add(num % 10);
            num /= 10;
        }
        digits.Sort();
        int a = 0, b = 0;
        for (int i = 0; i < digits.Count; ++i) {
            if (i % 2 == 0) a = a * 10 + digits[i];
            else b = b * 10 + digits[i];
        }
        return a + b;
    }
}
