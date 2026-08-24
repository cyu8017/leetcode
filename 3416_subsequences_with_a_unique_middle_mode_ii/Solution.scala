// LeetCode 3416 - Subsequences with a Unique Middle Mode II
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-ii/

object Solution {
  private def uniqueMode(a: Array[Int]): Boolean = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    a.foreach { x => freq(x) = freq.getOrElse(x, 0) + 1 }
    var best = 0
    var cnt = 0
    freq.values.foreach { f =>
      if (f > best) { best = f; cnt = 1 }
      else if (f == best) cnt += 1
    }
    cnt == 1
  }

  def subsequencesWithMiddleMode(nums: Array[Int]): Int = {
    val mod = 1000000007
    val n = nums.length
    var ans = 0
    var mid = 2
    while (mid < n - 2) {
      var a = 0
      while (a < mid) {
        var b = a + 1
        while (b < mid) {
          var c = mid + 1
          while (c < n) {
            var d = c + 1
            while (d < n) {
              val seq = Array(nums(a), nums(b), nums(mid), nums(c), nums(d))
              if (uniqueMode(seq)) ans = (ans + 1) % mod
              d += 1
            }
            c += 1
          }
          b += 1
        }
        a += 1
      }
      mid += 1
    }
    ans
  }
}
