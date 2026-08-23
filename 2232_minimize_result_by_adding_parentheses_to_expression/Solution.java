// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

class Solution {
    public String minimizeResult(String expression) {
        int plus = expression.indexOf('+');
        String left = expression.substring(0, plus);
        String right = expression.substring(plus + 1);
        int bestVal = Integer.MAX_VALUE;
        String best = "";
        for (int i = 0; i < left.length(); i++) {
            for (int j = 1; j <= right.length(); j++) {
                String a = left.substring(0, i);
                String b = left.substring(i);
                String c = right.substring(0, j);
                String d = right.substring(j);
                int val = Integer.parseInt(b) + Integer.parseInt(c);
                if (a.length() > 0) val *= Integer.parseInt(a);
                if (d.length() > 0) val *= Integer.parseInt(d);
                String cand = a + "(" + b + "+" + c + ")" + d;
                if (val < bestVal) {
                    bestVal = val;
                    best = cand;
                }
            }
        }
        return best;
    }
}
