// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design_auction_system/

import java.util.PriorityQueue

class AuctionSystem {
    private class Bid(val amount: Int, val userId: Int)

    private val bids = HashMap<Int, HashMap<Int, Int>>()
    private val heaps = HashMap<Int, PriorityQueue<Bid>>()

    fun addBid(userId: Int, itemId: Int, bidAmount: Int) {
        bids.getOrPut(itemId) { HashMap() }[userId] = bidAmount
        heaps.getOrPut(itemId) {
            PriorityQueue { a, b ->
                if (a.amount != b.amount) b.amount.compareTo(a.amount)
                else b.userId.compareTo(a.userId)
            }
        }.offer(Bid(bidAmount, userId))
    }

    fun updateBid(userId: Int, itemId: Int, newAmount: Int) {
        addBid(userId, itemId, newAmount)
    }

    fun removeBid(userId: Int, itemId: Int) {
        bids[itemId]?.remove(userId)
    }

    fun getHighestBidder(itemId: Int): Int {
        val h = heaps[itemId] ?: return -1
        val m = bids.getOrDefault(itemId, HashMap())
        while (h.isNotEmpty()) {
            val top = h.peek()
            val cur = m[top.userId]
            if (cur != null && cur == top.amount) return top.userId
            h.poll()
        }
        return -1
    }
}
