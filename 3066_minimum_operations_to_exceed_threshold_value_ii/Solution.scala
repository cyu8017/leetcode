// LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

object Solution {
  def minOperations(nums: Array[Int], k: Int): Int = {
    val pq = new java.util.PriorityQueue[java.lang.Long]()
    nums.foreach(x => pq.offer(x.toLong))
    var ans = 0
    while (pq.size() > 1 && pq.peek() < k) {
      val x = pq.poll()
      val y = pq.poll()
      pq.offer(x * 2 + y)
      ans += 1
    }
    ans
  }
}
