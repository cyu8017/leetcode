// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

object Solution {
  def maxPoints(technique1: Array[Int], technique2: Array[Int], k: Int): Long = {
    val n = technique1.length
    val idx = Array.tabulate[Integer](n)(i => i)
    java.util.Arrays.sort(idx, (i: Integer, j: Integer) =>
      Integer.compare(technique1(j) - technique2(j), technique1(i) - technique2(i)))
    var ans = 0L
    technique2.foreach(x => ans += x)
    var i = 0
    while (i < k) {
      val index = idx(i)
      ans -= technique2(index)
      ans += technique1(index)
      i += 1
    }
    i = k
    while (i < n) {
      val index = idx(i)
      if (technique1(index) >= technique2(index)) {
        ans -= technique2(index)
        ans += technique1(index)
      }
      i += 1
    }
    ans
  }
}
