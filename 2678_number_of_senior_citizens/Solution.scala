// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

object Solution {
  def countSeniors(details: Array[String]): Int = {
    var ans = 0
    var i = 0
    while (i < details.length) {
      val d = details(i)
      val age = (d.charAt(11) - '0') * 10 + (d.charAt(12) - '0')
      if (age > 60) ans += 1
      i += 1
    }
    ans
  }
}
