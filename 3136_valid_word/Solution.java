// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

class Solution {
    public boolean isValid(String word) {
        if (word.length() < 3) return false;
        boolean hasVowel = false, hasConsonant = false;
        boolean[] vs = new boolean[26];
        for (char c : "aeiou".toCharArray()) vs[c - 'a'] = true;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (Character.isLetter(c)) {
                char lower = Character.toLowerCase(c);
                if (vs[lower - 'a']) hasVowel = true;
                else hasConsonant = true;
            } else if (!Character.isDigit(c)) {
                return false;
            }
        }
        return hasVowel && hasConsonant;
    }
}
