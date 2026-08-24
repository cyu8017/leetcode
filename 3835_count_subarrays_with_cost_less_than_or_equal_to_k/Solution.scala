// LeetCode 3835 - Count Subarrays With Cost Less Than Or Equal To K
// https://leetcode.com/problems/count_subarrays_with_cost_less_than_or_equal_to_k/

object Solution {
  def countSubarrays(nums: Array[Int], k: Long): Long = {
    var ans = 0L
    val q1 = scala.collection.mutable.ArrayDeque.empty[Int]
    val q2 = scala.collection.mutable.ArrayDeque.empty[Int]
    var l = 0
    var r = 0
    while (r < nums.length) {
      val x = nums(r)
      while (q1.nonEmpty && nums(q1.last) <= x) q1.removeLast()
      while (q2.nonEmpty && nums(q2.last) >= x) q2.removeLast()
      q1.append(r)
      q2.append(r)
      while (l < r && (nums(q1.head).toLong - nums(q2.head)) * (r - l + 1) > k) {
        l += 1
        if (q1.head < l) q1.removeHead()
        if (q2.head < l) q2.removeHead()
      }
      ans += r - l + 1
      r += 1
    }
    ans
  }
}
