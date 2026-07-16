// LeetCode 0006 - Zigzag Conversion
// https://leetcode.com/problems/zigzag-conversion/

public class Solution {
    public string Convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.Length) {
            return s;
        }

        var rows = new System.Text.StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new System.Text.StringBuilder();
        }

        int index = 0;
        int step = 1;
        foreach (char ch in s) {
            rows[index].Append(ch);
            if (index == 0) {
                step = 1;
            } else if (index == numRows - 1) {
                step = -1;
            }
            index += step;
        }

        var result = new System.Text.StringBuilder();
        foreach (var row in rows) {
            result.Append(row);
        }
        return result.ToString();
    }
}
