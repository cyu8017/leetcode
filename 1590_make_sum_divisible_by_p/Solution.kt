// LeetCode 1590 - Make Sum Divisible by P
// https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution {
    fun minSubarray(nums: IntArray, p: Int): Int {
        var total = 0
        for (x in nums) total = (total + x) % p
        if (total == 0) return 0
        val target = total
        val seen = HashMap<Int, Int>()
        seen[0] = -1
        var prefix = 0
        var answer = nums.size
        for (i in nums.indices) {
            prefix = (prefix + nums[i]) % p
            val need = (prefix - target + p) % p
            if (seen.containsKey(need)) {
                answer = minOf(answer, i - seen[need]!!)
            }
            seen[prefix] = i
        }
        return if (answer < nums.size) answer else -1
    }
}
