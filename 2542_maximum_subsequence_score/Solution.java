// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Integer.compare(nums2[b], nums2[a]));
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        long sum = 0, ans = 0;
        for (int i : idx) {
            pq.offer(nums1[i]);
            sum += nums1[i];
            if (pq.size() > k) sum -= pq.poll();
            if (pq.size() == k) {
                long cand = sum * nums2[i];
                if (cand > ans) ans = cand;
            }
        }
        return ans;
    }
}
