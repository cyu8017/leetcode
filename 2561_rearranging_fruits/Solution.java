// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public long minCost(int[] basket1, int[] basket2) {
        Map<Integer, Integer> freq = new HashMap<>();
        int mn = Integer.MAX_VALUE;
        for (int x : basket1) {
            freq.put(x, freq.getOrDefault(x, 0) + 1);
            mn = Math.min(mn, x);
        }
        for (int x : basket2) {
            freq.put(x, freq.getOrDefault(x, 0) - 1);
            mn = Math.min(mn, x);
        }
        List<Integer> extra = new ArrayList<>();
        for (Map.Entry<Integer, Integer> kv : freq.entrySet()) {
            if (kv.getValue() % 2 != 0) return -1;
            for (int i = 0; i < Math.abs(kv.getValue()) / 2; ++i) extra.add(kv.getKey());
        }
        Collections.sort(extra);
        long ans = 0;
        for (int i = 0; i < extra.size() / 2; ++i) {
            ans += Math.min(extra.get(i), 2L * mn);
        }
        return ans;
    }
}
