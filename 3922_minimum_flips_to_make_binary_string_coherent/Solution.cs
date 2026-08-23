// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

using System;

public class Solution {
    public int MinFlips(string s) {
        int ones = 0;
        foreach (char c in s) if (c == '1') ones++;
        int answer = ones;
        if (ones > 0) answer = ones - 1;
        int zeros = s.Length - ones;
        answer = Math.Min(answer, zeros);
        if (s.Length >= 2) {
            int cost = 0;
            for (int i = 0; i < s.Length; i++) {
                char want = (i == 0 || i == s.Length - 1) ? '1' : '0';
                if (s[i] != want) cost++;
            }
            answer = Math.Min(answer, cost);
        }
        return answer;
    }
}
