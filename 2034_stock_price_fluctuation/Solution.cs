// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

using System.Collections.Generic;

public class StockPrice {
    private int latestTs = 0;
    private readonly Dictionary<int, int> priceAt = new();
    private readonly PriorityQueue<(int price, int ts), int> maxHeap = new();
    private readonly PriorityQueue<(int price, int ts), int> minHeap = new();

    public StockPrice() {}

    public void Update(int timestamp, int price) {
        priceAt[timestamp] = price;
        if (timestamp >= latestTs) latestTs = timestamp;
        maxHeap.Enqueue((price, timestamp), -price);
        minHeap.Enqueue((price, timestamp), price);
    }

    public int Current() => priceAt[latestTs];

    public int Maximum() {
        while (true) {
            var (price, ts) = maxHeap.Peek();
            if (priceAt[ts] == price) return price;
            maxHeap.Dequeue();
        }
    }

    public int Minimum() {
        while (true) {
            var (price, ts) = minHeap.Peek();
            if (priceAt[ts] == price) return price;
            minHeap.Dequeue();
        }
    }
}
