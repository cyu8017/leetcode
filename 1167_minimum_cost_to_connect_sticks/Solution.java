// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

import java.util.*;

class Solution {
    public int connectSticks(int[] sticks) {
        if (sticks.length <= 1) return 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s : sticks) pq.offer(s);
        int ans = 0;
        while (pq.size() > 1) {
            int cost = pq.poll() + pq.poll();
            ans += cost;
            pq.offer(cost);
        }
        return ans;
    }
}
