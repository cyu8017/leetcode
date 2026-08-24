// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

class Solution {
    fun validateCoupons(code: Array<String>, businessLine: Array<String>, isActive: BooleanArray): List<String> {
        val bs = hashSetOf("electronics", "grocery", "pharmacy", "restaurant")
        val idx = ArrayList<Int>()
        for (i in code.indices) {
            if (isActive[i] && businessLine[i] in bs && check(code[i])) idx.add(i)
        }
        idx.sortWith(compareBy({ businessLine[it] }, { code[it] }))
        val ans = ArrayList<String>()
        for (i in idx) ans.add(code[i])
        return ans
    }

    fun check(s: String): Boolean {
        if (s.isEmpty()) return false
        for (c in s) if (!c.isLetterOrDigit() && c != '_') return false
        return true
    }
}
