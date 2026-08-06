// LeetCode 1471 - The k Strongest Values in an Array
// https://leetcode.com/problems/the-k-strongest-values-in-an-array/

class Solution {
    fun getStrongest(arr: IntArray, k: Int): IntArray {
        arr.sort()
        val median = arr[(arr.size - 1) / 2]
        return arr.sortedWith(compareByDescending<Int> { kotlin.math.abs(it - median) }
            .thenByDescending { it }).take(k).toIntArray()
    }
}
