// LeetCode 1497 - Check If Array Pairs Are Divisible by k
// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution {
    fun canArrange(arr: IntArray, k: Int): Boolean {
        val count = IntArray(k)
        for (x in arr) {
            val r = ((x % k) + k) % k
            count[r]++
        }
        if (count[0] % 2 != 0) return false
        for (r in 1 until k) {
            if (count[r] != count[k - r]) return false
        }
        return true
    }
}
