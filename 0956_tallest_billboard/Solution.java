// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

import java.util.*;

class Solution {
    public int tallestBillboard(int[] rods) {
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 0);
        for (int rod : rods) {
            List<Map.Entry<Integer, Integer>> cur = new ArrayList<>(dp.entrySet());
            for (Map.Entry<Integer, Integer> kv : cur) {
                int diff = kv.getKey(), taller = kv.getValue();
                int key1 = diff + rod;
                dp.put(key1, Math.max(dp.getOrDefault(key1, 0), taller + rod));
                int nd = Math.abs(diff - rod);
                int nt = diff >= rod ? taller : taller - diff + rod;
                dp.put(nd, Math.max(dp.getOrDefault(nd, 0), nt));
            }
        }
        return dp.getOrDefault(0, 0);
    }
}
