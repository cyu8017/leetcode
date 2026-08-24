// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/

object Solution {
  def maximumScore(nums: Array[Int], s: String): Long = {
    var ans = 0L
    val pq = new java.util.PriorityQueue[Integer]((a: Integer, b: Integer) => Integer.compare(b, a))
    var i = 0
    while (i < nums.length) {
      pq.offer(nums(i))
      if (s.charAt(i) == '1') ans += pq.poll()
      i += 1
    }
    ans
  }
}
