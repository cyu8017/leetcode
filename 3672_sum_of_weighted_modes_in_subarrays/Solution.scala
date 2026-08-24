// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

object Solution {
  def modeWeight(nums: Array[Int], k: Int): Long = {
    val cnt = new java.util.HashMap[Integer, Integer]()
    val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) =>
      if (a(0) != b(0)) Integer.compare(b(0), a(0)) else Integer.compare(a(1), b(1))
    )

    def getMode(): Long = {
      while (true) {
        val top = pq.peek()
        val freq = top(0)
        val `val` = -top(1)
        if (cnt.getOrDefault(`val`, 0) == freq) return 1L * freq * `val`
        pq.poll()
      }
      0L
    }

    var i = 0
    while (i < k) {
      val x = nums(i)
      cnt.merge(x, 1, Integer.sum)
      pq.offer(Array(cnt.get(x), -x))
      i += 1
    }
    var ans = getMode()
    i = k
    while (i < nums.length) {
      val x = nums(i)
      val y = nums(i - k)
      cnt.merge(x, 1, Integer.sum)
      cnt.merge(y, -1, Integer.sum)
      pq.offer(Array(cnt.get(x), -x))
      pq.offer(Array(cnt.get(y), -y))
      ans += getMode()
      i += 1
    }
    ans
  }
}
