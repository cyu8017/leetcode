// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public long[] mostFrequentIDs(int[] nums, int[] freq) {
        int n = nums.length;
        Map<Integer, Integer> cnt = new HashMap<>();
        Map<Integer, Integer> lazy = new HashMap<>();
        long[] ans = new long[n];
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int i = 0; i < n; i++) {
            int x = nums[i], f = freq[i];
            int old = cnt.getOrDefault(x, 0);
            lazy.put(old, lazy.getOrDefault(old, 0) + 1);
            int neu = old + f;
            cnt.put(x, neu);
            pq.offer(neu);
            while (!pq.isEmpty() && lazy.getOrDefault(pq.peek(), 0) > 0) {
                int top = pq.poll();
                lazy.put(top, lazy.get(top) - 1);
            }
            if (!pq.isEmpty()) ans[i] = pq.peek();
        }
        return ans;
    }
}
