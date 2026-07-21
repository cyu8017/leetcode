// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

object Solution {
  def getNumberOfBacklogOrders(orders: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val buy = scala.collection.mutable.PriorityQueue.empty[(Int, Int)]
    val sell = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._1).reverse)

    for (order <- orders) {
      val price = order(0)
      var amount = order(1)
      val orderType = order(2)
      if (orderType == 0) buy.enqueue((price, amount))
      else sell.enqueue((price, amount))

      while (buy.nonEmpty && sell.nonEmpty && buy.head._1 >= sell.head._1) {
        val (bp, ba) = buy.dequeue()
        val (sp, sa) = sell.dequeue()
        val matched = math.min(ba, sa)
        val buyLeft = ba - matched
        val sellLeft = sa - matched
        if (buyLeft > 0) buy.enqueue((bp, buyLeft))
        if (sellLeft > 0) sell.enqueue((sp, sellLeft))
      }
    }

    var total = 0L
    while (buy.nonEmpty) total = (total + buy.dequeue()._2) % MOD
    while (sell.nonEmpty) total = (total + sell.dequeue()._2) % MOD
    total.toInt
  }
}
