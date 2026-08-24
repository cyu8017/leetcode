// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

object Solution {
  def minimumOperations(num: String): Int = {
    val n = num.length
    var ans = n
    if (num.contains('0')) ans = math.min(ans, n - 1)
    val targets = Array("00", "25", "50", "75")
    targets.foreach { t =>
      var j = n - 1
      while (j >= 0 && num.charAt(j) != t.charAt(1)) j -= 1
      if (j >= 0) {
        var i = j - 1
        while (i >= 0 && num.charAt(i) != t.charAt(0)) i -= 1
        if (i >= 0) ans = math.min(ans, n - i - 2)
      }
    }
    ans
  }
}
