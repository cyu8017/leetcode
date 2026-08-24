// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

object Solution {
  def isBalanced(num: String): Boolean = {
    var even = 0
    var odd = 0
    var i = 0
    while (i < num.length) {
      if (i % 2 == 0) even += num.charAt(i) - '0'
      else odd += num.charAt(i) - '0'
      i += 1
    }
    even == odd
  }
}
