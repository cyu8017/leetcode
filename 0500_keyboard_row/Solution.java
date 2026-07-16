// LeetCode 0500 - Keyboard Row
// https://leetcode.com/problems/keyboard-row/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public String[] findWords(String[] words) {
        Set<Character>[] rows = new Set[] {
            toSet("qwertyuiop"),
            toSet("asdfghjkl"),
            toSet("zxcvbnm"),
        };
        List<String> result = new ArrayList<>();
        for (String word : words) {
            Set<Character> letters = new HashSet<>();
            for (char ch : word.toCharArray()) {
                if (Character.isLetter(ch)) {
                    letters.add(Character.toLowerCase(ch));
                }
            }
            for (Set<Character> row : rows) {
                if (row.containsAll(letters)) {
                    result.add(word);
                    break;
                }
            }
        }
        return result.toArray(new String[0]);
    }

    private Set<Character> toSet(String letters) {
        Set<Character> row = new HashSet<>();
        for (char ch : letters.toCharArray()) {
            row.add(ch);
        }
        return row;
    }
}
