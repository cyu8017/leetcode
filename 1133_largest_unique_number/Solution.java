// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

import java.util.*;

class Solution {
    public int largestUniqueNumber(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int x : nums) count.merge(x, 1, Integer::sum);
        int ans = -1;
        for (Map.Entry<Integer, Integer> e : count.entrySet()) {
            if (e.getValue() == 1) ans = Math.max(ans, e.getKey());
        }
        return ans;
    }
}
