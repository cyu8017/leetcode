// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

object Solution {
  def minIncrements(n: Int, cost: Array[Int]): Int = {
    var ans = 0
    var i = n / 2 - 1
    while (i >= 0) {
      val l = 2 * i + 1
      val r = 2 * i + 2
      ans += math.abs(cost(l) - cost(r))
      cost(i) += math.max(cost(l), cost(r))
      i -= 1
    }
    ans
  }
}
