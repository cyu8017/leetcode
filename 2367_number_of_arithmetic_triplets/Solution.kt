// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution {
    fun arithmeticTriplets(nums: IntArray, diff: Int): Int {
        val seen = HashSet<Int>()
        for (x in nums) seen.add(x)
        var ans = 0
        for (x in nums) {
            if (x + diff in seen && x + 2 * diff in seen) ans++
        }
        return ans
    }
}
