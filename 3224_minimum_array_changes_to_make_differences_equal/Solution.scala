// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

object Solution {
  def minChanges(nums: Array[Int], k: Int): Int = {
    val d = new Array[Int](k + 2)
    val n = nums.length
    var i = 0
    while (i < n / 2) {
      var x = nums(i)
      var y = nums(n - 1 - i)
      if (x > y) { val t = x; x = y; y = t }
      d(0) += 1
      d(y - x) -= 1
      d(y - x + 1) += 1
      val mx = math.max(y, k - x)
      d(mx + 1) -= 1
      d(mx + 1) += 2
      i += 1
    }
    var ans = n
    var s = 0
    for (x <- d) {
      s += x
      ans = math.min(ans, s)
    }
    ans
  }
}
