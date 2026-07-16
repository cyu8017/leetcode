// LeetCode 0325 - Maximum Size Subarray Sum Equals k

// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/



class Solution {

    fun maxSubArrayLen(nums: IntArray, k: Int): Int {

        val prefixIndex = hashMapOf(0 to -1)

        var prefix = 0

        var best = 0

        for ((index, num) in nums.withIndex()) {

            prefix += num

            prefixIndex[prefix - k]?.let { start ->

                best = maxOf(best, index - start)

            }

            prefixIndex.putIfAbsent(prefix, index)

        }

        return best

    }

}

