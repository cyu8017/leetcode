// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

class Solution {
    fun distinctDifferenceArray(nums: IntArray): IntArray {
        val n = nums.size
        val suf = IntArray(n + 1)
        val seen = HashSet<Int>()
        for (i in n - 1 downTo 0) {
            seen.add(nums[i])
            suf[i] = seen.size
        }
        seen.clear()
        val ans = IntArray(n)
        for (i in 0 until n) {
            seen.add(nums[i])
            ans[i] = seen.size - suf[i + 1]
        }
        return ans
    }
}
