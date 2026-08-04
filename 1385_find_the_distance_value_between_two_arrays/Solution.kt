// LeetCode 1385 - Find the Distance Value Between Two Arrays
// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution {
    fun findTheDistanceValue(arr1: IntArray, arr2: IntArray, d: Int): Int {
        val b = arr2.sorted()
        var ans = 0
        for (x in arr1) {
            val i = b.binarySearch(x).let { if (it < 0) -it - 1 else it }
            val close = (i < b.size && kotlin.math.abs(b[i] - x) <= d) ||
                (i > 0 && kotlin.math.abs(b[i - 1] - x) <= d)
            if (!close) ans++
        }
        return ans
    }
}
