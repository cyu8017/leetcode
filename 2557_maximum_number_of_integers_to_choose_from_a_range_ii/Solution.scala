// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

object Solution {
  def maxCount(banned: Array[Int], n: Int, maxSum: Long): Int = {
    java.util.Arrays.sort(banned)
    val uniq = scala.collection.mutable.ArrayBuffer.empty[Int]
    banned.foreach { x =>
      if (x >= 1 && x <= n && (uniq.isEmpty || uniq.last != x)) uniq += x
    }
    var ans = 0
    var remain = maxSum
    def check(l: Long, r: Long): Unit = {
      if (l > r || remain <= 0) return
      var lo = l
      var hi = r
      var best = l - 1
      while (lo <= hi) {
        val mid = (lo + hi) / 2
        val cnt = mid - l + 1
        val sum = (l + mid) * cnt / 2
        if (sum <= remain) {
          best = mid
          lo = mid + 1
        } else hi = mid - 1
      }
      if (best >= l) {
        val cnt = (best - l + 1).toInt
        ans += cnt
        remain -= (l + best) * cnt / 2
      }
    }
    var prev = 0
    uniq.foreach { b =>
      check(prev + 1L, b - 1L)
      prev = b
    }
    check(prev + 1L, n.toLong)
    ans
  }
}
