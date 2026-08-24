// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

class Solution {
    fun isBalanced(num: String): Boolean {
        var even = 0
        var odd = 0
        for (i in num.indices) {
            val d = num[i] - '0'
            if (i % 2 == 0) even += d else odd += d
        }
        return even == odd
    }
}
