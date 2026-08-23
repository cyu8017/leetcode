// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/

using System.Collections.Generic;

public class Solution {
    public long MaximumScore(int[] nums, string s) {
        long ans = 0;
        var pq = new PriorityQueue<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            pq.Enqueue(nums[i], -nums[i]);
            if (s[i] == '1') {
                ans += pq.Dequeue();
            }
        }
        return ans;
    }
}
