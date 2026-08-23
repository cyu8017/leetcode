// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> bannedSet = new HashSet<>(Arrays.asList(banned));
        Map<String, Integer> counts = new HashMap<>();
        StringBuilder word = new StringBuilder();
        String best = "";
        int bestCount = 0;
        for (int i = 0; i <= paragraph.length(); i++) {
            char ch = i < paragraph.length() ? paragraph.charAt(i) : ' ';
            if (Character.isLetter(ch)) {
                word.append(Character.toLowerCase(ch));
            } else if (word.length() > 0) {
                String w = word.toString();
                word.setLength(0);
                if (!bannedSet.contains(w)) {
                    int c = counts.merge(w, 1, Integer::sum);
                    if (c > bestCount) {
                        bestCount = c;
                        best = w;
                    }
                }
            }
        }
        return best;
    }
}
