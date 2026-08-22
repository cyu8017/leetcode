// LeetCode 3991 - Sort Array Using Prefix Reversals
// https://leetcode.com/problems/sort-array-using-prefix-reversals/

import scala.collection.mutable

object Solution {
  def sortArray(nums: Array[Int], pre: Array[Int]): Int = {
    val n = nums.length
    def key(arr: Array[Int]): String = arr.mkString(",")
    val start = key(nums)
    val target = key(Array.range(0, n))
    if (start == target) return 0

    val lengths = pre.filter(i => i >= 2 && i <= n).distinct.sorted
    val visited = mutable.HashSet[String](start)
    var queue = mutable.Queue[Array[Int]](nums.clone())
    var steps = 0

    while (queue.nonEmpty) {
      steps += 1
      val nextQueue = mutable.Queue[Array[Int]]()
      while (queue.nonEmpty) {
        val cur = queue.dequeue()
        for (i <- lengths) {
          val nxt = cur.clone()
          var l = 0
          var r = i - 1
          while (l < r) {
            val tmp = nxt(l)
            nxt(l) = nxt(r)
            nxt(r) = tmp
            l += 1
            r -= 1
          }
          val k = key(nxt)
          if (k == target) return steps
          if (visited.add(k)) nextQueue.enqueue(nxt)
        }
      }
      queue = nextQueue
    }
    -1
  }
}
