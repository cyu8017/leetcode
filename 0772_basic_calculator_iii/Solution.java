// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

import java.util.*;

class Solution {
    public int calculate(String s) {
        StringBuilder expr = new StringBuilder();
        for (char ch : s.toCharArray()) if (!Character.isWhitespace(ch)) expr.append(ch);
        int[] i = {0};
        return parse(expr.toString(), i);
    }

    private int parse(String expr, int[] i) {
        List<Long> stack = new ArrayList<>();
        long num = 0;
        char sign = '+';
        while (i[0] < expr.length()) {
            char ch = expr.charAt(i[0]);
            if (Character.isDigit(ch)) num = num * 10 + (ch - '0');
            else if (ch == '(') {
                i[0]++;
                num = parse(expr, i);
            }
            if ((!Character.isDigit(ch) && ch != '(') || i[0] == expr.length() - 1) {
                if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ')' || i[0] == expr.length() - 1) {
                    if (sign == '+') stack.add(num);
                    else if (sign == '-') stack.add(-num);
                    else if (sign == '*') stack.set(stack.size() - 1, stack.get(stack.size() - 1) * num);
                    else if (sign == '/') {
                        long top = stack.remove(stack.size() - 1);
                        stack.add((long) (top / (double) num));
                    }
                    if (ch == ')') {
                        long sum = 0;
                        for (long v : stack) sum += v;
                        return (int) sum;
                    }
                    sign = ch;
                    num = 0;
                }
            }
            i[0]++;
        }
        long total = 0;
        for (long v : stack) total += v;
        return (int) total;
    }
}
