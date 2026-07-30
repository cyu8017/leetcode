// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

using System;

public class Solution {
    public int EqualSubstring(string s, string t, int maxCost) {
        int left = 0, cost = 0, answer = 0;
        for (int right = 0; right < s.Length; right++) {
            cost += Math.Abs(s[right] - t[right]);
            while (cost > maxCost) {
                cost -= Math.Abs(s[left] - t[left]);
                left++;
            }
            answer = Math.Max(answer, right - left + 1);
        }
        return answer;
    }
}
