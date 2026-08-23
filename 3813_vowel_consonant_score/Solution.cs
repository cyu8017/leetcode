// LeetCode 3813 - Vowel Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

public class Solution {
    public int VowelConsonantScore(string s) {
        int v = 0, c = 0;
        foreach (char ch in s) {
            if (char.IsLetter(ch)) {
                c++;
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') v++;
            }
        }
        c -= v;
        if (c == 0) return 0;
        return v / c;
    }
}
