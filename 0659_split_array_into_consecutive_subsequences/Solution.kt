// LeetCode 0659 - Split Array into Consecutive Subsequences
// https://leetcode.com/problems/split-array-into-consecutive-subsequences/


class Solution {
    fun isPossible(nums: IntArray): Boolean {
        val freq = HashMap<Int, Int>()
        val tails = HashMap<Int, Int>()
        for (num in nums) freq[num] = freq.getOrDefault(num, 0) + 1
        for (num in nums) {
            if (freq.getOrDefault(num, 0) == 0) continue
            freq[num] = freq[num]!! - 1
            when {
                tails.getOrDefault(num - 1, 0) > 0 -> {
                    tails[num - 1] = tails[num - 1]!! - 1
                    tails[num] = tails.getOrDefault(num, 0) + 1
                }
                freq.getOrDefault(num + 1, 0) > 0 && freq.getOrDefault(num + 2, 0) > 0 -> {
                    freq[num + 1] = freq[num + 1]!! - 1
                    freq[num + 2] = freq[num + 2]!! - 1
                    tails[num + 2] = tails.getOrDefault(num + 2, 0) + 1
                }
                else -> return false
            }
        }
        return true
    }
}
