// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

using System.Collections.Generic;

public class Solution {
    public IList<int> SequentialDigits(int low, int high) {
        const string digits = "123456789";
        var answer = new List<int>();
        for (int length = 2; length <= 9; length++) {
            for (int start = 0; start <= 9 - length; start++) {
                int value = int.Parse(digits.Substring(start, length));
                if (value >= low && value <= high) answer.Add(value);
            }
        }
        return answer;
    }
}
