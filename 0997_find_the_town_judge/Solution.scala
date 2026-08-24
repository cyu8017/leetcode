// LeetCode 0997 - Find the Town Judge
// https://leetcode.com/problems/find-the-town-judge/

object Solution {
  def findJudge(n: Int, trust: Array[Array[Int]]): Int = {
    val score = Array.ofDim[Int](n + 1)
    trust.foreach { t =>
      score(t(0)) -= 1
      score(t(1)) += 1
    }
    var i = 1
    while (i <= n) {
      if (score(i) == n - 1) return i
      i += 1
    }
    -1
  }
}
