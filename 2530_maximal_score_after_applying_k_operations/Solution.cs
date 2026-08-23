// LeetCode 2530 - Maximal Score After Applying K Operations
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

using System.Collections.Generic;

public class Solution {
    public long MaxKelements(int[] nums, int k) {
        var pq = new PriorityQueue<int, int>();
        foreach (int x in nums) pq.Enqueue(x, -x);
        long ans = 0;
        for (int i = 0; i < k; i++) {
            int x = pq.Dequeue();
            ans += x;
            int nxt = (x + 2) / 3;
            pq.Enqueue(nxt, -nxt);
        }
        return ans;
    }
}
