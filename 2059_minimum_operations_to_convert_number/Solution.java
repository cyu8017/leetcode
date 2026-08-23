// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

import java.util.*;

class Solution {
    public int minimumOperations(int[] nums, int start, int goal) {
        if (start == goal) return 0;
        Set<Integer> vis = new HashSet<>();
        vis.add(start);
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.offer(start);
        int steps = 0;
        while (!q.isEmpty()) {
            steps++;
            int sz = q.size();
            while (sz-- > 0) {
                int cur = q.poll();
                for (int x : nums) {
                    for (int nxt : new int[] { cur + x, cur - x, cur ^ x }) {
                        if (nxt == goal) return steps;
                        if (nxt >= 0 && nxt <= 1000 && vis.add(nxt)) q.offer(nxt);
                    }
                }
            }
        }
        return -1;
    }
}
