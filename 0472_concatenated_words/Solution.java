// LeetCode 0472 - Concatenated Words
// https://leetcode.com/problems/concatenated-words/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Arrays.sort(words, Comparator.comparingInt(String::length));
        Set<String> wordSet = new HashSet<>(Arrays.asList(words));
        List<String> result = new ArrayList<>();

        for (String word : words) {
            wordSet.remove(word);
            if (canForm(word, wordSet)) {
                result.add(word);
            }
            wordSet.add(word);
        }
        return result;
    }

    private boolean canForm(String word, Set<String> dictionary) {
        if (word.isEmpty()) {
            return true;
        }
        int length = word.length();
        boolean[] dp = new boolean[length + 1];
        dp[0] = true;
        for (int end = 1; end <= length; end++) {
            for (int start = 0; start < end; start++) {
                if (dp[start] && dictionary.contains(word.substring(start, end))) {
                    dp[end] = true;
                    break;
                }
            }
        }
        return dp[length];
    }
}
