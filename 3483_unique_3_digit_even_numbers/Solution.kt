// LeetCode 3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/

class Solution {
    fun totalNumbers(digits: IntArray): Int {
        var seen = HashSet<Int>()
        var n = digits.size
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (j == i) continue
                for (k in 0 until n) {
                    if (k == i || k == j) continue
                    if (digits[i] == 0) continue
                    if (digits[k] % 2 != 0) continue
                    seen.add(digits[i] * 100 + digits[j] * 10 + digits[k])
                }
            }
        }
        return seen.size
    }
}
