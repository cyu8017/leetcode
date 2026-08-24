// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum_absolute_distance_between_mirror_pairs/

class Solution {
    fun minMirrorPairDistance(nums: IntArray): Int {
        var n = nums.size
        var pos = HashMap<Int, Int>()
        var ans = n + 1
        for (i in 0 until n) {
            if (pos.containsKey(nums[i])) ans = minOf(ans, i - pos[nums[i]])
            pos[reverse(nums[i])] = i
        }
        return if (ans > n) -1 else ans
    }

    private fun reverse(x: Int): Int {
        var y = 0
        while (x > 0) {
y = y * 10 + x % 10
        return y
    }
}
x /= 10
}
