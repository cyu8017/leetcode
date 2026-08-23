// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution {
    public String greatestLetter(String s) {
        boolean[] lower = new boolean[26], upper = new boolean[26];
        for (char c : s) {
            if (c >= 'a' && c <= 'z') lower[c - 'a'] = true;
            else upper[c - 'A'] = true;
        }
        for (int i = 25; i >= 0; --i)
            if (lower[i] && upper[i]) return ((char)('A' + i)).toString();
        return "";
    }
}
