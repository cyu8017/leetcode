// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int largestInteger(int[] nums, int k) {
        int n = nums.length;
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int i = 0; i + k <= n; i++) {
            Set<Integer> seen = new HashSet<>();
            for (int j = i; j < i + k; j++) seen.add(nums[j]);
            for (int x : seen) cnt.merge(x, 1, Integer::sum);
        }
        int ans = -1;
        for (Map.Entry<Integer, Integer> e : cnt.entrySet()) {
            if (e.getValue() == 1 && e.getKey() > ans) ans = e.getKey();
        }
        return ans;
    }
}
