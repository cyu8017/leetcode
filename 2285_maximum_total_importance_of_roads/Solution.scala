// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

object Solution {
  def maximumImportance(n: Int, roads: Array[Array[Int]]): Long = {
    val deg = new Array[Int](n)
    for (r <- roads) {
      deg(r(0)) += 1
      deg(r(1)) += 1
    }
    java.util.Arrays.sort(deg)
    var ans = 0L
    var i = 0
    while (i < n) {
      ans += deg(i).toLong * (i + 1)
      i += 1
    }
    ans
  }
}
