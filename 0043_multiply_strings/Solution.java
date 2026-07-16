// LeetCode 0043 - Multiply Strings
// https://leetcode.com/problems/multiply-strings/

class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }

        int[] positions = new int[num1.length() + num2.length()];

        for (int i = num1.length() - 1; i >= 0; i--) {
            for (int j = num2.length() - 1; j >= 0; j--) {
                int product = (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
                int low = i + j + 1;
                int high = i + j;
                int total = product + positions[low];
                positions[low] = total % 10;
                positions[high] += total / 10;
            }
        }

        StringBuilder result = new StringBuilder();
        for (int digit : positions) {
            result.append(digit);
        }

        while (result.length() > 0 && result.charAt(0) == '0') {
            result.deleteCharAt(0);
        }

        return result.length() == 0 ? "0" : result.toString();
    }
}
