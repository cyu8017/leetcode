// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public long maxTotal(int[] value, int[] limit) {
        Map<Integer, List<Integer>> g = new HashMap<>();
        for (int i = 0; i < value.length; i++)
            g.computeIfAbsent(limit[i], x -> new ArrayList<>()).add(value[i]);
        long ans = 0;
        for (Map.Entry<Integer, List<Integer>> e : g.entrySet()) {
            int lim = e.getKey();
            List<Integer> vs = e.getValue();
            vs.sort(Collections.reverseOrder());
            for (int i = 0; i < Math.min(lim, vs.size()); i++) ans += vs.get(i);
        }
        return ans;
    }
}
