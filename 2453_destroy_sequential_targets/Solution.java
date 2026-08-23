// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int destroyTargets(int[] nums, int space) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int x : nums) {
            int m = x % space;
            cnt.put(m, cnt.getOrDefault(m, 0) + 1);
        }
        int bestCnt = 0;
        for (int c : cnt.values()) if (c > bestCnt) bestCnt = c;
        int ans = 1000000000;
        for (Map.Entry<Integer, Integer> kv : cnt.entrySet()) {
            if (kv.getValue() == bestCnt) {
                for (int x : nums) {
                    if (x % space == kv.getKey() && x < ans) ans = x;
                }
            }
        }
        return ans;
    }
}
