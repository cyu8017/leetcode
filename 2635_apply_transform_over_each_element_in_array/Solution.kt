// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

class Solution {
    fun map(arr: IntArray, fn: (Int, Int) -> Int): IntArray {
        val out = IntArray(arr.size)
        for (i in arr.indices) out[i] = fn(arr[i], i)
        return out
    }
}
