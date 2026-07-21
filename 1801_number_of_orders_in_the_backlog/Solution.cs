// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

using System;
using System.Collections.Generic;

public class Solution {
    public int GetNumberOfBacklogOrders(int[][] orders) {
        const int MOD = 1_000_000_007;
        var buy = new PriorityQueue<(int price, int amount), int>();
        var sell = new PriorityQueue<(int price, int amount), int>();

        foreach (var order in orders) {
            int price = order[0], amount = order[1], orderType = order[2];
            if (orderType == 0) {
                buy.Enqueue((price, amount), -price);
            } else {
                sell.Enqueue((price, amount), price);
            }

            while (buy.Count > 0 && sell.Count > 0 && buy.Peek().price >= sell.Peek().price) {
                var (buyPrice, buyAmount) = buy.Dequeue();
                var (sellPrice, sellAmount) = sell.Dequeue();
                int matched = Math.Min(buyAmount, sellAmount);
                buyAmount -= matched;
                sellAmount -= matched;
                if (buyAmount > 0) buy.Enqueue((buyPrice, buyAmount), -buyPrice);
                if (sellAmount > 0) sell.Enqueue((sellPrice, sellAmount), sellPrice);
            }
        }

        long total = 0;
        while (buy.Count > 0) total = (total + buy.Dequeue().amount) % MOD;
        while (sell.Count > 0) total = (total + sell.Dequeue().amount) % MOD;
        return (int)total;
    }
}
