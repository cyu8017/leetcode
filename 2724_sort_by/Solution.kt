// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

class Solution {
    fun sortBy(arr: IntArray, fn: (Int) -> Double): IntArray {
        return arr.sortedBy { fn(it) }.toIntArray()
    }
}
