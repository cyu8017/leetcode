// LeetCode 1089 - Duplicate Zeros
// https://leetcode.com/problems/duplicate-zeros/

class Solution {
    fun duplicateZeros(arr: IntArray) {
        var zeros = arr.count { it == 0 }
        val n = arr.size
        for (i in n - 1 downTo 0) {
            if (i + zeros < n) arr[i + zeros] = arr[i]
            if (arr[i] == 0) {
                zeros--
                if (i + zeros < n) arr[i + zeros] = 0
            }
        }
    }
}
