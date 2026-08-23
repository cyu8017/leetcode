// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

using System.Collections.Generic;

public class Solution {
    public long TotalCost(int[] costs, int k, int candidates) {
        var leftH = new PriorityQueue<(int cost, int idx), (int cost, int idx)>();
        var rightH = new PriorityQueue<(int cost, int idx), (int cost, int idx)>();
        int n = costs.Length;
        int l = 0, r = n - 1;
        while (l <= r && leftH.Count < candidates) {
            leftH.Enqueue((costs[l], l), (costs[l], l));
            l++;
        }
        while (r >= l && rightH.Count < candidates) {
            rightH.Enqueue((costs[r], r), (costs[r], r));
            r--;
        }
        long ans = 0;
        for (int t = 0; t < k; t++) {
            bool useLeft = false;
            if (leftH.Count > 0 && rightH.Count > 0) {
                var lt = leftH.Peek();
                var rt = rightH.Peek();
                if (lt.cost < rt.cost || (lt.cost == rt.cost && lt.idx <= rt.idx))
                    useLeft = true;
            } else if (leftH.Count > 0) {
                useLeft = true;
            }
            if (useLeft) {
                ans += leftH.Dequeue().cost;
                if (l <= r) {
                    leftH.Enqueue((costs[l], l), (costs[l], l));
                    l++;
                }
            } else {
                ans += rightH.Dequeue().cost;
                if (l <= r) {
                    rightH.Enqueue((costs[r], r), (costs[r], r));
                    r--;
                }
            }
        }
        return ans;
    }
}
