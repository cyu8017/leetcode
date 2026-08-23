// LeetCode 0786 - K-th Smallest Prime Fraction
// https://leetcode.com/problems/k-th-smallest-prime-fraction/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] KthSmallestPrimeFraction(int[] arr, int k) {
        int n = arr.Length;
        var heap = new PriorityQueue<(int i, int j), double>();
        for (int i = 0; i < n - 1; i++) {
            heap.Enqueue((i, n - 1), (double)arr[i] / arr[n - 1]);
        }
        for (int t = 0; t < k - 1; t++) {
            var (i, j) = heap.Dequeue();
            if (j - 1 > i) heap.Enqueue((i, j - 1), (double)arr[i] / arr[j - 1]);
        }
        var top = heap.Dequeue();
        return new int[] { arr[top.i], arr[top.j] };
    }
}
