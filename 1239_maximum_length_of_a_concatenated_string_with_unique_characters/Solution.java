// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

import java.util.*;

class Solution {
    public int maxLength(String[] arr) {
        List<int[]> masks = new ArrayList<>();
        masks.add(new int[]{0, 0});
        for (String word : arr) {
            int mask = 0;
            boolean ok = true;
            for (char ch : word.toCharArray()) {
                int bit = 1 << (ch - 'a');
                if ((mask & bit) != 0) {
                    ok = false;
                    break;
                }
                mask |= bit;
            }
            if (!ok) continue;
            int len = word.length();
            List<int[]> next = new ArrayList<>(masks);
            for (int[] state : masks) {
                if ((state[0] & mask) == 0) {
                    next.add(new int[]{state[0] | mask, state[1] + len});
                }
            }
            masks = next;
        }
        int best = 0;
        for (int[] state : masks) best = Math.max(best, state[1]);
        return best;
    }
}

