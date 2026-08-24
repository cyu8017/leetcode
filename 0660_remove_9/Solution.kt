// LeetCode 0660 - Remove 9
// https://leetcode.com/problems/remove-9/


class Solution {
    fun newInteger(n: Int): Int {
        var num = n
        var result = 0
        var base = 1
        while (num > 0) {
            result += (num % 9) * base
            num /= 9
            base *= 10
        }
        return result
    }
}
