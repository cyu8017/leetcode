// LeetCode 0537 - Complex Number Multiplication
// https://leetcode.com/problems/complex-number-multiplication/

public class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        int[] first = parse(num1);
        int[] second = parse(num2);
        int real = first[0] * second[0] - first[1] * second[1];
        int imag = first[0] * second[1] + first[1] * second[0];
        return real + "+" + imag + "i";
    }

    private int[] parse(String num) {
        int plus = num.indexOf('+');
        int real = Integer.parseInt(num.substring(0, plus));
        int imag = Integer.parseInt(num.substring(plus + 1, num.length() - 1));
        return new int[] { real, imag };
    }
}
