// LeetCode 2855 - Minimum Right Shifts to Sort the Array
// https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

class Solution {
    fun minimumRightShifts(nums: List<Int>): Int {
        val n = nums.size
        var drops = 0
        var idx = -1
        for (i in 0 until n) {
            if (nums[i] > nums[(i + 1) % n]) {
                drops++
                idx = i
            }
        }
        if (drops == 0) return 0
        if (drops > 1) return -1
        return n - 1 - idx
    }
}
