// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

import java.util.*;

/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface Master {
 *     public int guess(String word);
 * }
 */
class Solution {
    public void findSecretWord(String[] words, Master master) {
        List<String> candidates = new ArrayList<>(Arrays.asList(words));
        while (!candidates.isEmpty()) {
            String best = candidates.get(0);
            int bestWorst = candidates.size() + 1;
            for (String w : candidates) {
                int[] buckets = new int[7];
                for (String c : candidates) buckets[match(w, c)]++;
                int worst = 0;
                for (int b : buckets) worst = Math.max(worst, b);
                if (worst < bestWorst) {
                    bestWorst = worst;
                    best = w;
                }
            }
            int score = master.guess(best);
            if (score == 6) return;
            List<String> next = new ArrayList<>();
            for (String c : candidates) if (match(c, best) == score) next.add(c);
            candidates = next;
        }
    }

    private int match(String a, String b) {
        int m = 0;
        for (int i = 0; i < a.length(); i++) if (a.charAt(i) == b.charAt(i)) m++;
        return m;
    }
}
