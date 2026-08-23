// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

import java.util.PriorityQueue;

class Solution {
    public int[] resultsArray(int[][] queries, int k) {
        PriorityQueue<Integer> h = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int d = Math.abs(queries[i][0]) + Math.abs(queries[i][1]);
            h.offer(d);
            if (h.size() > k) {
                h.poll();
            }
            ans[i] = h.size() < k ? -1 : h.peek();
        }
        return ans;
    }
}
