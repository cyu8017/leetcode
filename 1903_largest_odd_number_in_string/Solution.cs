// LeetCode 1903 - Largest Odd Number in String
// https://leetcode.com/problems/largest-odd-number-in-string/

public class Solution {
    public string LargestOddNumber(string num) {
        for (int i = num.Length - 1; i >= 0; i--) {
            if ((num[i] - '0') % 2 != 0) return num.Substring(0, i + 1);
        }
        return "";
    }
}