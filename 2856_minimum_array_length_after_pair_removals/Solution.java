// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int minLengthAfterRemovals(List<Integer> nums) {
        int n = nums.size(), mx = 0;
        Map<Integer, Integer> freq = new HashMap<>();
        for (int v : nums) mx = Math.max(mx, freq.merge(v, 1, Integer::sum));
        if (mx <= n / 2) return n % 2;
        return 2 * mx - n;
    }
}
