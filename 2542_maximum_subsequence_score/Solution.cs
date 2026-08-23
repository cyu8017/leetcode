// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Array.Sort(idx, (a, b) => nums2[b].CompareTo(nums2[a]));
        var pq = new PriorityQueue<int, int>();
        long sum = 0, ans = 0;
        foreach (int i in idx) {
            pq.Enqueue(nums1[i], nums1[i]);
            sum += nums1[i];
            if (pq.Count > k) {
                sum -= pq.Dequeue();
            }
            if (pq.Count == k) {
                long cand = sum * nums2[i];
                if (cand > ans) ans = cand;
            }
        }
        return ans;
    }
}
