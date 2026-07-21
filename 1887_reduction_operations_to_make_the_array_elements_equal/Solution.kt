// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution {
    fun reductionOperations(nums: IntArray): Int {
        nums.sort()
        var answer = 0
        var rank = 0
        for (i in 1 until nums.size) {
            if (nums[i] != nums[i - 1]) rank++
            answer += rank
        }
        return answer
    }
}
