// LeetCode 0537 - Complex Number Multiplication
// https://leetcode.com/problems/complex-number-multiplication/

public class Solution {
    public string ComplexNumberMultiply(string num1, string num2) {
        int[] first = Parse(num1);
        int[] second = Parse(num2);
        int real = first[0] * second[0] - first[1] * second[1];
        int imag = first[0] * second[1] + first[1] * second[0];
        return $"{real}+{imag}i";
    }

    private static int[] Parse(string num) {
        int plus = num.IndexOf('+');
        int real = int.Parse(num[..plus]);
        int imag = int.Parse(num[(plus + 1)..^1]);
        return new[] { real, imag };
    }
}
