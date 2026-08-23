// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

import java.util.*;

class Solution {
    public String toGoatLatin(String sentence) {
        Set<Character> vowels = new HashSet<>(Arrays.asList(
            'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        String[] words = sentence.split(" ");
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            if (i > 0) out.append(' ');
            String word = words[i];
            StringBuilder goat = new StringBuilder();
            if (vowels.contains(word.charAt(0))) goat.append(word).append("ma");
            else goat.append(word.substring(1)).append(word.charAt(0)).append("ma");
            for (int j = 0; j <= i; j++) goat.append('a');
            out.append(goat);
        }
        return out.toString();
    }
}
