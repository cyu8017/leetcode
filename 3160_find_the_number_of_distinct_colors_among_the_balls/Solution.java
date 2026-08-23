// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        Map<Integer, Integer> g = new HashMap<>();
        Map<Integer, Integer> cnt = new HashMap<>();
        int[] ans = new int[queries.length];
        int ai = 0;
        for (int[] q : queries) {
            int x = q[0], y = q[1];
            cnt.put(y, cnt.getOrDefault(y, 0) + 1);
            Integer old = g.get(x);
            if (old != null) {
                int nv = cnt.get(old) - 1;
                if (nv == 0) cnt.remove(old);
                else cnt.put(old, nv);
            }
            g.put(x, y);
            ans[ai++] = cnt.size();
        }
        return ans;
    }
}
