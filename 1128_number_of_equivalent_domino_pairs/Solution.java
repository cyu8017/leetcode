// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

import java.util.*;

class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        Map<Integer, Integer> count = new HashMap<>();
        int ans = 0;
        for (int[] d : dominoes) {
            int a = Math.min(d[0], d[1]), b = Math.max(d[0], d[1]);
            int key = a * 10 + b;
            int c = count.getOrDefault(key, 0);
            ans += c;
            count.put(key, c + 1);
        }
        return ans;
    }
}
