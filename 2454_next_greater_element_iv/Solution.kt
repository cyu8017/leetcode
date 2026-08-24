// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

class Solution {
    fun secondGreaterElement(nums: IntArray): IntArray {
        val n = nums.size
        val ans = IntArray(n) { -1 }
        val stack1 = ArrayList<Int>()
        val stack2 = ArrayList<Int>()
        for (i in 0 until n) {
            val x = nums[i]
            while (stack2.isNotEmpty() && nums[stack2[stack2.size - 1]] < x) {
                ans[stack2.removeAt(stack2.size - 1)] = x
            }
            val tmp = ArrayList<Int>()
            while (stack1.isNotEmpty() && nums[stack1[stack1.size - 1]] < x) {
                tmp.add(stack1.removeAt(stack1.size - 1))
            }
            for (j in tmp.size - 1 downTo 0) stack2.add(tmp[j])
            stack1.add(i)
        }
        return ans
    }
}
