// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

class Solution {

    fun strongPasswordCheckerII(password: String): Boolean {

            if (password.length < 8) return false
            var special = "!@#$%^&*()-+"
            var hasLower = false; var hasUpper = false; var hasDigit = false; var hasSpecial = false
            for (i in 0 until password.length) {
                var c = password[i]
                if (i > 0 && c == password[i - 1]) return false
                if (c >= 'a' && c <= 'z') hasLower = true
                else if (c >= 'A' && c <= 'Z') hasUpper = true
                else if (c >= '0' && c <= '9') hasDigit = true
                else if (special.indexOf(c) >= 0) hasSpecial = true
            }
            return hasLower && hasUpper && hasDigit && hasSpecial

    }

}
