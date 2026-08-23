// LeetCode 2530 - Maximal Score After Applying K Operations
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

import java.util.PriorityQueue;

class Solution {
    public long maxKelements(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        for (int x : nums) pq.offer(x);
        long ans = 0;
        for (int i = 0; i < k; i++) {
            int x = pq.poll();
            ans += x;
            pq.offer((x + 2) / 3);
        }
        return ans;
    }
}
