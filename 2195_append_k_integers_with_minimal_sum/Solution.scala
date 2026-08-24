// LeetCode 2195 - Append K Integers With Minimal Sum
// https://leetcode.com/problems/append-k-integers-with-minimal-sum/

object Solution {
  def minimalKSum(nums: Array[Int], k0: Int): Long = {
    val sorted = nums.sorted
    var ans = 0L
    var prev = 0
    var k = k0
    sorted.foreach { x =>
      if (x > prev) {
        val start = prev + 1
        var end = x - 1
        if (start <= end) {
          var cnt = end - start + 1
          if (cnt > k) { end = start + k - 1; cnt = k }
          ans += (start.toLong + end) * cnt / 2
          k -= cnt
          if (k == 0) return ans
        }
        prev = x
      }
    }
    val s = prev.toLong + 1
    val e = s + k - 1
    ans + (s + e) * k / 2
  }
}
