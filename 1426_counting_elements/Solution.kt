// LeetCode 1426 - Counting Elements
// https://leetcode.com/problems/counting-elements/

class Solution {
    fun countElements(arr: IntArray): Int {
        val values = arr.toSet()
        return arr.count { it + 1 in values }
    }
}
