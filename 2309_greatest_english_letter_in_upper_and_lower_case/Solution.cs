// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

public class Solution {
    public string GreatestLetter(string s) {
        bool[] lower = new bool[26], upper = new bool[26];
        foreach (char c in s) {
            if (c >= 'a' && c <= 'z') lower[c - 'a'] = true;
            else upper[c - 'A'] = true;
        }
        for (int i = 25; i >= 0; --i)
            if (lower[i] && upper[i]) return ((char)('A' + i)).ToString();
        return "";
    }
}
