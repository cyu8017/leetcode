// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

class Solution {
    public boolean isRationalEqual(String s, String t) {
        return Math.abs(parse(s) - parse(t)) < 1e-12;
    }

    private double parse(String x) {
        if (!x.contains("(")) return x.isEmpty() ? 0.0 : Double.parseDouble(x);
        int lp = x.indexOf('(');
        String nonRep = x.substring(0, lp);
        String rep = x.substring(lp + 1, x.length() - 1);
        if (!nonRep.contains(".")) nonRep += ".";
        int dot = nonRep.indexOf('.');
        String integer = nonRep.substring(0, dot);
        String frac = nonRep.substring(dot + 1);
        double bas = integer.isEmpty() ? 0.0 : Double.parseDouble(integer);
        if (frac.length() > 0) {
            double denom = 1;
            for (int i = 0; i < frac.length(); i++) denom *= 10;
            bas += Double.parseDouble(frac) / denom;
        }
        if (rep.length() > 0) {
            double repVal = Double.parseDouble(rep);
            double cycle = 1;
            for (int i = 0; i < rep.length(); i++) cycle *= 10;
            double denom = cycle - 1;
            for (int i = 0; i < frac.length(); i++) denom *= 10;
            bas += repVal / denom;
        }
        return bas;
    }
}
