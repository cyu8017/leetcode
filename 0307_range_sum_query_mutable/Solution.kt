// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

class NumArray(nums: IntArray) {
    private val nums = nums.copyOf()
    private val tree = IntArray(nums.size + 1)

    init {
        for (index in nums.indices) {
            add(index + 1, nums[index])
        }
    }

    fun update(index: Int, `val`: Int) {
        val delta = `val` - nums[index]
        nums[index] = `val`
        add(index + 1, delta)
    }

    fun sumRange(left: Int, right: Int): Int {
        return prefix(right + 1) - prefix(left)
    }

    private fun add(index: Int, delta: Int) {
        var current = index
        while (current <= nums.size) {
            tree[current] += delta
            current += current and -current
        }
    }

    private fun prefix(index: Int): Int {
        var total = 0
        var current = index
        while (current > 0) {
            total += tree[current]
            current -= current and -current
        }
        return total
    }
}
