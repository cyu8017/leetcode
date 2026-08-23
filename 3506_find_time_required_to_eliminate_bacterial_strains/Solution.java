// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

import java.util.PriorityQueue;

class Solution {
    public long minEliminationTime(int[] timeReq, int splitTime) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int v : timeReq) pq.offer(v);
        while (pq.size() > 1) {
            pq.poll();
            int x = pq.poll();
            pq.offer(x + splitTime);
        }
        return pq.peek();
    }
}
