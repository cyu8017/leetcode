// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

object Solution {
  def maxHammingDistances(nums: Array[Int], m: Int): Array[Int] = {
    val dist = Array.fill(1 << m)(-1)
    var q = scala.collection.mutable.ArrayBuffer.empty[Int]
    nums.foreach { x =>
      dist(x) = 0
      q += x
    }
    var k = 1
    while (q.nonEmpty) {
      val t = scala.collection.mutable.ArrayBuffer.empty[Int]
      q.foreach { x =>
        var i = 0
        while (i < m) {
          val y = x ^ (1 << i)
          if (dist(y) == -1) {
            dist(y) = k
            t += y
          }
          i += 1
        }
      }
      q = t
      k += 1
    }
    var i = 0
    while (i < nums.length) {
      val x = nums(i)
      nums(i) = m - dist(x ^ ((1 << m) - 1))
      i += 1
    }
    nums
  }
}
