// LeetCode 1065 - Index Pairs of a String
// https://leetcode.com/problems/index-pairs-of-a-string/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[][] indexPairs(String text, String[] words) {
        Set<String> wordSet = new HashSet<>();
        for (String w : words) {
            wordSet.add(w);
        }
        List<int[]> ans = new ArrayList<>();
        int n = text.length();
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (wordSet.contains(text.substring(i, j + 1))) {
                    ans.add(new int[] { i, j });
                }
            }
        }
        return ans.toArray(new int[0][]);
    }
}
