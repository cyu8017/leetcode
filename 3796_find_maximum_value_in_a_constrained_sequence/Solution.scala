// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

object Solution {
  def maxValue(n: Int, restrictions: Array[Array[Int]], diff: Array[Int]): Int = {
    val INF = Integer.MAX_VALUE / 4
    val bound = Array.fill(n)(INF)
    bound(0) = 0
    restrictions.foreach(r => bound(r(0)) = r(1))
    var i = 1
    while (i < n) {
      bound(i) = math.min(bound(i), bound(i - 1) + diff(i - 1))
      i += 1
    }
    i = n - 2
    while (i >= 0) {
      bound(i) = math.min(bound(i), bound(i + 1) + diff(i))
      i -= 1
    }
    var ans = bound(0)
    i = 1
    while (i < n) {
      ans = math.max(ans, bound(i))
      i += 1
    }
    ans
  }
}
