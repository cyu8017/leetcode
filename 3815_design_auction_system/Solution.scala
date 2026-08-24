// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

class AuctionSystem() {
  private class Bid(val amount: Int, val userId: Int)

  private val bids = new java.util.HashMap[Integer, java.util.Map[Integer, Integer]]()
  private val heaps = new java.util.HashMap[Integer, java.util.PriorityQueue[Bid]]()

  def addBid(userId: Int, itemId: Int, bidAmount: Int): Unit = {
    bids.computeIfAbsent(itemId, _ => new java.util.HashMap[Integer, Integer]()).put(userId, bidAmount)
    heaps.computeIfAbsent(itemId, _ => new java.util.PriorityQueue[Bid]((a: Bid, b: Bid) => {
      if (a.amount != b.amount) Integer.compare(b.amount, a.amount)
      else Integer.compare(b.userId, a.userId)
    })).offer(new Bid(bidAmount, userId))
  }

  def updateBid(userId: Int, itemId: Int, newAmount: Int): Unit = {
    addBid(userId, itemId, newAmount)
  }

  def removeBid(userId: Int, itemId: Int): Unit = {
    val m = bids.get(itemId)
    if (m != null) m.remove(userId)
  }

  def getHighestBidder(itemId: Int): Int = {
    val h = heaps.get(itemId)
    if (h == null) return -1
    val m = bids.getOrDefault(itemId, java.util.Collections.emptyMap[Integer, Integer]())
    while (!h.isEmpty) {
      val top = h.peek()
      val cur = m.get(top.userId)
      if (cur != null && cur == top.amount) return top.userId
      h.poll()
    }
    -1
  }
}
