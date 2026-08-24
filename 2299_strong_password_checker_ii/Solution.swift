// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

class Solution {
    func strongPasswordCheckerII(_ password: String) -> Bool {
        if password.count < 8 { return false }
        let special = Set("!@#$%^&*()-+")
        let arr = Array(password)
        var hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false
        for i in 0..<arr.count {
            let c = arr[i]
            if i > 0 && c == arr[i - 1] { return false }
            if c.isLowercase { hasLower = true }
            else if c.isUppercase { hasUpper = true }
            else if c.isNumber { hasDigit = true }
            else if special.contains(c) { hasSpecial = true }
        }
        return hasLower && hasUpper && hasDigit && hasSpecial
    }
}
