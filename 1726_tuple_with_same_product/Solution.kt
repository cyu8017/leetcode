// LeetCode 1726 - Tuple with Same Product
// https://leetcode.com/problems/tuple-with-same-product/

class Solution {
    fun tupleSameProduct(nums: IntArray): Int {
        val counts = HashMap<Int, Int>()
        for (i in nums.indices) {
            for (j in i + 1 until nums.size) {
                val product = nums[i] * nums[j]
                counts[product] = (counts[product] ?: 0) + 1
            }
        }
        var result = 0L
        for (count in counts.values) {
            result += count.toLong() * (count - 1) * 4
        }
        return result.toInt()
    }
}
