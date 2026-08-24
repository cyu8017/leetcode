// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

import java.util.*;

class Solution {
    public int minAreaRect(int[][] points) {
        TreeMap<Integer, List<Integer>> byX = new TreeMap<>();
        for (int[] p : points) {
            byX.computeIfAbsent(p[0], k -> new ArrayList<>()).add(p[1]);
        }
        Map<String, Integer> last = new HashMap<>();
        long ans = Long.MAX_VALUE;
        for (Map.Entry<Integer, List<Integer>> kv : byX.entrySet()) {
            int x = kv.getKey();
            List<Integer> ys = kv.getValue();
            Collections.sort(ys);
            for (int i = 0; i < ys.size(); i++) {
                for (int j = i + 1; j < ys.size(); j++) {
                    String key = ys.get(i) + "#" + ys.get(j);
                    if (last.containsKey(key)) {
                        ans = Math.min(ans, (long) Math.abs(x - last.get(key)) * (ys.get(j) - ys.get(i)));
                    }
                    last.put(key, x);
                }
            }
        }
        return ans == Long.MAX_VALUE ? 0 : (int) ans;
    }
}
