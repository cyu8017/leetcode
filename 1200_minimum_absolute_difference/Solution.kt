// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

class Solution {
    fun minimumAbsDifference(arr: IntArray): List<List<Int>> {
        arr.sort()
        var best = Int.MAX_VALUE
        for (i in 0 until arr.size - 1) best = minOf(best, arr[i + 1] - arr[i])
        val ans = mutableListOf<List<Int>>()
        for (i in 0 until arr.size - 1) {
            if (arr[i + 1] - arr[i] == best) ans.add(listOf(arr[i], arr[i + 1]))
        }
        return ans
    }
}
