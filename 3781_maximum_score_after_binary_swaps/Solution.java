// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum_score_after_binary_swaps/

import java.util.PriorityQueue;

class Solution {
    public long maximumScore(int[] nums, String s) {
        long ans = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        for (int i = 0; i < nums.length; i++) {
            pq.offer(nums[i]);
            if (s.charAt(i) == '1') {
                ans += pq.poll();
            }
        }
        return ans;
    }
}
