// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

class Solution {

    fun appealSum(s: String): Long {

            var last = IntArray(26)
            last.fill(-1)
            var ans = 0; var cur = 0
            for (i in 0 until s.length) {
                var c = s[i] - 'a'
                cur += i - last[c]
                last[c] = i
                ans += cur
            }
            return ans

    }

}
