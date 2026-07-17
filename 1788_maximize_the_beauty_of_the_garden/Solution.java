// LeetCode 1788 - Maximize the Beauty of the Garden
// https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maximumBeauty(int[] flowers) {
        Map<Integer, Integer> first = new HashMap<>();
        long[] prefix = new long[flowers.length + 1];
        for (int i = 0; i < flowers.length; i++) {
            prefix[i + 1] = prefix[i] + Math.max(flowers[i], 0);
        }
        long best = Long.MIN_VALUE;
        for (int i = 0; i < flowers.length; i++) {
            int value = flowers[i];
            if (first.containsKey(value)) {
                int left = first.get(value);
                long between = prefix[i] - prefix[left + 1];
                best = Math.max(best, (long) flowers[left] + flowers[i] + between);
            } else {
                first.put(value, i);
            }
        }
        return (int) best;
    }
}
