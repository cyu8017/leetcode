// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

public class Solution {
    public char RepeatedCharacter(string s) {
        bool[] seen = new bool[26];
        foreach (char c in s) {
            int i = c - 'a';
            if (seen[i]) return c;
            seen[i] = true;
        }
        return (char)0;
    }
}
