// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

object Solution {
  def maxDepthAfterSplit(seq: String): Array[Int] = {
    var depth = 0
    val ans = Array.ofDim[Int](seq.length)
    for (i <- seq.indices) {
      if (seq(i) == '(') {
        ans(i) = depth % 2
        depth += 1
      } else {
        depth -= 1
        ans(i) = depth % 2
      }
    }
    ans
  }
}
