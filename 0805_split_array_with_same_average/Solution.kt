// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

class Solution {
    private var nums: IntArray? = null
    private var n: Int = 0
    private var memo: MutableSet<Long>? = null

    fun splitArraySameAverage(nums: IntArray): Boolean {
        var nums = nums
        this.nums = nums
        n = nums.size
        var total = 0
        for (x in nums) { total += x }
        nums.sort()
        memo = HashSet()
        for (size in 1 until n) {
            if ((total * size) % n == 0 && find(total * size / n, size, 0)) return true
        }
        return false
    }

    private fun find(target: Int, count: Int, index: Int): Boolean {
        if (count == 0) return target == 0
        if (index == n || count + index > n || target < 0) return false
        var key = (target  shl  20) | (count  shl  10) | index
        if (memo.contains(key)) return false
        if (find(target - nums[index], count - 1, index + 1) || find(target, count, index + 1)) {
            return true
        }
        memo.add(key)
        return false
    }
}
