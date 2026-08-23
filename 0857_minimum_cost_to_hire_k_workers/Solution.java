// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

import java.util.*;

class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        int n = quality.length;
        double[][] workers = new double[n][2];
        for (int i = 0; i < n; i++) {
            workers[i][0] = (double) wage[i] / quality[i];
            workers[i][1] = quality[i];
        }
        Arrays.sort(workers, Comparator.comparingDouble(a -> a[0]));
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        long totalQ = 0;
        double ans = 1e18;
        for (double[] w : workers) {
            int q = (int) w[1];
            heap.offer(q);
            totalQ += q;
            if (heap.size() > k) totalQ -= heap.poll();
            if (heap.size() == k) ans = Math.min(ans, totalQ * w[0]);
        }
        return ans;
    }
}
