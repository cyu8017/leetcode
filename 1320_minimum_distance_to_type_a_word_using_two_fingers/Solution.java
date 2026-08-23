// LeetCode 1320 - Minimum Distance To Type A Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

import java.util.*;

class Solution {
    public int minimumDistance(String word) {
        int[] letters = new int[word.length()];
        for (int i = 0; i < word.length(); i++) letters[i] = word.charAt(i) - 'A';
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(26, 0);
        int previous = letters[0];
        for (int i = 1; i < letters.length; i++) {
            int current = letters[i];
            Map<Integer, Integer> nxt = new HashMap<>();
            for (Map.Entry<Integer, Integer> e : dp.entrySet()) {
                int free = e.getKey(), cost = e.getValue();
                nxt.merge(free, cost + dist(previous, current), Math::min);
                nxt.merge(previous, cost + dist(free, current), Math::min);
            }
            dp = nxt;
            previous = current;
        }
        int ans = Integer.MAX_VALUE;
        for (int v : dp.values()) ans = Math.min(ans, v);
        return ans;
    }

    private int dist(int a, int b) {
        if (a == 26) return 0;
        return Math.abs(a / 6 - b / 6) + Math.abs(a % 6 - b % 6);
    }
}
