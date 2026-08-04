// LeetCode 1554 - Strings Differ by One Character
// https://leetcode.com/problems/strings-differ-by-one-character/

import java.util.*;

class Solution {
    public boolean differByOne(String[] dict) {
        Set<String> seen = new HashSet<>();
        for (String word : dict) {
            char[] b = word.toCharArray();
            for (int i = 0; i < b.length; i++) {
                char orig = b[i];
                b[i] = '*';
                String pattern = new String(b);
                if (seen.contains(pattern)) {
                    return true;
                }
                seen.add(pattern);
                b[i] = orig;
            }
        }
        return false;
    }
}
