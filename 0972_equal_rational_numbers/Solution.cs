// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

using System;

public class Solution {
    public bool IsRationalEqual(string s, string t) {
        return Math.Abs(Parse(s) - Parse(t)) < 1e-12;
    }
    private double Parse(string x) {
        if (!x.Contains('(')) return string.IsNullOrEmpty(x) ? 0.0 : double.Parse(x);
        int lp = x.IndexOf('(');
        string nonRep = x.Substring(0, lp);
        string rep = x.Substring(lp + 1, x.Length - lp - 2);
        if (!nonRep.Contains('.')) nonRep += ".";
        int dot = nonRep.IndexOf('.');
        string integer = nonRep.Substring(0, dot);
        string frac = nonRep.Substring(dot + 1);
        double bas = string.IsNullOrEmpty(integer) ? 0.0 : double.Parse(integer);
        if (frac.Length > 0) {
            double denom = 1;
            for (int i = 0; i < frac.Length; i++) denom *= 10;
            bas += double.Parse(frac) / denom;
        }
        if (rep.Length > 0) {
            double repVal = double.Parse(rep);
            double cycle = 1;
            for (int i = 0; i < rep.Length; i++) cycle *= 10;
            double denom = cycle - 1;
            for (int i = 0; i < frac.Length; i++) denom *= 10;
            bas += repVal / denom;
        }
        return bas;
    }
}
