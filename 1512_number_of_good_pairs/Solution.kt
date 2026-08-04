// LeetCode 1512 - Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/

class Solution {
    fun numIdenticalPairs(nums: IntArray): Int {
        val counts = HashMap<Int, Int>()
        for (num in nums) {
            counts[num] = counts.getOrDefault(num, 0) + 1
        }
        var ans = 0
        for (count in counts.values) {
            ans += count * (count - 1) / 2
        }
        return ans
    }
}
