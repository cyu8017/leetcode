// LeetCode 0246 - Strobogrammatic Number
// https://leetcode.com/problems/strobogrammatic-number/

class Solution {
    fun isStrobogrammatic(num: String): Boolean {
        val mapping = mapOf('0' to '0', '1' to '1', '6' to '9', '8' to '8', '9' to '6')
        var left = 0
        var right = num.length - 1
        while (left <= right) {
            if (mapping[num[left]] != num[right]) {
                return false
            }
            left++
            right--
        }
        return true
    }
}
