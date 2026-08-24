// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution {

    fun divideArray(nums: IntArray): Boolean {

            var freq = HashMap<Int, Int>()
            for (x in nums) {
                var c = freq.getOrDefault(x, 0)
                freq.put(x, c + 1)
            }
            for (c in freq.values) if (c % 2 != 0) return false
            return true

    }

}
