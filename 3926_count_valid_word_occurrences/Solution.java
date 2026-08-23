// LeetCode 3926 - Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] countWordOccurrences(String[] chunks, String[] queries) {
        StringBuilder sb = new StringBuilder();
        for (String c : chunks) sb.append(c);
        String s = sb.toString();
        int n = s.length();
        Map<String, Integer> cnt = new HashMap<>();
        int i = 0;
        while (i < n) {
            if (s.charAt(i) == ' ' || s.charAt(i) == '-') {
                i++;
                continue;
            }
            int j = i;
            while (j < n && s.charAt(j) != ' ' && (s.charAt(j) != '-' || (j + 1 < n && s.charAt(j + 1) != ' ' && s.charAt(j + 1) != '-'))) {
                j++;
            }
            String word = s.substring(i, j);
            cnt.put(word, cnt.getOrDefault(word, 0) + 1);
            i = j;
        }
        int[] ans = new int[queries.length];
        for (int k = 0; k < queries.length; k++) ans[k] = cnt.getOrDefault(queries[k], 0);
        return ans;
    }
}
