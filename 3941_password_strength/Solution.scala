// LeetCode 3941 - Password Strength
// https://leetcode.com/problems/password-strength/

object Solution {
  def passwordStrength(password: String): Int = {
    val st = password.toSet
    var ans = 0
    for (ch <- st) {
      if (ch.isLower) ans += 1
      else if (ch.isUpper) ans += 2
      else if (ch.isDigit) ans += 3
      else ans += 5
    }
    ans
  }
}
