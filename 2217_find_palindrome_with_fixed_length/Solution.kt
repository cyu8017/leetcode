// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

class Solution {

    fun kthPalindrome(queries: IntArray, intLength: Int): LongArray {

            var half = (intLength + 1) / 2
            var start = 1
            for (i in 1 until half) { start *= 10 }
            var total = start * 9
            var ans = LongArray(queries.size)
            for (i in 0 until queries.size) {
                var q = queries[i]
                if (q > total) { ans[i] = -1; continue; }
                var left = start + q - 1
                var pal = left
                var x = left
                if (intLength % 2 != 0) x /= 10
                while (x > 0) { pal = pal * 10 + x % 10; x /= 10; }
                ans[i] = pal
            }
            return ans

    }

}
