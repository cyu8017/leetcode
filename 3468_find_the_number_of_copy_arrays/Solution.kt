// LeetCode 3468 - Find the Number of Copy Arrays
// https://leetcode.com/problems/find-the-number-of-copy-arrays/

class Solution {
    fun countArrays(original: IntArray, bounds: Array<IntArray>): Int {
        var n = original.size
        var lo = bounds[0][0]
        var hi = bounds[0][1]
        for (i in 1 until n) {
            var diff = original[i] - original[i - 1]
            var lo2 = bounds[i][0]
            var hi2 = bounds[i][1]
            var nlo = lo + diff
            var nhi = hi + diff
            if (nlo < lo2) nlo = lo2
            if (nhi > hi2) nhi = hi2
            if (nlo > nhi) return 0
            lo = nlo
            hi = nhi
        }
        return hi - lo + 1
    }
}
