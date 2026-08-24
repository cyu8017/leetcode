// LeetCode 0667 - Beautiful Arrangement II
// https://leetcode.com/problems/beautiful-arrangement-ii/


class Solution {
    fun constructArray(n: Int, k: Int): IntArray {
        val result = IntArray(n)
        var left = 1
        var right = n
        var idx = 0
        var remain = k
        while (idx < n) {
            if (remain > 1) {
                if (remain % 2 == 1) result[idx++] = left++ else result[idx++] = right--
                remain--
            } else {
                result[idx++] = left++
            }
        }
        return result
    }
}
