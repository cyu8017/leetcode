// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice() {
  private var latestTs = 0
  private val priceAt = scala.collection.mutable.Map.empty[Int, Int]
  private val maxHeap = scala.collection.mutable.PriorityQueue.empty[(Int, Int)]
  private val minHeap = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._1).reverse)

  def update(timestamp: Int, price: Int): Unit = {
    priceAt(timestamp) = price
    if (timestamp >= latestTs) latestTs = timestamp
    maxHeap.enqueue((price, timestamp))
    minHeap.enqueue((price, timestamp))
  }

  def current(): Int = priceAt(latestTs)

  def maximum(): Int = {
    while (true) {
      val (p, ts) = maxHeap.head
      if (priceAt(ts) == p) return p
      maxHeap.dequeue()
    }
    0
  }

  def minimum(): Int = {
    while (true) {
      val (p, ts) = minHeap.head
      if (priceAt(ts) == p) return p
      minHeap.dequeue()
    }
    0
  }
}
