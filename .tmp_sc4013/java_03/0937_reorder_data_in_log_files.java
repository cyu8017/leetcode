// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

import java.util.*;

class Solution {
    public String[] reorderLogFiles(String[] logs) {
        List<String> letter = new ArrayList<>();
        List<String> digit = new ArrayList<>();
        for (String log : logs) {
            int sp = log.indexOf(' ');
            if (Character.isLetter(log.charAt(sp + 1))) letter.add(log);
            else digit.add(log);
        }
        letter.sort((a, b) -> {
            int spa = a.indexOf(' '), spb = b.indexOf(' ');
            String resta = a.substring(spa + 1), restb = b.substring(spb + 1);
            int cmp = resta.compareTo(restb);
            if (cmp != 0) return cmp;
            return a.substring(0, spa).compareTo(b.substring(0, spb));
        });
        List<String> ans = new ArrayList<>(letter);
        ans.addAll(digit);
        return ans.toArray(new String[0]);
    }
}
