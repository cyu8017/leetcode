// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maximumWidth(int[] planks) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int x : planks) cnt.put(x, cnt.getOrDefault(x, 0) + 1);
        Map<Integer, Integer> t = new HashMap<>();
        int ans = 0;
        for (Map.Entry<Integer, Integer> e1 : cnt.entrySet()) {
            int x = e1.getKey(), v1 = e1.getValue();
            t.put(x, t.getOrDefault(x, 0) + v1);
            ans = Math.max(ans, t.get(x));
            t.put(x * 2, t.getOrDefault(x * 2, 0) + v1 / 2);
            ans = Math.max(ans, t.get(x * 2));
            for (Map.Entry<Integer, Integer> e2 : cnt.entrySet()) {
                int y = e2.getKey(), v2 = e2.getValue();
                if (y > x) {
                    int key = x + y;
                    t.put(key, t.getOrDefault(key, 0) + Math.min(v1, v2));
                    ans = Math.max(ans, t.get(key));
                }
            }
        }
        return ans;
    }
}
