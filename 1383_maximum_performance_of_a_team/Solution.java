// LeetCode 1383 - Maximum Performance Of A Team
// https://leetcode.com/problems/maximum-performance-of-a-team/

import java.util.*;

class Solution {
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        int[][] eng = new int[n][2];
        for (int i = 0; i < n; i++) {
            eng[i][0] = efficiency[i];
            eng[i][1] = speed[i];
        }
        Arrays.sort(eng, (a, b) -> Integer.compare(b[0], a[0]));
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        long total = 0, ans = 0;
        for (int[] e : eng) {
            pq.offer(e[1]);
            total += e[1];
            if (pq.size() > k) total -= pq.poll();
            ans = Math.max(ans, total * e[0]);
        }
        return (int) (ans % 1_000_000_007);
    }
}
