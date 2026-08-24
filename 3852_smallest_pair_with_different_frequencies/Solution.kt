// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

class Solution {
    fun minDistinctFreqPair(nums: IntArray): IntArray {
        var cnt = HashMap<Int, Int>()
        for (v in nums) { cnt[v] = cnt.getOrDefault(v, 0 + 1) }
        var x = nums[0]
        for (v in nums) { x = minOf(x, v) }
        var minY = Int.MAX_VALUE
        for (y in cnt.keys) {
            if (y < minY && !cnt[(x] == cnt[y])) minY = y
        }
        if (minY == Int.MAX_VALUE) return intArrayOf( -1, -1 )
        return intArrayOf( x, minY )
    }
}
