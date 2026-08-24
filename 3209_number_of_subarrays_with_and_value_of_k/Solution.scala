// LeetCode 3209 - Number of Subarrays With AND Value of K
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

object Solution {
  def countSubarrays(nums: Array[Int], k: Int): Long = {
    var pre = scala.collection.mutable.HashMap.empty[Int, Int]
    var ans = 0L
    for (x <- nums) {
      val cur = scala.collection.mutable.HashMap.empty[Int, Int]
      for ((key, v) <- pre) {
        val nk = x & key
        cur(nk) = cur.getOrElse(nk, 0) + v
      }
      cur(x) = cur.getOrElse(x, 0) + 1
      ans += cur.getOrElse(k, 0)
      pre = cur
    }
    ans
  }
}
