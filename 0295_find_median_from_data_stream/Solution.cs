// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

using System.Collections.Generic;

public class MedianFinder {
    private readonly PriorityQueue<int, int> small = new();
    private readonly PriorityQueue<int, int> large = new();

    public void AddNum(int num) {
        small.Enqueue(num, -num);
        int moved = small.Dequeue();
        large.Enqueue(moved, moved);
        if (large.Count > small.Count) {
            int rebalanced = large.Dequeue();
            small.Enqueue(rebalanced, -rebalanced);
        }
    }

    public double FindMedian() {
        if (small.Count > large.Count) {
            return small.Peek();
        }
        return (small.Peek() + large.Peek()) / 2.0;
    }
}
