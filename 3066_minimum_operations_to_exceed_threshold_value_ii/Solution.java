// LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

import java.util.PriorityQueue;

class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for (int x : nums) pq.offer((long) x);
        int ans = 0;
        while (pq.size() > 1 && pq.peek() < k) {
            long x = pq.poll();
            long y = pq.poll();
            pq.offer(x * 2 + y);
            ans++;
        }
        return ans;
    }
}
