// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class WordDistance {
    private final Map<String, List<Integer>> positions = new HashMap<>();

    public WordDistance(String[] wordsDict) {
        for (int index = 0; index < wordsDict.length; index++) {
            positions.computeIfAbsent(wordsDict[index], key -> new ArrayList<>()).add(index);
        }
    }

    public int shortest(String word1, String word2) {
        List<Integer> left = positions.get(word1);
        List<Integer> right = positions.get(word2);
        int i = 0;
        int j = 0;
        int best = Integer.MAX_VALUE;
        while (i < left.size() && j < right.size()) {
            best = Math.min(best, Math.abs(left.get(i) - right.get(j)));
            if (left.get(i) <= right.get(j)) {
                i++;
            } else {
                j++;
            }
        }
        return best;
    }
}
