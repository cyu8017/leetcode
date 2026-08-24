// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum_operations_to_make_binary_palindrome/

class Solution {
    companion object {
        private val PALS = ArrayList<Int>()

        init {
            val N = 1 shl 14
            for (i in 0 until N) {
                val sb = StringBuilder()
                var x = i
                if (x == 0) {
                    sb.append('0')
                } else {
                    while (x > 0) {
                        sb.append(('0'.code + (x and 1)).toChar())
                        x = x shr 1
                    }
                    sb.reverse()
                }
                if (isPalindrome(sb)) PALS.add(i)
            }
        }

        private fun isPalindrome(s: StringBuilder): Boolean {
            val m = s.length
            for (i in 0 until m / 2) {
                if (s[i] != s[m - 1 - i]) return false
            }
            return true
        }
    }

    fun minOperations(nums: IntArray): IntArray {
        val ans = IntArray(nums.size)
        for (k in nums.indices) {
            val x = nums[k]
            val it = lowerBound(x)
            var t = Int.MAX_VALUE
            if (it < PALS.size) t = PALS[it] - x
            if (it > 0) t = minOf(t, x - PALS[it - 1])
            ans[k] = t
        }
        return ans
    }

    private fun lowerBound(x: Int): Int {
        var lo = 0
        var hi = PALS.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (PALS[mid] < x) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
