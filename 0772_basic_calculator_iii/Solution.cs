// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public int Calculate(string s) {
        var expr = new StringBuilder();
        foreach (char ch in s) if (!char.IsWhiteSpace(ch)) expr.Append(ch);
        int i = 0;
        return Parse(expr.ToString(), ref i);
    }

    private int Parse(string expr, ref int i) {
        var stack = new List<long>();
        long num = 0;
        char sign = '+';
        while (i < expr.Length) {
            char ch = expr[i];
            if (char.IsDigit(ch)) num = num * 10 + (ch - '0');
            else if (ch == '(') {
                i++;
                num = Parse(expr, ref i);
            }
            if ((!char.IsDigit(ch) && ch != '(') || i == expr.Length - 1) {
                if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ')' || i == expr.Length - 1) {
                    if (sign == '+') stack.Add(num);
                    else if (sign == '-') stack.Add(-num);
                    else if (sign == '*') stack[stack.Count - 1] *= num;
                    else if (sign == '/') {
                        long top = stack[stack.Count - 1];
                        stack.RemoveAt(stack.Count - 1);
                        stack.Add((long)(top / (double)num));
                    }
                    if (ch == ')') {
                        long sum = 0;
                        foreach (long v in stack) sum += v;
                        return (int)sum;
                    }
                    sign = ch;
                    num = 0;
                }
            }
            i++;
        }
        long total = 0;
        foreach (long v in stack) total += v;
        return (int)total;
    }
}
