// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

using System;

public class Solution {
    public string MinimizeResult(string expression) {
        int plus = expression.IndexOf('+');
        string left = expression.Substring(0, plus);
        string right = expression.Substring(plus + 1);
        int bestVal = int.MaxValue;
        string best = "";
        for (int i = 0; i < left.Length; i++) {
            for (int j = 1; j <= right.Length; j++) {
                string a = left.Substring(0, i);
                string b = left.Substring(i);
                string c = right.Substring(0, j);
                string d = right.Substring(j);
                int val = int.Parse(b) + int.Parse(c);
                if (a.Length > 0) val *= int.Parse(a);
                if (d.Length > 0) val *= int.Parse(d);
                string cand = a + "(" + b + "+" + c + ")" + d;
                if (val < bestVal) {
                    bestVal = val;
                    best = cand;
                }
            }
        }
        return best;
    }
}
