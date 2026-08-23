// LeetCode 2135 - Count Words Obtained After Adding a Letter
// https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

import java.util.*;

class Solution {
    private int mask(String w) {
        int m = 0;
        for (int i = 0; i < w.length(); i++) m |= 1 << (w.charAt(i) - 'a');
        return m;
    }

    public int wordCount(String[] startWords, String[] targetWords) {
        Set<Integer> have = new HashSet<>();
        for (String w : startWords) have.add(mask(w));
        int ans = 0;
        for (String w : targetWords) {
            int m = mask(w);
            for (int i = 0; i < w.length(); i++) {
                if (have.contains(m ^ (1 << (w.charAt(i) - 'a')))) { ans++; break; }
            }
        }
        return ans;
    }
}
