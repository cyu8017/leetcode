// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

class Solution {

    fun totalSteps(nums: IntArray): Int {

            var stack = ArrayList<Int>()
            var ans = 0
            for (i in nums.size - 1 downTo 0) {
                var steps = 0
                while (!stack.isEmpty() && nums[i] > stack[stack.size - 1][0]) {
                    steps = maxOf(steps, stack[stack.size - 1][1])
                    stack.removeAt(stack.size - 1)
                    steps++
                }
                ans = maxOf(ans, steps)
                stack.add(intArrayOf(nums[i], steps))
            }
            return ans

    }

}
