// LeetCode 1566 - Detect Pattern of Length M Repeated K or More Times
// https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

class Solution {
    fun containsPattern(arr: IntArray, m: Int, k: Int): Boolean {
        var run = 0
        for (i in m until arr.size) {
            run = if (arr[i] == arr[i - m]) run + 1 else 0
            if (run >= m * (k - 1)) return true
        }
        return false
    }
}
