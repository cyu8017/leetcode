// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if (pattern.length() != words.length) {
            return false;
        }
        Map<Character, String> charToWord = new HashMap<>();
        Map<String, Character> wordToChar = new HashMap<>();
        for (int index = 0; index < pattern.length(); index++) {
            char ch = pattern.charAt(index);
            String word = words[index];
            if (charToWord.containsKey(ch)) {
                if (!charToWord.get(ch).equals(word)) {
                    return false;
                }
            } else {
                if (wordToChar.containsKey(word)) {
                    return false;
                }
                charToWord.put(ch, word);
                wordToChar.put(word, ch);
            }
        }
        return true;
    }
}
