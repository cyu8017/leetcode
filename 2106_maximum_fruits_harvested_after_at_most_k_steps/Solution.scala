// LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

object Solution {
  private def minSteps(left: Int, right: Int, start: Int): Int = {
    if (right <= start) start - left
    else if (left >= start) right - start
    else math.min((start - left) + (right - left), (right - start) + (right - left))
  }

  def maxTotalFruits(fruits: Array[Array[Int]], startPos: Int, k: Int): Int = {
    val n = fruits.length
    val pref = Array.fill(n + 1)(0)
    val pos = Array.fill(n)(0)
    var i = 0
    while (i < n) {
      pos(i) = fruits(i)(0)
      pref(i + 1) = pref(i) + fruits(i)(1)
      i += 1
    }
    var ans = 0
    var j = 0
    i = 0
    while (i < n) {
      while (j < n && minSteps(pos(i), pos(j), startPos) > k) j += 1
      if (j <= i) ans = math.max(ans, pref(i + 1) - pref(j))
      i += 1
    }
    j = 0
    i = 0
    while (i < n) {
      while (j <= i && minSteps(pos(j), pos(i), startPos) > k) j += 1
      ans = math.max(ans, pref(i + 1) - pref(j))
      i += 1
    }
    ans
  }
}
