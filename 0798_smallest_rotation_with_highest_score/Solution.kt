// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

class Solution {
    fun bestRotation(nums: IntArray): Int {
        var n = nums.size
        var change = IntArray(n)
        java.util.change.fill(1)
        for (i in 0 until n) { change[(i - nums[i] + 1 + n) % n] -= 1 }
        for (i in 1 until n) { change[i] += change[i - 1] }
        var best = 0
        for (i in 1 until n) { if (change[i] > change[best]) best = i }
        return best
    }
}
