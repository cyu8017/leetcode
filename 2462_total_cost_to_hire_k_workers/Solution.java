// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

import java.util.PriorityQueue;

class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        PriorityQueue<int[]> leftH = new PriorityQueue<>((a, b) ->
            a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        PriorityQueue<int[]> rightH = new PriorityQueue<>((a, b) ->
            a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        int n = costs.length;
        int l = 0, r = n - 1;
        while (l <= r && leftH.size() < candidates) {
            leftH.offer(new int[]{costs[l], l});
            l++;
        }
        while (r >= l && rightH.size() < candidates) {
            rightH.offer(new int[]{costs[r], r});
            r--;
        }
        long ans = 0;
        for (int t = 0; t < k; t++) {
            boolean useLeft = false;
            if (!leftH.isEmpty() && !rightH.isEmpty()) {
                int[] lt = leftH.peek(), rt = rightH.peek();
                if (lt[0] < rt[0] || (lt[0] == rt[0] && lt[1] <= rt[1])) useLeft = true;
            } else if (!leftH.isEmpty()) {
                useLeft = true;
            }
            if (useLeft) {
                ans += leftH.poll()[0];
                if (l <= r) {
                    leftH.offer(new int[]{costs[l], l});
                    l++;
                }
            } else {
                ans += rightH.poll()[0];
                if (l <= r) {
                    rightH.offer(new int[]{costs[r], r});
                    r--;
                }
            }
        }
        return ans;
    }
}
