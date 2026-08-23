// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

using System.Collections.Generic;

public class AuctionSystem {
    Dictionary<int, Dictionary<int, int>> bids = new Dictionary<int, Dictionary<int, int>>();
    Dictionary<int, PriorityQueue<(int amount, int userId), (int, int)>> heaps =
        new Dictionary<int, PriorityQueue<(int amount, int userId), (int, int)>>();

    public AuctionSystem() {}

    public void AddBid(int userId, int itemId, int bidAmount) {
        if (!bids.ContainsKey(itemId)) bids[itemId] = new Dictionary<int, int>();
        bids[itemId][userId] = bidAmount;
        if (!heaps.ContainsKey(itemId))
            heaps[itemId] = new PriorityQueue<(int, int), (int, int)>();
        heaps[itemId].Enqueue((bidAmount, userId), (-bidAmount, -userId));
    }

    public void UpdateBid(int userId, int itemId, int newAmount) {
        AddBid(userId, itemId, newAmount);
    }

    public void RemoveBid(int userId, int itemId) {
        if (bids.ContainsKey(itemId)) bids[itemId].Remove(userId);
    }

    public int GetHighestBidder(int itemId) {
        if (!heaps.ContainsKey(itemId)) return -1;
        var h = heaps[itemId];
        while (h.Count > 0) {
            var top = h.Peek();
            if (bids.ContainsKey(itemId) && bids[itemId].ContainsKey(top.userId) &&
                bids[itemId][top.userId] == top.amount) return top.userId;
            h.Dequeue();
        }
        return -1;
    }
}
