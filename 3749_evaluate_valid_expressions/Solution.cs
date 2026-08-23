// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate-valid-expressions/

public class Solution {
    public long EvaluateExpression(string expression) {
        (long, int) Parse(int i) {
            if (char.IsDigit(expression[i]) || expression[i] == '-') {
                int j = i;
                if (expression[j] == '-') j++;
                while (j < expression.Length && char.IsDigit(expression[j])) j++;
                return (long.Parse(expression.Substring(i, j - i)), j);
            }
            int j2 = i;
            while (expression[j2] != '(') j2++;
            string op = expression.Substring(i, j2 - i);
            j2++;
            var (val1, nextJ1) = Parse(j2);
            j2 = nextJ1 + 1;
            var (val2, nextJ2) = Parse(j2);
            j2 = nextJ2 + 1;
            long res = 0;
            if (op == "add") res = val1 + val2;
            else if (op == "sub") res = val1 - val2;
            else if (op == "mul") res = val1 * val2;
            else if (op == "div") res = val1 / val2;
            return (res, j2);
        }
        return Parse(0).Item1;
    }
}
