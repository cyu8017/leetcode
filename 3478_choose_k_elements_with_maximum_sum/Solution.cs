// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

using System;
using System.Collections.Generic;

public class Solution {
    public long[] FindMaxSum(int[] nums1, int[] nums2, int k) {
        int n = nums1.Length;
        var arr = new (int v1, int v2, int i)[n];
        for (int i = 0; i < n; i++) arr[i] = (nums1[i], nums2[i], i);
        Array.Sort(arr, (a, b) => a.v1.CompareTo(b.v1));
        long[] ans = new long[n];
        var h = new PriorityQueue<int, int>();
        long sum = 0;
        for (int i = 0; i < n;) {
            int v = arr[i].v1;
            int start = i;
            while (i < n && arr[i].v1 == v) i++;
            for (int t = start; t < i; t++) ans[arr[t].i] = sum;
            for (int t = start; t < i; t++) {
                h.Enqueue(arr[t].v2, arr[t].v2);
                sum += arr[t].v2;
                if (h.Count > k) {
                    sum -= h.Dequeue();
                }
            }
        }
        return ans;
    }
}
