// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

object Solution {
  def kSum(nums: Array[Int], k: Int): Long = {
    var total = 0L
    val n = nums.length
    val absNums = Array.fill(n)(0)
    var i = 0
    while (i < n) {
      if (nums(i) >= 0) {
        total += nums(i)
        absNums(i) = nums(i)
      } else absNums(i) = -nums(i)
      i += 1
    }
    java.util.Arrays.sort(absNums)
    val h = scala.collection.mutable.PriorityQueue.empty[(Long, Int)]
    h.enqueue((total, 0))
    var t = 0
    while (t < k - 1) {
      val (sum, idx) = h.dequeue()
      if (idx < absNums.length) {
        h.enqueue((sum - absNums(idx), idx + 1))
        if (idx > 0) h.enqueue((sum - absNums(idx) + absNums(idx - 1), idx + 1))
      }
      t += 1
    }
    h.head._1
  }
}
