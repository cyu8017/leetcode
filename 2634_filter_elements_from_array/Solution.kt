// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

class Solution {
    fun filter(arr: IntArray, fn: (Int, Int) -> Boolean): IntArray {
        val out = ArrayList<Int>()
        for (i in arr.indices) if (fn(arr[i], i)) out.add(arr[i])
        return out.toIntArray()
    }
}
