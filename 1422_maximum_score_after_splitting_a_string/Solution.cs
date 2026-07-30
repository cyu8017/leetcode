// LeetCode 1422 - Maximum Score After Splitting A String
// https://leetcode.com/problems/maximum-score-after-splitting-a-string/

public class Solution {
    public int MaxScore(string s) {
        int ones = 0;
        foreach (char c in s) if (c == '1') ones++;
        int leftZeros = 0, answer = 0;
        for (int i = 0; i < s.Length - 1; i++) {
            if (s[i] == '0') leftZeros++; else ones--;
            answer = System.Math.Max(answer, leftZeros + ones);
        }
        return answer;
    }
}
