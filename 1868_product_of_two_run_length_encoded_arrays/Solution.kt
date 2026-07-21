// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

class Solution {
    fun findRLEArray(encoded1: Array<IntArray>, encoded2: Array<IntArray>): List<List<Int>> {
        val result = mutableListOf<MutableList<Int>>()
        var i = 0
        var j = 0
        var rem1 = encoded1[0][1]
        var rem2 = encoded2[0][1]
        while (i < encoded1.size) {
            val take = minOf(rem1, rem2)
            val value = encoded1[i][0] * encoded2[j][0]
            if (result.isNotEmpty() && result.last()[0] == value) {
                result.last()[1] += take
            } else {
                result.add(mutableListOf(value, take))
            }
            rem1 -= take
            rem2 -= take
            if (rem1 == 0) {
                i++
                if (i < encoded1.size) rem1 = encoded1[i][1]
            }
            if (rem2 == 0) {
                j++
                if (j < encoded2.size) rem2 = encoded2[j][1]
            }
        }
        return result
    }
}
