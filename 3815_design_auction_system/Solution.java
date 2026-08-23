// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design_auction_system/

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class AuctionSystem {
    private static class Bid {
        int amount, userId;
        Bid(int amount, int userId) {
            this.amount = amount;
            this.userId = userId;
        }
    }

    private final Map<Integer, Map<Integer, Integer>> bids = new HashMap<>();
    private final Map<Integer, PriorityQueue<Bid>> heaps = new HashMap<>();

    public AuctionSystem() {}

    public void addBid(int userId, int itemId, int bidAmount) {
        bids.computeIfAbsent(itemId, k -> new HashMap<>()).put(userId, bidAmount);
        heaps.computeIfAbsent(itemId, k -> new PriorityQueue<>((a, b) -> {
            if (a.amount != b.amount) return Integer.compare(b.amount, a.amount);
            return Integer.compare(b.userId, a.userId);
        })).offer(new Bid(bidAmount, userId));
    }

    public void updateBid(int userId, int itemId, int newAmount) {
        addBid(userId, itemId, newAmount);
    }

    public void removeBid(int userId, int itemId) {
        Map<Integer, Integer> m = bids.get(itemId);
        if (m != null) m.remove(userId);
    }

    public int getHighestBidder(int itemId) {
        PriorityQueue<Bid> h = heaps.get(itemId);
        if (h == null) return -1;
        Map<Integer, Integer> m = bids.getOrDefault(itemId, Map.of());
        while (!h.isEmpty()) {
            Bid top = h.peek();
            Integer cur = m.get(top.userId);
            if (cur != null && cur == top.amount) return top.userId;
            h.poll();
        }
        return -1;
    }
}
