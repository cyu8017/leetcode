// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution {
    fun countDistinctIntegers(nums: IntArray): Int {
        val seen = HashSet<Int>()
        for (x in nums) {
            seen.add(x)
            seen.add(rev(x))
        }
        return seen.size
    }

    private fun rev(x0: Int): Int {
        var x = x0
        var r = 0
        while (x > 0) {
            r = r * 10 + x % 10
            x /= 10
        }
        return r
    }
}
