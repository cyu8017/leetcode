// LeetCode 3941 - Password Strength
// https://leetcode.com/problems/password-strength/

class Solution {
    fun passwordStrength(password: String): Int {
        val st = HashSet<Char>()
        for (ch in password) st.add(ch)
        var ans = 0
        for (ch in st) {
            ans += when {
                ch.isLowerCase() -> 1
                ch.isUpperCase() -> 2
                ch.isDigit() -> 3
                else -> 5
            }
        }
        return ans
    }
}
