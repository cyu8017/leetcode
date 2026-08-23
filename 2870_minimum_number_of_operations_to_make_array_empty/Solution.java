// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minOperations(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int v : nums) freq.merge(v, 1, Integer::sum);
        int ans = 0;
        for (int c : freq.values()) {
            if (c == 1) return -1;
            ans += (c + 2) / 3;
        }
        return ans;
    }
}
