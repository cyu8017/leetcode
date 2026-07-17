// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

import java.util.PriorityQueue;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int getNumberOfBacklogOrders(int[][] orders) {
        PriorityQueue<int[]> buy = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        PriorityQueue<int[]> sell = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for (int[] order : orders) {
            int price = order[0];
            int amount = order[1];
            int type = order[2];
            if (type == 0) {
                buy.offer(new int[] { price, amount });
            } else {
                sell.offer(new int[] { price, amount });
            }

            while (!buy.isEmpty() && !sell.isEmpty() && buy.peek()[0] >= sell.peek()[0]) {
                int[] buyOrder = buy.poll();
                int[] sellOrder = sell.poll();
                int buyPrice = buyOrder[0];
                int buyAmount = buyOrder[1];
                int sellPrice = sellOrder[0];
                int sellAmount = sellOrder[1];
                int matched = Math.min(buyAmount, sellAmount);
                buyAmount -= matched;
                sellAmount -= matched;
                if (buyAmount > 0) {
                    buy.offer(new int[] { buyPrice, buyAmount });
                }
                if (sellAmount > 0) {
                    sell.offer(new int[] { sellPrice, sellAmount });
                }
            }
        }

        long total = 0;
        for (int[] entry : buy) {
            total = (total + entry[1]) % MOD;
        }
        for (int[] entry : sell) {
            total = (total + entry[1]) % MOD;
        }
        return (int) total;
    }
}
