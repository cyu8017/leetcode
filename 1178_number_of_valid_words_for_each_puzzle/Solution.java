// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

import java.util.*;

class Solution {
    public List<Integer> findNumOfValidWords(String[] words, String[] puzzles) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (String w : words) freq.merge(maskOf(w), 1, Integer::sum);
        List<Integer> ans = new ArrayList<>();
        for (String puzzle : puzzles) {
            int first = 1 << (puzzle.charAt(0) - 'a');
            int full = maskOf(puzzle);
            int sub = full, total = 0;
            while (true) {
                if ((sub & first) != 0) total += freq.getOrDefault(sub, 0);
                if (sub == 0) break;
                sub = (sub - 1) & full;
            }
            ans.add(total);
        }
        return ans;
    }
    private int maskOf(String s) {
        int mask = 0;
        for (char ch : s.toCharArray()) mask |= 1 << (ch - 'a');
        return mask;
    }
}
