// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] minDistinctFreqPair(int[] nums) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int v : nums) cnt.put(v, cnt.getOrDefault(v, 0) + 1);
        int x = nums[0];
        for (int v : nums) x = Math.min(x, v);
        int minY = Integer.MAX_VALUE;
        for (int y : cnt.keySet()) {
            if (y < minY && !cnt.get(x).equals(cnt.get(y))) minY = y;
        }
        if (minY == Integer.MAX_VALUE) return new int[] { -1, -1 };
        return new int[] { x, minY };
    }
}
