// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution {
    fun getSneakyNumbers(nums: IntArray): IntArray {
        val seen = HashSet<Int>()
        val ans = ArrayList<Int>()
        for (x in nums) {
            if (!seen.add(x)) ans.add(x)
        }
        return ans.toIntArray()
    }
}
