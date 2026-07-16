// LeetCode 0291 - Word Pattern II
// https://leetcode.com/problems/word-pattern-ii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean wordPatternMatch(String pattern, String s) {
        return backtrack(pattern, s, 0, 0, new HashMap<>(), new HashMap<>());
    }

    private boolean backtrack(
            String pattern,
            String s,
            int patternIndex,
            int stringIndex,
            Map<Character, String> charToWord,
            Map<String, Character> wordToChar) {
        if (patternIndex == pattern.length()) {
            return stringIndex == s.length();
        }
        char ch = pattern.charAt(patternIndex);
        if (charToWord.containsKey(ch)) {
            String word = charToWord.get(ch);
            if (!s.startsWith(word, stringIndex)) {
                return false;
            }
            return backtrack(pattern, s, patternIndex + 1, stringIndex + word.length(), charToWord, wordToChar);
        }
        for (int end = stringIndex + 1; end <= s.length(); end++) {
            String word = s.substring(stringIndex, end);
            if (wordToChar.containsKey(word)) {
                continue;
            }
            charToWord.put(ch, word);
            wordToChar.put(word, ch);
            if (backtrack(pattern, s, patternIndex + 1, end, charToWord, wordToChar)) {
                return true;
            }
            charToWord.remove(ch);
            wordToChar.remove(word);
        }
        return false;
    }
}
