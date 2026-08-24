// LeetCode 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
// https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

class Solution {
    fun maxNonOverlapping(nums: IntArray, target: Int): Int {
        val seen = HashSet<Int>()
        seen.add(0)
        var prefix = 0
        var answer = 0
        for (value in nums) {
            prefix += value
            if (prefix - target in seen) {
                answer++
                prefix = 0
                seen.clear()
                seen.add(0)
            } else {
                seen.add(prefix)
            }
        }
        return answer
    }
}
