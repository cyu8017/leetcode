// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

import java.util.PriorityQueue;

class MedianFinder {
    private final PriorityQueue<Integer> small = new PriorityQueue<>((a, b) -> b - a);
    private final PriorityQueue<Integer> large = new PriorityQueue<>();

    public void addNum(int num) {
        small.offer(num);
        large.offer(small.poll());
        if (large.size() > small.size()) {
            small.offer(large.poll());
        }
    }

    public double findMedian() {
        if (small.size() > large.size()) {
            return small.peek();
        }
        return (small.peek() + large.peek()) / 2.0;
    }
}
