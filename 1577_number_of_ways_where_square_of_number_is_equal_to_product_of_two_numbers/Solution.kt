// LeetCode 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
// https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

class Solution {
    fun numTriplets(nums1: IntArray, nums2: IntArray): Int =
        count(nums1, nums2) + count(nums2, nums1)

    private fun count(a: IntArray, b: IntArray): Int {
        val squares = HashMap<Long, Int>()
        for (x in a) {
            val sq = 1L * x * x
            squares[sq] = squares.getOrDefault(sq, 0) + 1
        }
        val products = HashMap<Long, Int>()
        for (i in b.indices) {
            for (j in i + 1 until b.size) {
                val prod = 1L * b[i] * b[j]
                products[prod] = products.getOrDefault(prod, 0) + 1
            }
        }
        var total = 0
        for ((key, value) in squares) {
            total += value * products.getOrDefault(key, 0)
        }
        return total
    }
}
