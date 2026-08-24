// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

object Solution {
  def strongPasswordCheckerII(password: String): Boolean = {
    if (password.length < 8) return false
    val special = "!@#$%^&*()-+"
    var hasLower = false
    var hasUpper = false
    var hasDigit = false
    var hasSpecial = false
    var i = 0
    while (i < password.length) {
      val c = password.charAt(i)
      if (i > 0 && c == password.charAt(i - 1)) return false
      if (c >= 'a' && c <= 'z') hasLower = true
      else if (c >= 'A' && c <= 'Z') hasUpper = true
      else if (c >= '0' && c <= '9') hasDigit = true
      else if (special.indexOf(c) >= 0) hasSpecial = true
      i += 1
    }
    hasLower && hasUpper && hasDigit && hasSpecial
  }
}
