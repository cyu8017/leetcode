// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

object Solution {
  def missingRolls(rolls: Array[Int], mean: Int, n: Int): Array[Int] = {
    var sum = 0
    rolls.foreach { r => sum += r }
    val remain = mean * (rolls.length + n) - sum
    if (remain < n || remain > 6 * n) return Array.empty[Int]
    val ans = Array.ofDim[Int](n)
    val baseVal = remain / n
    val extra = remain % n
    var i = 0
    while (i < n) {
      ans(i) = baseVal + (if (i < extra) 1 else 0)
      i += 1
    }
    ans
  }
}
