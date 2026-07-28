// LeetCode 1046 - Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/

import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) pq.offer(s);
        while (pq.size() > 1) {
            int a = pq.poll(), b = pq.poll();
            if (a != b) pq.offer(a - b);
        }
        return pq.isEmpty() ? 0 : pq.peek();
    }
}
