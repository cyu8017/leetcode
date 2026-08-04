// LeetCode 1356 - Sort Integers by The Number of 1 Bits
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution {
    fun sortByBits(arr: IntArray): IntArray {
        return arr.sortedWith(compareBy({ Integer.bitCount(it) }, { it })).toIntArray()
    }
}
