// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

import java.util.*;

class StockPrice {
    private int latestTs = 0;
    private final Map<Integer, Integer> priceAt = new HashMap<>();
    private final PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
    private final PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));

    public StockPrice() {}

    public void update(int timestamp, int price) {
        priceAt.put(timestamp, price);
        if (timestamp >= latestTs) latestTs = timestamp;
        maxHeap.offer(new int[] { price, timestamp });
        minHeap.offer(new int[] { price, timestamp });
    }

    public int current() {
        return priceAt.get(latestTs);
    }

    public int maximum() {
        while (true) {
            int[] top = maxHeap.peek();
            if (priceAt.get(top[1]) == top[0]) return top[0];
            maxHeap.poll();
        }
    }

    public int minimum() {
        while (true) {
            int[] top = minHeap.peek();
            if (priceAt.get(top[1]) == top[0]) return top[0];
            minHeap.poll();
        }
    }
}
