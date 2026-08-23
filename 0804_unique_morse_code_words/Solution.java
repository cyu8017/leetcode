// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

import java.util.*;

class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] codes = {
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--", "--.."
        };
        Set<String> seen = new HashSet<>();
        for (String word : words) {
            StringBuilder code = new StringBuilder();
            for (char ch : word.toCharArray()) code.append(codes[ch - 'a']);
            seen.add(code.toString());
        }
        return seen.size();
    }
}
