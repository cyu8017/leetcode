// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

class Solution {
    fun maskPII(s: String): String {
        var s = s
        var at = s.indexOf('@')
        if (at >= 0) {
            s = s.toLowerCase()
            at = s.indexOf('@')
            var name = s.substring(0, at)
            var domain = s.substring(at + 1)
            return name[0] + "*****" + name[name.length - 1] + "@" + domain
        }
        var digits = StringBuilder()
        for (ch in s.toCharArray()) { if (Character.isDigit(ch)) digits.append(ch) }
        var local = digits.substring(digits.length - 4)
        var country = digits.length - 10
        if (country == 0) return "***-***-" + local
        return "+" + "*".repeat(country) + "-***-***-" + local
    }
}
