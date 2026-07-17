// LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
// https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

object Solution {
  def minCharacters(a: String, b: String): Int = {
    val ca = new Array[Int](26)
    val cb = new Array[Int](26)
    a.foreach(ch => ca(ch - 'a') += 1)
    b.foreach(ch => cb(ch - 'a') += 1)
    val n = a.length
    val m = b.length
    val maxCount = math.max(ca.max, cb.max)
    var ans = n + m - maxCount
    var preA = 0
    var preB = 0
    for (code <- 0 until 25) {
      preA += ca(code)
      preB += cb(code)
      ans = math.min(ans, math.min(n - preA + preB, m - preB + preA))
    }
    ans
  }
}
