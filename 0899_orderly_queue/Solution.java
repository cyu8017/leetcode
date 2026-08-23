// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

import java.util.Arrays;

class Solution {
    public String orderlyQueue(String s, int k) {
        if (k > 1) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            return new String(chars);
        }
        String best = s;
        for (int i = 1; i < s.length(); i++) {
            String cand = s.substring(i) + s.substring(0, i);
            if (cand.compareTo(best) < 0) best = cand;
        }
        return best;
    }
}
