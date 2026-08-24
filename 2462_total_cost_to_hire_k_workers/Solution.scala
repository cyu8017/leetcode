// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

object Solution {
  def totalCost(costs: Array[Int], k: Int, candidates: Int): Long = {
    implicit val ord: Ordering[(Int, Int)] = Ordering.Tuple2[Int, Int]
    val leftH = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](ord.reverse)
    val rightH = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](ord.reverse)
    val n = costs.length
    var l = 0
    var r = n - 1
    while (l <= r && leftH.size < candidates) {
      leftH.enqueue((costs(l), l))
      l += 1
    }
    while (r >= l && rightH.size < candidates) {
      rightH.enqueue((costs(r), r))
      r -= 1
    }
    var ans = 0L
    var t = 0
    while (t < k) {
      var useLeft = false
      if (leftH.nonEmpty && rightH.nonEmpty) {
        val lt = leftH.head
        val rt = rightH.head
        if (lt._1 < rt._1 || (lt._1 == rt._1 && lt._2 <= rt._2)) useLeft = true
      } else if (leftH.nonEmpty) {
        useLeft = true
      }
      if (useLeft) {
        ans += leftH.dequeue()._1
        if (l <= r) {
          leftH.enqueue((costs(l), l))
          l += 1
        }
      } else {
        ans += rightH.dequeue()._1
        if (l <= r) {
          rightH.enqueue((costs(r), r))
          r -= 1
        }
      }
      t += 1
    }
    ans
  }
}
