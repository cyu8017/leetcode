// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

using System;
using System.Collections.Generic;

public class Solution {
    public int BalancedString(string s) {
        var count = new Dictionary<char, int>();
        foreach (char ch in s) count[ch] = count.GetValueOrDefault(ch) + 1;
        int limit = s.Length / 4;
        int n = s.Length, left = 0, answer = n;
        for (int right = 0; right < n; right++) {
            count[s[right]]--;
            while (left < n && Excess(count, limit) == 0) {
                answer = Math.Min(answer, right - left + 1);
                count[s[left]]++;
                left++;
            }
        }
        return answer;
    }

    private static int Excess(Dictionary<char, int> count, int limit) {
        int excess = 0;
        foreach (char c in "QWER") {
            if (count.GetValueOrDefault(c) > limit) excess++;
        }
        return excess;
    }
}
