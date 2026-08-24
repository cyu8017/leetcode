// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/
// JS-only problem; Java stand-in.

fun interface ArrayCallback {
    fun call(value: Int, index: Int, array: IntArray)
}

class Solution {
    fun forEach(arr: IntArray, callback: ArrayCallback) {
        for (i in arr.indices) callback.call(arr[i], i, arr)
    }
}
