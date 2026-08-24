// LeetCode 0303 - Range Sum Query - Immutable
// https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(nums: IntArray) {
    private val prefix = IntArray(nums.size + 1)

    init {
        for (index in nums.indices) {
            prefix[index + 1] = prefix[index] + nums[index]
        }
    }

    fun sumRange(left: Int, right: Int): Int {
        return prefix[right + 1] - prefix[left]
    }
}
