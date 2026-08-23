// LeetCode 0703 - Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/

using System.Collections.Generic;

public class KthLargest {
    private readonly int k;
    private readonly PriorityQueue<int, int> heap = new PriorityQueue<int, int>();

    public KthLargest(int k, int[] nums) {
        this.k = k;
        foreach (int num in nums) Add(num);
    }

    public int Add(int val) {
        heap.Enqueue(val, val);
        if (heap.Count > k) heap.Dequeue();
        return heap.Peek();
    }
}
