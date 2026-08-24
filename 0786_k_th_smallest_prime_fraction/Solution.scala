// LeetCode 0786 - K-th Smallest Prime Fraction
// https://leetcode.com/problems/k-th-smallest-prime-fraction/

object Solution {
  def kthSmallestPrimeFraction(arr: Array[Int], k: Int): Array[Int] = {
    val n = arr.length
    val heap = scala.collection.mutable.PriorityQueue.empty[(Int, Int)](
      Ordering.by[(Int, Int), Double] { case (i, j) => arr(i).toDouble / arr(j) }.reverse
    )
    var i = 0
    while (i < n - 1) {
      heap.enqueue((i, n - 1))
      i += 1
    }
    var t = 0
    while (t < k - 1) {
      val (ii, jj) = heap.dequeue()
      if (jj - 1 > ii) heap.enqueue((ii, jj - 1))
      t += 1
    }
    val (a, b) = heap.dequeue()
    Array(arr(a), arr(b))
  }
}
