// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution {
    public char repeatedCharacter(String s) {
        boolean[] seen = new boolean[26];
        for (char c : s) {
            int i = c - 'a';
            if (seen[i]) return c;
            seen[i] = true;
        }
        return (char)0;
    }
}
