// LeetCode 1446 - Consecutive Characters
// https://leetcode.com/problems/consecutive-characters/

public class Solution {
    public int MaxPower(string s) {
        int answer = 1, run = 1;
        for (int i = 1; i < s.Length; i++) {
            run = s[i] == s[i - 1] ? run + 1 : 1;
            answer = System.Math.Max(answer, run);
        }
        return answer;
    }
}
