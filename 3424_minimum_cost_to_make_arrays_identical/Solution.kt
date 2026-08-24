// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

class Solution {
    fun minCost(arr: IntArray, brr: IntArray, k: Long): Long {
        var noSwap = 0
        for (i in 0 until arr.size) { noSwap += kotlin.math.abs(arr[i] - brr[i]) }
        var a2 = arr
        var b2 = brr
        a2.sort()
        b2.sort()
        var withSwap = k
        for (i in 0 until a2.size) { withSwap += kotlin.math.abs(a2[i] - b2[i]) }
        return if (noSwap < withSwap) noSwap else withSwap
    }
}
