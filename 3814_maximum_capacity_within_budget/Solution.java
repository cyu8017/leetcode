// LeetCode 3814 - Maximum Capacity Within Budget
// https://leetcode.com/problems/maximum_capacity_within_budget/

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public int maxCapacity(int[] costs, int[] capacity, int budget) {
        List<int[]> arr = new ArrayList<>();
        for (int k = 0; k < costs.length; k++) {
            if (costs[k] < budget) arr.add(new int[]{costs[k], capacity[k]});
        }
        if (arr.isEmpty()) return 0;
        arr.sort(Comparator.comparingInt(a -> a[0]));
        int m = arr.size();
        boolean[] alive = new boolean[m];
        java.util.Arrays.fill(alive, true);
        PriorityQueue<int[]> h = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(b[0], a[0]);
            return Integer.compare(b[1], a[1]);
        });
        for (int i = 0; i < m; i++) h.offer(new int[]{arr.get(i)[1], i});
        while (!h.isEmpty() && !alive[h.peek()[1]]) h.poll();
        int ans = h.peek()[0];
        int i = 0, j = m - 1;
        while (i < j) {
            alive[i] = false;
            while (i < j && arr.get(i)[0] + arr.get(j)[0] >= budget) {
                alive[j] = false;
                j--;
            }
            while (!h.isEmpty() && !alive[h.peek()[1]]) h.poll();
            if (!h.isEmpty()) ans = Math.max(ans, arr.get(i)[1] + h.peek()[0]);
            i++;
        }
        return ans;
    }
}
