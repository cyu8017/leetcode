// LeetCode 3086 - Minimum Moves to Pick K Ones
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

object Solution {
  def minimumMoves(nums: Array[Int], k: Int, maxChanges: Int): Long = {
    val n = nums.length
    val cnt = new Array[Int](n + 1)
    val s = new Array[Int](n + 1)
    var i = 1
    while (i <= n) {
      cnt(i) = cnt(i - 1) + nums(i - 1)
      s(i) = s(i - 1) + i * nums(i - 1)
      i += 1
    }
    var ans = Long.MaxValue
    i = 1
    while (i <= n) {
      var t = 0L
      var need = k - nums(i - 1)
      Array(i - 1, i + 1).foreach { j =>
        if (need > 0 && 1 <= j && j <= n && nums(j - 1) == 1) {
          need -= 1
          t += 1
        }
      }
      val c = math.min(need, maxChanges)
      need -= c
      t += c * 2L
      if (need <= 0) {
        ans = math.min(ans, t)
      } else {
        var l = 2
        var r = math.max(i - 1, n - i)
        while (l <= r) {
          val mid = (l + r) >> 1
          val l1 = math.max(1, i - mid)
          val r1 = math.max(0, i - 2)
          val l2 = math.min(n + 1, i + 2)
          val r2 = math.min(n, i + mid)
          val c1 = cnt(r1) - cnt(l1 - 1)
          val c2 = cnt(r2) - cnt(l2 - 1)
          if (c1 + c2 >= need) {
            val t1 = c1.toLong * i - (s(r1) - s(l1 - 1))
            val t2 = s(r2) - s(l2 - 1) - c2.toLong * i
            ans = math.min(ans, t + t1 + t2)
            r = mid - 1
          } else {
            l = mid + 1
          }
        }
      }
      i += 1
    }
    ans
  }
}
