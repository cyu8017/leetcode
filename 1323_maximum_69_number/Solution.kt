// LeetCode 1323 - Maximum 69 Number
// https://leetcode.com/problems/maximum-69-number/

class Solution {
    fun maximum69Number(num: Int): Int {
        return num.toString().replaceFirst('6', '9').toInt()
    }
}
