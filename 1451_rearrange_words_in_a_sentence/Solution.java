// LeetCode 1451 - Rearrange Words In A Sentence
// https://leetcode.com/problems/rearrange-words-in-a-sentence/

import java.util.*;

class Solution {
    public String arrangeWords(String text) {
        String[] words = text.split(" ");
        words[0] = words[0].toLowerCase();
        Arrays.sort(words, Comparator.comparingInt(String::length));
        words[0] = Character.toUpperCase(words[0].charAt(0)) + words[0].substring(1);
        return String.join(" ", words);
    }
}
