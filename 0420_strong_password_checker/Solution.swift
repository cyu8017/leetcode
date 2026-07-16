// LeetCode 0420 - Strong Password Checker
// https://leetcode.com/problems/strong-password-checker/

class Solution {
    func strongPasswordChecker(_ password: String) -> Int {
        let length = password.count
        var missing = 3
        if password.range(of: "[a-z]", options: .regularExpression) != nil {
            missing -= 1
        }
        if password.range(of: "[A-Z]", options: .regularExpression) != nil {
            missing -= 1
        }
        if password.range(of: "\\d", options: .regularExpression) != nil {
            missing -= 1
        }

        var replace = 0
        var oneRepeat = 0
        var twoRepeat = 0
        let chars = Array(password)
        var index = 0
        while index < length {
            var run = 1
            while index + run < length && chars[index + run] == chars[index] {
                run += 1
            }
            if run >= 3 {
                replace += run / 3
                if run % 3 == 0 {
                    oneRepeat += 1
                } else if run % 3 == 1 {
                    twoRepeat += 1
                }
            }
            index += run
        }

        if length < 6 {
            return max(6 - length, missing)
        }
        if length <= 20 {
            return max(missing, replace)
        }

        var delete = length - 20
        replace -= min(delete, oneRepeat)
        delete -= min(delete, oneRepeat)
        replace -= min(delete / 2, twoRepeat)
        delete -= min(delete / 2, twoRepeat) * 2
        replace -= delete / 3
        return length - 20 + max(missing, replace)
    }
}
