// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

class Solution {
    fun minSwaps(nums: IntArray): Int {
        val pos = Array(2) { ArrayList<Int>() }
        for (i in nums.indices) pos[nums[i] and 1].add(i)
        if (kotlin.math.abs(pos[0].size - pos[1].size) > 1) return -1
        if (pos[0].size > pos[1].size) return calc(pos, nums.size, 0)
        if (pos[0].size < pos[1].size) return calc(pos, nums.size, 1)
        return minOf(calc(pos, nums.size, 0), calc(pos, nums.size, 1))
    }

    fun calc(pos: Array<ArrayList<Int>>, n: Int, k: Int): Int {
        var res = 0
        var i = 0
        while (i < n) {
            res += kotlin.math.abs(pos[k][i / 2] - i)
            i += 2
        }
        return res
    }
}
