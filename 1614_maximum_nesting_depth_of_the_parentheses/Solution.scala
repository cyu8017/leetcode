// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

object Solution {
  def maxDepth(s: String): Int = {
    var depth = 0
    var ans = 0
    for (ch <- s) {
      if (ch == '(') {
        depth += 1
        ans = math.max(ans, depth)
      } else if (ch == ')') depth -= 1
    }
    ans
  }
}
