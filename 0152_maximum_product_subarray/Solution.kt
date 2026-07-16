class Solution {
    fun maxProduct(nums: IntArray): Int {
        var best = nums[0]; var max = nums[0]; var min = nums[0]
        for (i in 1 until nums.size) {
            val value = nums[i]; val previousMax = max; val previousMin = min
            max = maxOf(value, previousMax * value, previousMin * value)
            min = minOf(value, previousMax * value, previousMin * value)
            best = maxOf(best, max)
        }
        return best
    }
}