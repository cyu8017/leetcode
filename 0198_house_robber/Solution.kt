class Solution {
    fun rob(nums: IntArray): Int {
        var previousTwo = 0
        var previousOne = 0
        for (num in nums) {
            val current = maxOf(previousOne, previousTwo + num)
            previousTwo = previousOne
            previousOne = current
        }
        return previousOne
    }
}
