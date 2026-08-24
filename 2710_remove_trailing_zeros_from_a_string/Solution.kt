// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution {
    fun removeTrailingZeros(num: String): String {
        var end = num.length
        while (end > 0 && num[end - 1] == '0') end--
        return num.substring(0, end)
    }
}
