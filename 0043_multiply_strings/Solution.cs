// LeetCode 0043 - Multiply Strings
// https://leetcode.com/problems/multiply-strings/

public class Solution {
    public string Multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }

        int[] positions = new int[num1.Length + num2.Length];

        for (int i = num1.Length - 1; i >= 0; i--) {
            for (int j = num2.Length - 1; j >= 0; j--) {
                int product = (num1[i] - '0') * (num2[j] - '0');
                int low = i + j + 1;
                int high = i + j;
                int total = product + positions[low];
                positions[low] = total % 10;
                positions[high] += total / 10;
            }
        }

        int start = 0;
        while (start < positions.Length && positions[start] == 0) {
            start++;
        }

        var result = new System.Text.StringBuilder();
        for (int i = start; i < positions.Length; i++) {
            result.Append(positions[i]);
        }

        return result.Length == 0 ? "0" : result.ToString();
    }
}
